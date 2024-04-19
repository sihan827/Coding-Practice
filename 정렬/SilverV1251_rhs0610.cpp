#include <bits/stdc++.h>
using namespace std;
/*
첫 단어가 최대한 빠른 단어여야 단어 전체가 빠름. 따라서 가장 빠른 첫 단어를 구하고, 2번째 단어를 구하는 식으로 할 것.
*/


int DEBUG = 1;

string input, output;

void Input()
{
	cin >> input;
}

void Process()
{
	
	string first = input.substr(0,1), second = "", last = "";//첫단어/2단어/3단어, 첫 단어는 첫 글자부터 시작
	
	for (int i = 1; i <= input.length() - 2; i++)//첫번째 단어가 될 수 있는 범위는 끝에서 2번째 글자까지만
	{
		string newfirst = input.substr(0, i);//첫글자부터 i개만큼 잘라줌
		if (first.front() < newfirst.back())//first의 첫글자가 newfirst의 마지막 글자보다 빠르면 그냥 통과
		{
			continue;
		}

		reverse(newfirst.begin(), newfirst.end());//newfirst를 뒤집고
		if (first > newfirst)//newfirst가 더 빠르면 바꿔줌
		{
			first = newfirst;
		}
	}
	second = input.substr(first.length(),1);
	for (int i = 1; first.length() + i <= input.length() - 1; i++)//동일한 과정, 그러나 second가 될 수 있는 범위는 length-1까지임
	{
		string newsecond = input.substr(first.length(), i);
		
		if (second.front() < newsecond.back())
			continue;

		reverse(newsecond.begin(), newsecond.end());
		if (second > newsecond)
		{
			second= newsecond;
		}
	}
	last = input.substr(first.length()+second.length());//last는 first와 second를 자르고 남은 나머지
	reverse(last.begin(), last.end());
	output = first + second + last;
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
	while (DEBUG)
	{
	};
	return 0;
}