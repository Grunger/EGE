#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
using namespace std;

int main(int argc, char **argv)
{
	long long n;
	ifstream in("107_27_B.txt");
	in >> n;
	cout << n << endl;
	vector<int> a(n);
	for (int i = 0; i < n; i++) in >> a[i];
	//for (int i = 0; i < n; i++) cout << a[i] << endl;
	cout << endl;
	
	long long m = pow(10, 10);
	long long p = 0;
	
	vector<int> second(n + 1);
	for (int i = 0; i < n; i++) {
		second[i] = a[n - i - 1];
	}	
	/*cout << "a" << endl;
	for (int i = 0; i < n; i++)
		cout << a[i] << " ";
	cout << endl;	
	cout << "second" << endl;
	for (int i = 0; i < n; i++)
		cout << second[i] << " ";
	cout << endl;*/
	int t = clock();
	for (int d = 0; d < n; d++){
		cout << d << endl;
		cout << (clock() - t) / 60000;
		vector<int> second(n + 1);
		for (int i = 0; i < n; i++) {
			second[i] = a[n - i - 1];
		}
	
		int p1 = 1;
		int p2 = n - 1;
		for (int j = 0; j < n; j++){
			long long t1 = 0;
			for (int i = 0; i < p1; i++) t1 = t1 + i * a[i];
			long long t2 = 0;
			for (int i = 0; i < p2; i++) t2 = t2 + (i + 1) * second[i];
			if (max(t1, t2) < m) {
				m = max(t1, t2);
				p = d;
			}
			p1 += 1;
			p2 -= 1;
			
		}
		//cout << endl << endl;
		int tmp = a[0];
		for (int i = 0; i < n - 1; i++) a[i] = a[i + 1];
		a[n - 1] = tmp;
	}
	cout << m << " " << p + 1;
	return 0;
}

