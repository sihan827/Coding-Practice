/*

1번의 이동으로 갈수 있는 최대 거리는 1 (1)
1= 1*(0+1), 1 = 1+0
2번의 이동으로 갈 수 있는 최대 거리는 2 (1 / 1)
2 = 1*(1+1), 2 = 1+1
3번의 이동으로 갈 수 있는 최대 거리는 4 (1 2 / 1)
4 = 2*(1+1), 3 = 2+1
4번의 이동으로 갈 수 있는 최대 거리는 6 (1 2 / 2 1)
6 = 2*(2+1), 4 = 2+2
5번의 이동으로 갈 수 있는 최대 거리는 9 (1 2 3 / 2 1)
9 = 3*(2+1), 7 = 3+2
6번의 이동으로 갈 수 있는 최대 거리는 12 (1 2 3 / 3 2 1)
12 = 3*(3+1), 6 = 3+3
7번의 이동으로 갈 수 있는 최대 거리는 16 (1 2 3 4 / 3 2 1)
16 = 4*(3+1), 7 = 4+3

그리고 그 사이의 값들은 최대 거리에서 Warp 거리를 1씩 줄여나가면 됨
예) 15를 가고싶다면 1 2 3 3 3 2 1 , ...
14를 가고싶다면 1 2 3 2 3 2 1, ...
13을 가고싶다면 1 2 2 2 3 2 1, ...
*/

int DEBUG = 1;

#include <bits/stdc++.h>
using namespace std;

vector<int> input;
vector<int> output;

void Input()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int X, Y;
		cin >> X >> Y;
		input.push_back(Y - X); // 거리만 저장
	}
}

void Process()
{
	for (auto length : input)
	{
		int start = floor(sqrt(length));

		if (length == start * start)
		{
			output.push_back(start * 2 - 1);
		}
		else if (length <= start * (start + 1))
		{
			output.push_back(start * 2);
		}
		else
		{
			output.push_back(start * 2 + 1);
		}
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
	while (DEBUG)
	{
	};
	return 0;
}