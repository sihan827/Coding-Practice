#include <bits/stdc++.h>
using namespace std;

int DEBUG = 1;

int Y1, Y2, M1, M2, D1, D2;
string output;

int MonthDay(int month) // m월 d일 ~ m+1월 d일까지의 날수
{
    if (month > 12)
        month -= 12;
    if (month < 8) // 1~7월
    {
        if (month == 2)
            return 28; // 2월은 28일
        if (month % 2 == 0)
            return 30; // 그 외 짝수달은 30일
        else
            return 31; // 홀수달은 31일
    }
    else // 8~12월
    {
        if (month % 2 == 0)
            return 31; // 짝수달은 31일
        else
            return 30; // 홀수달은 30일
    }
}

int MonthToMonth(int start, int end) // m1월 d일~ m2월 d일까지의 날수
{
    int sum = 0;
    int isReverse = 1;
    if (end < start)
    {
        isReverse = -1;
        swap(start, end);
    }

    for (int i = start; i < end; i++)
    {
        sum += MonthDay(i);
    }
    return sum * isReverse;
}

int YearToYear(int startY, int startM, int endY, int endM) // y1년 m월 d일~y2년 m월d일까지의 날수
{
    int sum = (endY - startY) * 365;
    if (startM > 2) // 올해 2월이 포함되냐?
        startY += 1;
    if (endM <= 2) // 그때 2월 넘어감?
        endY -= 1;
    //if (DEBUG) cout << "LeapYear: " << startY << " to " << endY << endl;
    int modulo = 4;
    startY = startY + ((modulo - (startY % modulo)) % modulo); // 올해 or 다음 윤년으로
    endY = endY - endY % 4;                                    // 끝년 직전 윤년으로
    sum += (endY - startY) / 4 + 1;                            // 윤년 갯수만큼 더해줌
    //if (DEBUG) cout << "4LeapYear: " << startY << " to " << endY << endl;

    modulo = 100;
    startY = startY + ((modulo - (startY % modulo)) % modulo); // 다음 n00년으로
    endY = endY - endY % 100;                                  // 끝년 직전 n00년으로
    sum -= (endY - startY) / 100 + 1;                          // 100년 갯수만큼 빼줌
    //if (DEBUG) cout << "100LeapYear: " << startY << " to " << endY << endl;

    modulo = 400;
    startY = startY + ((modulo - (startY % modulo)) % modulo); // 다음 n400년으로
    endY = endY - endY % 400;                                  // 끝년 직전 n400년으로
    sum += (endY - startY) / 400 + 1;                          // 400년 갯수만큼 더해줌
    //if (DEBUG) cout << "400LeapYear: " << startY << " to " << endY << endl;

    return sum;
}

void Input()
{
    cin >> Y1 >> M1 >> D1;
    cin >> Y2 >> M2 >> D2;
}

void Process()
{
    if (Y2 - Y1 > 1000 || Y2 - Y1 == 1000 && M2 >= M1 && D2 >= D1)
    {
        output = "gg";
        return;
    }
    if (DEBUG)
    {
        cout << "Y2Y: " << YearToYear(Y1, M1, Y2, M2) << endl;
        cout << "M2M: " << MonthToMonth(M1, M2) << endl;
        cout << "D2D: " << D2 - D1 << endl;
    }

    int sum = YearToYear(Y1, M1, Y2, M2) + MonthToMonth(M1, M2) + D2 - D1;
    output = "D-" + to_string(sum);
}

void Output()
{
    cout << output << endl;
}

int main()
{
    Input();
    Process();
    Output();
    while (DEBUG)
    {
        Input();
        Process();
        Output();
    };
    return 0;
}