#include <stdio.h>
#include <stdlib.h>

int main()
{
    char cards_name[3];
    int val = 0;
    int count = 0;
    do{
        puts("输入牌名：");
        scanf("%2s", cards_name);
           
        switch(cards_name[0]){
        case 'J':
        case 'Q':
        case 'K':
            val = 10;
            break;
        case 'A':
            val = 11;
            break;
        case 'X':
            continue;
        default:
            val = atoi(cards_name);
            break;
        }
        printf("%d\n",val);

    /*if val in [3,6] */
    if((val > 2) && (val < 7)){
        puts("计数增加");
        count ++;
    }
    /*if val in [J,Q,K,10]*/
    else if(val == 10){
        puts("计数减少");
        count --;
    }

    if(val <1 || val > 10){
        puts("输入值错误");
        continue;
    }

    printf("当前计数:%d\n", count);
    }while(cards_name[0] != 'X');
    
    printf("输入值为%s\n", cards_name);
    return 0;
}

