#include <stdio.h>
#include <stdlib.h>
typedef char element;

typedef struct node{
    element data;
    struct node *left;
    struct node *right;
} NODE;

typedef struct doubly_linked_list_info{
    NODE *head;
    NODE *cur;
    int length;
} LIST;

void init_list(LIST *list);
void destroy_list(LIST *list); //노드 순회하며 free
int is_empty(LIST *list); 
void add_tail(LIST *list, element item); //연결리스트 맨 뒤에 요소 추가
void insert_node(LIST *list, element item); //cur 뒤에 요소 추가
void delete_node(LIST *list); //cur 노드 free
void goto_first(LIST *list);
void goto_last(LIST *list);
void traverse_front(LIST *list);
void traverse_rear(LIST *list);
void goto_index(LIST *list, int index); //입력한 index로 이동(1부터 시작)
void replace(LIST *list, element item); //cur의 data를 item으로 교체
int data_count(LIST *list);
int is_member(LIST *list, element item);
void clear_list(LIST *list);
void reverse_list(LIST *list); //역순
void print_list(LIST *list);
void data_swap(LIST *list, int index); //해당 index의 data와 cur의 data 교체
element get_data(LIST *list); //cur의 data return



int main(){
    LIST *list = (LIST*)malloc(sizeof(LIST));
    init_list(list);
    printf("+: insert data \n ex) +a +b\n");
    printf("<: go to first data\n");
    printf(">: go to last data\n");
    printf("-: delete data\n");
    printf("N: go to next data\n");
    printf("P: go to previous data\n");
    printf("G: return data\n");
    printf("=: replace data\n ex) =u\n");
    printf("R: reverse list\n");
    printf("C: clear list\n");
    printf("L: print list\n");
    printf("#: count data\n");
    printf("?: data in list? \n ex) ?a ?b\n");
    printf("S: swap data\n ex)S1 S2\n");
    printf("T: add data to tail\n ex) Ta Tb\n");
    printf("E: is the list empty?\n");
    printf("Q: exit\n");
    while (1){
        char command[20] = {'\0'};
        printf("COMMAND: ");
        gets(command);
        if (command[0] == 'Q'){
            printf("QUIT\n");
            destroy_list(list);
            break;
        }
        for (int i = 0; command[i] != '\0'; i++){
            if (command[i] == '+'){
                insert_node(list, command[i+1]);
                i++;
            }
            else if (command[i] == 'T'){
                add_tail(list, command[i+1]);
                i++;
            }
            else if (command[i] == '-'){
                delete_node(list);
            }
            else if (command[i] == '<'){
                goto_first(list);
            }
            else if (command[i] == '>'){
                goto_last(list);
            }
            else if (command[i] == 'N'){
               traverse_front(list);
            }
            else if (command[i] == 'P'){
                traverse_rear(list);
            }
            else if (command[i] >= '0' && command[i] <= '9'){
                int index = 0;
                while (command[i] >= '0' && command[i] <= '9'){
                    index *= 10;
                    index += command[i] - 48;
                    i++;
                }
                i--;
                goto_index(list, index);
            }   
            else if (command[i] == '='){
                replace(list, command[i+1]);
                i++;
            }   
            else if (command[i] == '#'){
                printf("LENGTH: %d\n", list->length);
            }
            else if (command[i] == '?'){
                if (is_member(list, command[i+1]) == -2){
                    printf("EMPTY\n");
                }
                else if (is_member(list, command[i+1]) == -1){
                    printf("NOT MEMBER\n");
                }
                else{
                    printf("INDEX: %d\n", is_member(list, command[i+1]));
                }
                i++;
            }
            else if (command[i] == 'C'){
                clear_list(list);
            }
            else if (command[i] == 'E'){
                if (is_empty(list))
                    printf("TRUE\n");
                else
                    printf("FALSE\n");
            }
            else if (command[i] == 'R'){
                reverse_list(list);
            }
            else if (command[i] == 'L'){
                print_list(list);
            }
            else if (command[i] == 'G'){
                if (get_data(list) == '0'){
                    printf("EMPTY\n");
                }
                else
                    printf("%c RETURNED\n", get_data(list));
            }
            else if (command[i] == 'S'){
                int index = 0;
                i++;
                while (command[i] >= '0' && command[i] <= '9'){
                    index *= 10;
                    index += command[i] - 48;
                    i++;
                }
                i--;
                data_swap(list, index);
            }
        }
    }
    free(list);
    return 0;
}


void init_list(LIST *list){
    list->head = (NODE*)malloc(sizeof(NODE));
    list->head->left = NULL;
    list->head->right = NULL;
    list->cur = list->head;
    list->length = 0;
}

void destroy_list(LIST *list){
    NODE *destroyer = list->head;
    NODE *temp;
    while (destroyer != NULL){
        temp = destroyer->right;
        free(destroyer);
        destroyer = temp;
    }
}

int is_empty(LIST *list){
    if (list->length == 0)
        return 1;
    else
        return 0;
}

void add_tail(LIST *list, element item){
    NODE *newnode = (NODE*)malloc(sizeof(NODE));
    newnode->data = item;
    while (list->cur->right != NULL){
        list->cur = list->cur->right;
    }
    newnode->left = list->cur;
    newnode->right = NULL;
    list->cur->right = newnode;
    (list->length)++;
    list->cur = newnode;
}

void insert_node(LIST *list, element item){
    if (is_empty(list)){
        list->cur = list->head;
        add_tail(list, item);
    }
    else if (list->cur->right == NULL)
        add_tail(list, item);
    else{
        NODE *newnode = (NODE*)malloc(sizeof(NODE));
        newnode->data = item;
        newnode->left = list->cur;
        newnode->right = list->cur->right;
        list->cur->right->left = newnode;
        list->cur->right = newnode;
        list->cur = newnode;
        (list->length)++;
    }
}

void delete_node(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    NODE *temp;
    if (list->cur->right == NULL){
        temp = list->cur->left;
        list->cur->left->right = NULL;
        free(list->cur);
        (list->length)--;
        list->cur = temp;
    }
    else{
        temp = list->cur->right;
        list->cur->left->right = list->cur->right;
        list->cur->right->left = list->cur->left;
        free(list->cur);
        (list->length)--;
        list->cur = temp;
    }
}

void goto_first(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    list->cur = list->head->right;
}

void goto_last(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    while (list->cur->right != NULL){
        list->cur = list->cur->right;
    }
}

void traverse_front(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    else if (list->cur->right == NULL){
        printf("CANT TRAVERSE\n");
        return;
    }
    else{
        list->cur = list->cur->right;
    }
}

void traverse_rear(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    else if (list->cur->left == list->head){
        printf("CANT TRAVERSE\n");
        return;
    }
    else{
        list->cur = list->cur->left;
    }
}

void goto_index(LIST *list, int index){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    else if (list->length < index || index <= 0){
        printf("WRONG INDEX\n");
        return;
    }
    else{
        list->cur = list->head;
        for (int i = 1; i <= index; i++){
            list->cur = list->cur->right;
        }
    }
}

void replace(LIST *list, element item){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    list->cur->data = item;
}

int data_count(LIST *list){
    if (is_empty(list))
        return -1;
    else
        return list->cur->data;
}

int is_member(LIST *list, element item){
    if (is_empty(list))
        return -2;
    NODE *temp = list->head->right;
    for (int i = 1; i <= list->length; i++){
        if (temp->data == item)
            return i;
        else
            temp = temp->right;
    }
    return -1;
}

void clear_list(LIST *list){
    while (list->head->right != NULL){
        delete_node(list);
    }
}

void reverse_list(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    NODE *temp1 = list->head->right;
    NODE *temp2 = list->cur;
    while (temp2->right != NULL){
        temp2 = temp2->right;
    }
    for (int i = 0; i < (list->length) / 2; i++){
        element swap = temp1->data;
        temp1->data = temp2->data;
        temp2->data = swap;
        temp1 = temp1->right;
        temp2 = temp2->left;
    }
}

void print_list(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    NODE *temp = list->head->right;
    for (int i = 0; i < list->length; i++){
        printf("%c ", temp->data);
        temp = temp->right;
    }
    printf("\n");
    printf("Cur: %c\n", list->cur->data);
}

void data_swap(LIST *list, int index){
    if (is_empty(list)){
        printf("EMPTY\n");
        return;
    }
    else if (list->length < index || index <= 0){
        printf("WRONG INDEX\n");
        return;
    }
    else{
        NODE *temp = list->head;
        for (int i = 0; i < index; i++){
            temp = temp->right;
        }
        if (temp == list->cur){
            printf("SAME INDEX\n");
            return;
        }
        element swap = list->cur->data;
        list->cur->data = temp->data;
        temp->data = swap;
        return;
    }
}

element get_data(LIST *list){
    if (is_empty(list)){
        printf("EMPTY\n");
        return 0;
    }
    return list->cur->data;
}
