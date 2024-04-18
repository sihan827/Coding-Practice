#include <bits/stdc++.h>
using namespace std;

int DEBUG = 1;

int N;
vector<string> dic;

bool cmp(const string &s1, const string &s2) //정렬을 위한 연산자
{
    if (s1.size() == s2.size())
    {
        return s1 < s2;
    }
    return s1.size() < s2.size();
}



void Input()
{
	cin >> N;
    for (int i = 0; i < N; i++)
    {
        string line;
        cin >> line;
        dic.push_back(line);
    }
}

void Process()
{
	sort(dic.begin(), dic.end(), cmp); //stl 정렬 이용
    for (auto it = dic.end() - 1; it != dic.begin(); it--)//지워야 할 때는 후위순회가 나음
    {
        if (*it == *(it - 1))
        {
            dic.erase(it);
        }
    }

}

void Output()
{
	for (string line : dic)
        cout << line << endl;
}

int main()
{
	Input();
	Process();
	Output();
	while (DEBUG){};
	return 0;
}