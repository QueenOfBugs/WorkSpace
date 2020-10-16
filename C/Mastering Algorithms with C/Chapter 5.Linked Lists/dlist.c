#include <stdio.h>
#include "dlist.h"
#include <stdlib.h>

int main(){


    return 0;
}

//initialize the double linked list
void dlist_init(DList *list, void (*destory) (void*data)){

    list->size = 0;
    list->destory = destory;

    list->head = NULL;
    list->tail = NULL;

}

// list destory

void dlist_destory(DList *list){
    void *data;
    while(dlist_size(list) > 0){
        if(dlist_rem_next)
    }
}
