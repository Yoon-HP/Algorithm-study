#include <stdio.h>
int main()
{
    int x[10], i, j, cnt = 0;
    for (i = 0; i < 10; i++)
    {
        scanf("%d", &x[i]);
        x[i] %= 42;
    }
    for (i = 0; i < 10; i++)
    {
        int check = 0;
        for (j = 0; j <= i; j++)
        {
            if (x[j] == x[i])
            {
                check++;
            }
        }
        if (check == 1)
        {
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}