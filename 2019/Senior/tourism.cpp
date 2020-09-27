#include <bits/stdc++.h>
using namespace std;

/*
    Finally solved this one. No datastructure bash and runs in O(N).
    Making a DP state with O(N) items was quite difficult, but here is mine:
    
    DP[i] = Maximum value for the first `i` attractions, **keeping the condition that the # of days is minimal**.
    
    The last part is crucial, and tells us that for day `i` there is a specific number of attractions it must visit in order to keep the condition valid.
    This number of attractions is `i % K`. Consider the upper bound of attractions you've already visited, this is K * C, where C is minimal.
    The lower bound of attractions you've visited is `i - K`, where the most recent day takes up all K slots.
    
    This led to my first naive solution, which runs in O(NK) time:
*/

/*
// O(NK) - passes subtask 2
const int MAXN = 1000006;
long long dp[MAXN], arr[MAXN];

int main(){
    cin.sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int N, K; cin >> N >> K;
    for(int i = 0; i < N; ++i) cin >> arr[i];
    for(int i = 0; i < N; ++i){
        long long v = arr[i];
        for(int j = i; j > i - i % K; --j) v = max(v, arr[j]);
        for(int nxt = i - i % K; nxt > max(-1, i - K); --nxt){
            v = max(v, arr[nxt]);
            dp[i] = max(dp[i], v + (nxt == 0 ? 0 : dp[nxt - 1]));
        }
    }
    cout << dp[N - 1] << '\n';
    return 0;
}
*/

/*
    From here on out I will attempt to optimize the inner loop out in order to make it run linear time.
    The first half of the loop computes the subarray max from `i` to `i - i % K` in O(K) time.
    Observation: There are O(K) indices who's left endpoint of the subarray is located at `i - i % K`.
    We can loop in buckets of size K, compute the prefix max at each bucket.

    The second half of the loop is trickier and requires another observation:
    If DP[i] and DP[i + 1] are in the same bucket, then DP[i] >= DP[i + 1] (except for the special case).
    The special case is that when RMQ[i] < RMQ[i + 1] and DP[i + 1] depends on RMQ[i + 1], DP[i] will decrease.
    Otherwise we can take care of the inner loop using a pointer and compute DP[i] in amortized constant time for every bucket.
*/

const int MAXN = 1000006;
long long dp[MAXN], arr[MAXN], rmq[MAXN];

int main(){
    cin.sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int N, K; cin >> N >> K;
    for(int i = 0; i < N; ++i) cin >> arr[i];
    for(int i = 0; i < N; i += K){
        rmq[i] = arr[i];
        for(int j = i + 1; j < min(N, i + K); ++j) rmq[j] = max(rmq[j - 1], arr[j]);
    }
    for(int j = 0; j < N; j += K){
        long long cmax = arr[j];
        for(int c = 0, i = min(N - 1, j + K - 1); i >= j; --i){
            if(cmax <= rmq[i + 1]) dp[i] = dp[i + 1] - (rmq[i + 1] - rmq[i]); // Special case
            else dp[i] = dp[i + 1];
            while(j - c >= max(0, i - K + 1)){
                assert(j >= c);
                cmax = max(cmax, arr[j - c]);
                dp[i] = max(dp[i], max(rmq[i], cmax) + (j == c ? 0 : dp[j - c - 1]));
                ++c;
            }
        }
    }
    cout << dp[N - 1] << '\n';
    return 0;
}
