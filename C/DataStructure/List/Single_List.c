#include <stdio.h>
#include <stdlib.h>

// 1. 创建节点
//
// 1.1 节点类型
struct Node{
    //存储数据
    int data;
    //连接节点
    struct Node * Next;
}typedef node;// 这也是给节点起别名

// 给节点起别名
//typedef struct Node node;

//使用函数前要先声明
node * createNode(int data);

int main()
{
    node *First = createNode(10);
    printf("First Node's data = %d %d",First->data,First->Next);
    printf("Hello world\n"); 

    return 0;
}

node* createNode(int data){
    // 1.2.1 准备空间 开内存 申请内存
    node* pNew = (node *)malloc(sizeof(node));
    if(pNew == NULL){
        return NULL;
    }
    // 1.2.2 设置数据
    pNew->data = data;
    pNew->Next = NULL;
    // 1.2.3 返回制造的节点
    return pNew;
}
