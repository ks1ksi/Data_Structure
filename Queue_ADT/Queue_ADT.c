#include <stdio.h>
#define MAX_SIZE 10

typedef char element;
typedef struct Circular_Queue{
    element arr[MAX_SIZE];
    int front;
    int rear;
    int len;
} Queue;

void init_queue(Queue *queue){
    queue->front = 0;
    queue->rear = 0;
    queue->len = 0;
}

int is_full(Queue *queue){
    if (queue->front % MAX_SIZE == (queue->rear + 1) % MAX_SIZE)
        return 1;
    else
        return 0;
}

int is_empty(Queue *queue){
    if (queue->front == queue->rear)
        return 1;
    else
        return 0;
}

void enqueue(Queue *queue, element item){
    if (is_full(queue)){
        printf("FULL\n");
        return;
    }
    if (queue->rear == MAX_SIZE - 1)
        queue->rear = 0;
    else
        (queue->rear)++;
    queue->arr[queue->rear] = item;
    (queue->len)++;
}

element dequeue(Queue *queue){
    if (is_empty(queue)){
        printf("EMPTY\n");
        return 0;
    }
    if (queue->front == MAX_SIZE - 1)
        queue->front = 0;
    else
        (queue->front)++;
    (queue->len)--;
    return queue->arr[queue->front];
}

element peek(Queue *queue){
    if (is_empty(queue)){
        return 0;
    }
    int idx = queue->front;
    if (queue->front == MAX_SIZE - 1)
        idx = 0;
    else
        idx++;
    return queue->arr[idx];
}

void print_queue(Queue *queue){
    if (is_empty(queue)){
        printf("EMPTY\n");
        return;
    }
    Queue temp;
    init_queue(&temp);
    while (!is_empty(queue)){
        printf("%c ", peek(queue));
        enqueue(&temp, dequeue(queue));
    }
    printf("\n");
    while (!is_empty(&temp))
        enqueue(queue, dequeue(&temp));
}

void front(Queue *queue){
    printf("front: %d\n", queue->front);
}

void rear(Queue *queue){
    printf("rear: %d\n", queue->rear);
}

int data_count(Queue *queue){
    return queue->len;
}


int is_member(Queue *queue, element item){
    if (is_empty(queue)){
        printf("EMPTY\n");
        return -1;
    }
    int tf = 0;
    Queue temp;
    init_queue(&temp);
    while (!is_empty(queue)){
        if (peek(queue) == item)
            tf = 1;
        enqueue(&temp, dequeue(queue));
    }
    while (!is_empty(&temp))
        enqueue(queue, dequeue(&temp));
    return tf;
}

void replace(Queue *queue, element item){
    if (is_empty(queue)){
        printf("EMPTY\n");
        return;
    }
    queue->arr[queue->rear] = item;
}

void clear_queue(Queue *queue){
    while (!is_empty(queue)){
        dequeue(queue);
    }
}

int howmanydequeue(Queue *queue, element item){
    if (is_empty(queue)){
        printf("EMPTY\n");
        return -1;
    }
    int count;
    int tf = 0;
    Queue temp;
    init_queue(&temp);
    while (!is_empty(queue)){
        if (peek(queue) == item){
            tf = 1;
            count = temp.len + 1;
        }
        enqueue(&temp, dequeue(queue));
    }
    while (!is_empty(&temp))
        enqueue(queue, dequeue(&temp));
    if (tf == 0)
        return 0;
    else
        return count;
}

void minimize_queue(Queue *queue, int num){
    if (is_empty(queue)){
        printf("EMPTY\n");
        return;
    }
    else if (queue->len <= num){
        printf("WRONG NUM\n");
        return;
    }
    int count = queue->len - num;
    while (count > 0){
        dequeue(queue);
        count--;
    }
}

void find_and_replace(Queue *queue, element item1, element item2){
    if (is_empty(queue)){
        printf("EMPTY\n");
        return;
    }
    Queue temp;
    init_queue(&temp);
    int count = howmanydequeue(queue, item1);
    if (count == 0){
        printf("NO DATA\n");
        return;
    }
    while (count > 0){
        enqueue(&temp, dequeue(queue));
        count--;
    }
    replace(&temp, item2);
    while (!is_empty(queue))
        enqueue(&temp, dequeue(queue));
    while (!is_empty(&temp))
        enqueue(queue, dequeue(&temp));
}





int main(){
    Queue cq;
    init_queue(&cq);
    printf("+: enqueue data\n ex) +a +b\n");
    printf("-: dequeue data\n");
    printf("P: peek data\n");
    printf("L: print queue\n");
    printf("#: count data\n");
    printf("F: is full?\n");
    printf("E: is empty?\n");
    printf("H: print head(front)\n");
    printf("T: print tail(rear)\n");
    printf("=: replace data at tail\n ex) =u\n");
    printf("?: is member?\n ex) ?m\n");
    printf("h: how many dequeues to get data?\n ex) ha hb\n");
    printf("M: minimize queue\n ex) M2 M3\n");
    printf("f: find item and replace\n ex) fab -> a will be replaced to b\n");
    printf("C: clear queue\n");
    printf("NUM: dequeue 'num' times\n");
    printf("MAX SIZE: %d\n", MAX_SIZE - 1);
    printf("Q: quit\n");
    while (1){
        printf("COMMAND: ");
        char command[20];
        gets(command);
        if (command[0] == 'Q')
            break;
        for (int i = 0; command[i] != '\0'; i++){
            if (command[i] == '+'){
                enqueue(&cq, command[i+1]);
                i++;
            }
            else if (command[i] == '-'){
                dequeue(&cq);
            }
            else if (command[i] == 'P'){
                if (peek(&cq) == 0){
                    printf("EMPTY\n");
                }
                else{
                    printf("%c returned\n", peek(&cq));
                }
            }
            else if (command[i] == 'L'){
                print_queue(&cq);
            }
            else if (command[i] == '#'){
                printf("%d\n", data_count(&cq));
            }
            else if (command[i] == 'F'){
                if (is_full(&cq))
                    printf("TRUE\n");
                else
                    printf("FALSE\n");
            }
            else if (command[i] == 'E'){
                if (is_empty(&cq))
                    printf("TRUE\n");
                else
                    printf("FALSE\n");
            }
            else if (command[i] == 'H'){
                front(&cq);
            }
            else if (command[i] == 'T'){
                rear(&cq);
            }
            else if (command[i] == '='){
                replace(&cq, command[i+1]);
                i++;
            }
            else if (command[i] == '?'){
                if (is_member(&cq, command[i+1]))
                    printf("TRUE\n");
                else if (is_member(&cq, command[i+1]) == -1)
                    printf("EMPTY\n");
                else
                    printf("FALSE\n");
            }
            else if (command[i] == 'h'){
                if (howmanydequeue(&cq, command[i+1]) == -1)
                    printf("EMPTY\n");
                else if (howmanydequeue(&cq, command[i+1]) == 0)
                    printf("NO DATA\n");
                else
                    printf("YOU NEED %d TIMES OF DEQUEUE\n", howmanydequeue(&cq, command[i+1]));
                i++;
            }
            else if (command[i] == 'M'){
                minimize_queue(&cq, command[i+1] - 48);
                i++;
            }
            else if (command[i] == 'f'){
                find_and_replace(&cq, command[i+1], command[i+2]);
                i+=2;
            }
            else if (command[i] == 'C'){
                clear_queue(&cq);
            }
            else if ('0' <= command[i] && command[i] <= '9'){
                int count = command[i] - 48;
                while (count > 0){
                    dequeue(&cq);
                    count--;
                }
            }
        }
    }
    return 0;
}