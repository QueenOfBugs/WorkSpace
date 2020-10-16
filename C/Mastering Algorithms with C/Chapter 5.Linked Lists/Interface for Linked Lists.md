|name|Synopsis|Return Value|Description|Complexity|
| :------:| :------: | :------: | :------: | :------: |
|list_init|void list_init(List \*list, void (\*destory)(void \*data));|None|initializes the linked list specified by **list**.Must be called for a linked list before the list can be used for any other operation.The **destory** argument provide a way to free dynamically allocated data when **list_destory** is called. **destory** should be set to free or a user-defined function to free the  dynamically allocated members as well as structure itself|**O(1)**|
|list_destory|void list_destory(List \*list);|None|destroy the linked list specified by list.No other operations are permitted after calling **list_destory** unless **list_init** is called again. The **list_destory** operation removes all elements from a linked list and calls the function passed as **destory** to **list_init** once for each elements as it is removed, provided destory was not set to NULL.|**O(*n*)**,where n is the number of the elements in the linked list.|
|list_ins_next|int list_ins_next(List \*list, ListElmt \*element, const void *data);|0 if inserting the element is successful, or -1 otherwise.|Insert an element just after **element** in the linked list specified by **list**. If **element** is NULL, the new element is inserted at ther head of the list. The new element contains a pointer to **data**, sod the memory referenced by **data** should remain vallid as long as the element remains in the list. It is the responsibility of the caller to manager the storage associated with **data**.|**O(1)**|
|list_rem_next|int list_rem_next(List \*list, ListElmt \*element, void **data);|0 if removing the element is successful,or -1 otherwise.|Removes the element just after **element** from the linked list specified by **list**.If **element** is NULL, the element at the head of the linked list is removed. Upon return,**data** points to the data stored in the element that was removed. It is the responsibility of the caller to manage the storage associated with the data|**O(1)**|
|list_size|int list_size(const List \*list);|Number of the elements in the list.|Macro that evaluates to the number of elements in the linked list specified by **list**.|**O(1)|
|list_head|ListElmt \*list_head(const List \*list);|Element at the head of the list|Macro that evaluates to the element at the head of the linked list specified by **list**.|**O(1)**|
|list_tail|ListElmt \*list_tail(const List \*list);|Element at the tail of the list|macro that evaluates to the element at the tail of the linked list specified by **list**.|**O(1)**|
|list_is_head|int list_is_head(const ListElmt \*element);|1 if the element is at the head of the list, or otherwise.|Macro that determines whether the element specified as **element** is at the head of a linked list.|**O(1)**|
|list_is_tail|int list_is_tail(ListElmt \*element);|1 if the element is at the head of the list, or otherwise.|Macro that determinse whether the element specified as **element** is at the tail of a linked list.|**O(1)**|
|list_data|void \*list_data(const ListElmt \*element);|Data stored in the element.|Macro that evaluates to the data stored in the element of a linked list specified bu **element**.|**O(1)**|
|list_next|ListElmt \*list_next(const ListElmt \*element);|Element following the specified element.|Macro that evaluates to the element of a linked list following the element specified by **element**.|**O(1)**|

## list_init
The **list_init** operation initializes a linked list so that it can be used in other operations. Initializing a linked list is a simple operation in which the size member of the list is set to 0,the **destory** member to **destory**, and the **head** and **tail** pointers to NULL.

The runtime complexity of **list_init** is **O(1)** because all of the steps in initializing a linked list run in a constant amount of time.

## list_destory


