#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "list.h"

// list_init

void list_init(List *list, void (*destory)(void *data)){
    list->size = 0;
    list->destory = destory;
    list-> head = NULL;
    list->tail = NULL;

    return;
}

// list_destory

void list_destory(List *list){
    void *data;
    // remove each element
    while(list_size(list) > 0){
        if(list_rem_next(list, NULL, (void **)&data) == 0 && list->destory != NULL){
            // call a user-defined function to free dynamically allocated data.
            
            list->destory(data);
        }
        
    }
    // no operatioons are allowed ,but clear the structure as a precaution.
memset(list, 0, sizeof(List));
return;
}

// list_ins_next

int list_ins_next(List *list, ListElmt *element, const void *data){
    ListElmt *new_element;

    //alocate storage for the element.
    
    if((new_element = (ListElmt *) malloc(sizeof(ListElmt))) == NULL){
        return -1;
    }

    //insert the element into the list.
    
    new_element->data = (void *)data;
    if(element == NULL){
        // insert at the head of the list
        if(list_size(list) == 0){
            list->tail = new_element;
        }
        new_element->next = list->head;
        list->head = new_element;

    }
    else{
        //insert at somewhere other than at the head 
        

        // insert at the end of the list.
        if(element->next == NULL){
            list->tail = element;
        }
        new_element->next = element->next;
        element->next = new_element;
    }
    list->size ++;
    return 0;
}

// list_rem_next
 
int list_rem_next(List *list, ListElmt *element, void **data){
    ListElmt *old_element;
    // do not allow removal from an empty list.
    
    if(list_size(list) == 0){
        return -1;
    }

    //remove the element from the list
    
    if(element == NULL){
        //handle removal from the head of the list 

        *data = list->head->data;
        old_element = list->head;
        list->head = list->head->next;

        // if the list has only one element.
        if(list_size(list) == 1){
            list->tail = NULL;
        }
    }
    else{
        // handle removal from somewhere other than the head.

        if(element->next == NULL){
            //element is at the tail of the list
            return -1;
        }
        *data = element->next->data;
        old_element = element->next;
        element->next = element->next->next;

        if(element->next == NULL){
            list->tail = element;
        }

    }
    // free the storage allocated by abstract datatype.
    free(old_element);
    list->size --;
    return 0;
}



int main()
{
    printf("Hello world\n");
    return 0;
}

