#include <stdio.h>

void go_south_east(int *lat, int *lon){
//    优先级问题 -- 优先级高于 * 
//    下面的写法会是(指针)地址lat加一后的地址存放的数据的值加一/减一
//    *lat --;
//    *lon ++;
    (*lat) --;
    (*lon) ++;
//    *lat = *lat - 1;
//    *lon = *lon + 1;
//   printf("%d%d\n",*lat,*lon);
}
int main()
{
    int latitude = 32;
    int longitude = -64;
    go_south_east(&latitude, &longitude);
    //printf("test");
    printf("la:%d,lo:%d\n",latitude,longitude);
    return 0;
}

