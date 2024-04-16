#include <bits/stdc++.h>
using namespace std;

int DEBUG = 1;

/*
Xcm를 만드는데 필요한 막대의 갯수는 2진수로 나타냈을때의 비트수가 됨
*/

int input, output = 0;
void Input()
{
	cin >> input;
}

void Process()
{
	for (int i = 0; i < 8; i++)//한개씩 비트를 줄여가며 더함
	{
		output += input&1;
		input = input >> 1;
	}
}

void Output()
{
	cout << output;
}

int main()
{
	Input();
	Process();
	Output();
	while (DEBUG){};
	return 0;
}