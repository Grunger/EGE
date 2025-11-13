#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int main() {
  ifstream Fin( "27-b.txt" );
  int N, s = 0, dMin = 10001;
  Fin >> N;
  for( int i = 0; i < N; i++ ) {
  	 int a, b;
     Fin >> a >> b;	 
     s += max( a, b );
     int d = abs( a-b );
     if( d % 3 > 0 )
       dMin = min( d, dMin );
    }

  if( s % 3 != 0 )
    cout << s;
  else
    cout << s-dMin; 
}
  
