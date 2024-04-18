#include <bits/stdc++.h>
using namespace std;

int DEBUG = 1;

/*
↗1개 ↙2개 ↗3개... 순으로 나아감
1~n까지의 합은 n(n+1)/2
*/

int X= 0, numerator = 0, denominator = 0;
void Input()
{
	cin >> X;
}

void Process()
{
	int n = 1;
	while (n*(n+1) < X*2) n++; //n을 구했음
	//n이 홀수라면 n(n+1)/2번째 분수는 n/1이고 짝수라면 1/n임

	int diff = n*(n+1)/2 - X; //n(n+1)/2와의 차이를 구함. 이때 분자+분모= n+1이 나옴
	//분자 or 분모는 각각 diff+1, n-diff가 나옴

	if (n%2 == 1) //n이 홀수면 분모가 diff+1
	{
		numerator= diff+1;
		denominator= n-diff;
	}
	else //n이 짝수면 분자가 diff+1
	{
		numerator= n-diff;
		denominator= diff+1;
	}

}

void Output()
{
	cout << numerator << "/" << denominator << endl;
}

int main()
{
	Input();
	Process();
	Output();
	while (DEBUG){};
	return 0;
}