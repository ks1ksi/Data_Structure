#include <stdio.h>
#include <stdlib.h>

typedef char element;
typedef struct Node{
    element data;
    struct Node *left;
    struct Node *right;
} Node;
typedef struct Deque{
    Node *front;
    Node *rear;
    int len;
} Deque;

void init_deque(Deque *dq);
int is_empty(Deque *dq);
void push_back(Deque *dq, element item);
void push_front(Deque *dq, element item);
element pop_back(Deque *dq);
element pop_front(Deque *dq);
element peek_back(Deque *dq);
element peek_front(Deque *dq);
void print_deque(Deque *dq);
void clear_deque(Deque *dq);
int is_member(Deque *dq, element item);
void destroy(Deque *dq);

int main(){
    Deque dq;
    init_deque(&dq);
    printf("+< or +>: push front or back\n ex) +>a +<b\n");
    printf("-< or ->: pop front or back\n");
    printf("P<, P>: get front or back\n");
    printf("L: print deque\n");
    printf("C: clear deque\n");
    printf("E: is empty?\n");
    printf("?: is memeber?\n ex) ?u\n");
    printf("#: count data\n");
    printf("Q: quit\n");
    while (1){
        printf("COMMAND: ");
        char command[30];
        gets(command);
        if (command[0] == 'Q'){
            destroy(&dq);
            break;
        }
        for (int i = 0; command[i] != '\0'; i++){
            if (command[i] == '+'){
                if (command[i+1] == '<'){
                    push_front(&dq, command[i+2]);
                }
                else if (command[i+1] == '>'){
                    push_back(&dq, command[i+2]);
                }
                i += 2;
            }
            else if (command[i] == '-'){
                if (is_empty(&dq)){
                    printf("EMPTY\n");
                }
                else if (command[i+1] == '<'){
                    pop_front(&dq);
                }
                else if (command[i+1] == '>'){
                    pop_back(&dq);
                }
                i++;
            }
            else if (command[i] == 'P'){
                if (is_empty(&dq)){
                    printf("EMPTY\n");
                }
                else if (command[i+1] == '<'){
                    printf("%c RETURNED\n", peek_front(&dq));
                }
                else if (command[i+1] == '>'){
                    printf("%c RETURNED\n", peek_back(&dq));
                }
                i++;
            }
            else if (command[i] == 'L'){
                print_deque(&dq);
            }
            else if (command[i] == 'C'){
                clear_deque(&dq);
            }
            else if (command[i] == '#'){
                printf("%d\n", dq.len);
            }
            else if (command[i] == '?'){
                if (is_member(&dq, command[i+1]) == -1)
                    printf("EMPTY\n");
                else if (is_member(&dq, command[i+1]))
                    printf("TRUE\n");
                else
                    printf("FALSE\n");
                i++;
            }
            else if (command[i] == 'E'){
                if (is_empty(&dq)){
                    printf("TRUE\n");
                }
                else{
                    printf("FALSE\n");
                }
            }
        }
    }

    return 0;
}

void init_deque(Deque *dq){
    dq->len = 0;
    dq->front = NULL;
    dq->rear = NULL;
}

int is_empty(Deque *dq){
    if (dq->len == 0)
        return 1;
    else
        return 0;
}

void push_back(Deque *dq, element item){
    Node *node = (Node*)malloc(sizeof(Node));
    node->data = item;
    if (is_empty(dq)){
        node->left = NULL;
        node->right = NULL;
        dq->front = node;
        dq->rear = node;
    }
    else{
        node->left = dq->rear;
        node->right = NULL;
        dq->rear->right = node;
        dq->rear = node;
    }
    (dq->len)++;
}

void push_front(Deque *dq, element item){
    Node *node = (Node*)malloc(sizeof(Node));
    node->data = item;
    if (is_empty(dq)){
        node->left = NULL;
        node->right = NULL;
        dq->front = node;
        dq->rear = node;
    }
    else{
        node->left = NULL;
        node->right = dq->front;
        dq->front->left = node;
        dq->front = node;
    }
    (dq->len)++;
}

element pop_back(Deque *dq){
    if (is_empty(dq)){
        return 0;
    }
    else if (dq->len == 1){
        element rdata = dq->rear->data;
        free(dq->rear);
        init_deque(dq);
        return rdata;
    }
    else{
        Node *temp = dq->rear;
        element rdata = temp->data;
        dq->rear = temp->left;
        free(temp);
        dq->rear->right = NULL;
        (dq->len)--;
        return rdata;
    }
}

element pop_front(Deque *dq){
    if (is_empty(dq)){
        return 0;
    }
    else if (dq->len == 1){
        element rdata = dq->front->data;
        free(dq->front);
        init_deque(dq);
        return rdata;
    }
    else{
        Node *temp = dq->front;
        element rdata = temp->data;
        dq->front = temp->right;
        free(temp);
        dq->front->left = NULL;
        (dq->len)--;
        return rdata;
    }

}

element peek_back(Deque *dq){
    if (is_empty(dq)){
        return 0;
    }
    return dq->rear->data;
}

element peek_front(Deque *dq){
    if (is_empty(dq)){
        return 0;
    }
    return dq->front->data;
}

void print_deque(Deque *dq){
    if (is_empty(dq)){
        printf("EMPTY\n");
        return;
    }
    Node *temp = dq->front;
    while (temp != NULL){
        printf("%c ", temp->data);
        temp = temp->right;
    }
    printf("\n");
}

void clear_deque(Deque *dq){
    while (!is_empty(dq)){
        pop_back(dq);
    }
}

int is_member(Deque *dq, element item){
    if (is_empty(dq)){
        return -1;
    }
    int tf = 0;
    Deque temp;
    init_deque(&temp);
    while (!is_empty(dq)){
        if (peek_back(dq) == item){
            tf = 1;
            break;
        }
        else
            push_back(&temp, pop_back(dq));
    }
    while (!is_empty(&temp))
        push_back(dq, pop_back(&temp));
    return tf;
}

void destroy(Deque *dq){
    Node *temp = dq->front;
    while (temp->right != NULL){
        temp = temp->right;
        free(temp->left);
    }
    free(temp);
}