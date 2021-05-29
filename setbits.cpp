/*You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).

Example 1:

Input: N = 4
Output: 5
Explanation:
For numbers from 1 to 4.
For 1: 0 0 1 = 1 set bits
For 2: 0 1 0 = 1 set bits
For 3: 0 1 1 = 2 set bits
For 4: 1 0 0 = 1 set bits
Therefore, the total set bits is 5.*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll dp[1000001];
ll sum_bits[1000001];
void solve()
{
    ll range = 1e6;
    ll n = range + 1;
    ll sum = 0;
    for (ll i = 1; i < range; i++){
        dp[i] = dp[i >> 1] + i % 2;  //or dp[i]=dp[i >> 1] + (i & 1);
        // ">>" denoted as Right Shift
        //Takes two numbers, right shifts the bits of the first operand, 
        //the second operand decides the number of places to shift. In other words right shifting 
        //an integer “x” with an integer “y” denoted as ‘(x>>y)‘ is equivalent to dividing x with 2^y.
        sum += dp[i];
        sum_bits[i] = sum;
    }
}

int main()
{
    int t;
    cin >> t;
    while (t--){
        ll n;
        cin >> n;
        solve();
        cout << sum_bits[n] << "\n";
    }
    return 0;
}

/*
int countSetBits(int n)
    {
        n++;
        int count = 0, rem, t = 1;
        while (t <= n) {
            count += (n / (t * 2)) * t;
            rem = (n % (t * 2)) - t;
            if (rem > 0)
                count += rem;
            
            t = t << 1;
            // Denoted as Left Shift  
            //Takes two numbers, left shifts the bits of the first operand, the second operand 
            //decides the number of places to shift. Or in other words left shifting an 
            //integer “x” with an integer “y” denoted as ‘(x<<y)’ is equivalent to 
            //multiplying x with 2^y (2 raised to power y). 
        }
        return count;
    }
*/