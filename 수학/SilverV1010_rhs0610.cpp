// 조합 문제

#include <bits/stdc++.h>
using namespace std;



struct NM
{
	int N, M;
};

vector<NM> input;
vector<long int> output;

long int Combination(int n, int r)//조합
{
	long long int result = 1;
	if (r > n / 2)
	{
		r = n - r;
	}

	for (int i = 1; i <= r; i++)//n~n-r+1까지 다 곱하면 오버플로우 날수도 있으니 한단계씩
	{
		result = result * (n-i+1)/i;
	}
	return result;
}

void Input()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N, M;
		cin >> N >> M;
		input.push_back({N, M});
	}
}

void Process()
{
	for (auto nm : input)
	{
		int n = nm.N, m = nm.M;
		output.push_back(Combination(m, n));
	}
}

void Output()
{
	for (auto result : output)
	{
		cout << result << endl;
	}
}

int main()
{
	Input();
	Process();
	Output();
	return 0;
}