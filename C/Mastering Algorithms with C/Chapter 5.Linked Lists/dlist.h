// dlist.h

#ifndef DLIST_H
#define DLIST_H

typedef struct DListElemt_{
    void *data;
    struct DListElemt_ *prev;
    struct DListElemt_ *next;
}DListElemt;

typedef struct DList_{
    int size;
    
    int (*match)(const void *key1, const void *key2);
    void (*destory)(void *data);

    DList_ *head;
    DList_ *tail;

}DList;

//Public Interface

void dlist_init(DList *list, void (*destory)(void *data));

void dlist_destory(DList *list);

int dlist_ins_prev(DList *list,DListElemt *element,const void *data);

int dlist_ins_next(DList *list,DListElemt *element,const void *data);

int dlist_rem_next(DList *list,DListElemt *element, void **data);

#define dlist_size(list) ((list)->size)

#define dlist_head(list) ((list)->head)

#define dlist_tail(list) ((list)->tail)

#define dlist_is_head(element) ((element)->prev == NULL ? 1:0) 

#define dlist_is_tail(element) ((element)->next == NULL ? 1:0)

#define dlist_data(element) ((elemenmt)->data)

#define dlist_next(element) ((element)->next)

#define dlist_prev(element) ((element)->prev)
#endif
