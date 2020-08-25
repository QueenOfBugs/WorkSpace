#include <stdio.h>

void test(char str[]){
    printf("%s\n",str);
    printf("sizeof:%i",sizeof(str));


}
int main()
{
    char str1[10] = "testqqs";

    printf("%c",3[str1]);
    char *s;
    test(str1);
    s = str1;
    printf("%p\n",&s);
    printf("%p\n",str1);
    printf("Hello world\n");
    return 0;
}

