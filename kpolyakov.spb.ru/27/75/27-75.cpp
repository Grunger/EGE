#include<iostream>
#include<fstream>
using namespace std;

int main()
{
  const int K = 43;	
  ifstream F("27-75a.txt");
  int N;
  F >> N;
  int tailSum[K] = {0};
  for( int i=1;i<K;i++) tailSum[i] = -1;
  int tailLen[K] = {0};
  int maxSum = 0;
  int minLen = 1000000000;
  int totalSum = 0;
  for( int i=0; i<N; i++ ) {
    int x;
    F >> x;
    totalSum += x;
    int r = totalSum % K;
    if( tailSum[r] != -1 ) {
      int curSum = totalSum - tailSum[r];
      int curLen = i - tailLen[r] + 1;
      if( (curSum > maxSum) or 
          ((curSum == maxSum) and (curLen < minLen)) ) {
         maxSum = curSum;
         minLen = curLen;
         } 
       } 
     else {
       tailSum[r] = totalSum;
       tailLen[r] = i+1;
	      }
  }
cout << minLen;
}
