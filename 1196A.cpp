#include <iostream>
#include <math>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int sum = 0;
    int Candies[n][3];
    for ( int i = 0 ; i < n ; i++ )
    {
        for ( int j = 0 ; j < 3 ; j++ )
            cin >> Candies[i][j];
    }

    for ( int i = 0 ; i < n ; i++ )
    {
        sum = 0;
        for ( int j = 0 ; j < 3 ; j++ )
            sum = sum + Candies[i][j];

        cout << sum << "\n";
    }

}
