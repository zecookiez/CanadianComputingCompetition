#include <bits/stdc++.h>
using namespace std;

/*

 Subtask 1 - Dynamic Programming
 
     Let dp[sz][row][col] represent the maximum element of the subtriangle of size sz with the tip at [row, col].
     
     To calculate each state, you need to have dp[sz - 1][row + 1][col] and dp[sz - 1][row + 1][col + 1].
     
     Look at why this is true -- to build a triangle of size X + 1 you need the lower two subtriangles of size X, along with the subtriangle at the tip.
     
     We can loop through the sizes from 1 to K.
         Go through every point of a subtriangle of size K.
             Grab the maximum item of the three subtriangles for every point.
     
     This results in an O(N^2 * K) algorithm with a very good constant, as there are N^2 cells for every iteration of K.

 Full solution - Optimizing the recurrence

     First, observe that K iterations is a lot. If we draw the overlaps of the 3 subtriangles, there are a lot of overlapping cells!
     
     If we can find some optimal smaller triangles that overlap less, we can avoid calculating some states of dp[sz], saving time.

     As a matter of fact, we can. The optimal triangle size is CEIL(sz / 3 * 2), try drawing a triangle and see why (draw an equilateral triangle with 9 mini triangles).

     Alternatively, make *2* dp tables, one for subtriangles with the tip at the top, one for subtriangles with the tip at the bottom.
     
     We can make the larger triangle with 3 right-side up triangles of sz/2, and 1 upside-down triangle of sz/2.

     Both will save sz/CONSTANT states every step, turning the K loop into a log(K) loop.
     
     Time complexity:  O(N^2 log K).
     Space complexity: O(N^2).

 */

int n, k, dp[3005][3005];

void helper(int sz){

    if(sz == 1) return;

    int overlap = sz * 2 / 3 + (sz % 3 != 0 && sz > 2);

    helper(overlap);

    for(int K, j = 0; j <= n - sz; ++j)
        for(K = 0; K <= j; ++K)
            dp[j][K] = max(dp[j][K], max(dp[j + sz - overlap][K], dp[j + sz - overlap][K + sz - overlap]));

}

int main(){

    cin.sync_with_stdio(0); cin.tie(0); cout.tie(0);

    cin >> n >> k;

    //dp[row][col] -> max element at size [row][col] at the top

    for(int j, i = 0; i < n; ++i)
        for(j = 0; j <= i; ++j)
            cin >> dp[i][j];

    helper(k);

    long long tot = 0;

    for(int j, i = 0; i <= n - k; ++i)
        for(j = 0; j <= i; ++j)
            tot += dp[i][j];

    cout << tot << "\n";

    return 0;

}
