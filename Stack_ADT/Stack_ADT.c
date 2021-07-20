#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 10

typedef char element;
typedef struct Stack{
    element arr[MAX_SIZE];
    int top;
}Stack;

void init_stack(Stack *stack){
    stack->top = -1;
}

int is_full(Stack *stack){
    if ((stack->top) + 1 == MAX_SIZE)
        return 1;
    else
        return 0;
}

int is_empty(Stack *stack){
    if (stack->top == -1)
        return 1;
    else
        return 0;
}

void push(Stack *stack, element item){
    if (is_full(stack)){
        printf("FULL\n");
        return;
    }
    stack->arr[++(stack->top)] = item;
}

element pop(Stack *stack){
    if (is_empty(stack))
        return 0;
    else
        return stack->arr[(stack->top)--];
}

element peek(Stack *stack){
    if (is_empty(stack))
        return 0;
    else
        return stack->arr[stack->top];
}

void print_stack(Stack *stack){
    if (is_empty(stack)){
        printf("EMPTY\n");
        return;
    }
    Stack temp;
    init_stack(&temp);
    while (is_empty(stack) == 0){
        push(&temp, pop(stack));
    }
    while (is_empty(&temp) == 0){
        printf("%c ", peek(&temp));
        push(stack, pop(&temp));
    }
    printf("\n");
}

int element_count(Stack *stack){
    return (stack->top) + 1;
}

void top_stack (Stack *stack){
    if (is_empty(stack)){
        printf("EMPTY\n");
        return;
    }
    printf("(%d, %c)\n", (stack->top) + 1, stack->arr[stack->top]);
}

int is_member(Stack *stack, element item){
    if (is_empty(stack))
        return -1;
    Stack temp;
    init_stack(&temp);
    int tf = 0;
    while (is_empty(stack) == 0){
        if (peek(stack) == item){
            tf = 1;
            break;
        }
        else
            push(&temp, pop(stack));
    }
    while (is_empty(&temp) == 0){
        push(stack, pop(&temp));
    }
    return tf;
}

void clear_stack(Stack *stack){
    if (is_empty(stack)){
        printf("EMPTY\n");
        return;
    }
    while (is_empty(stack) == 0){
        pop(stack);
    }
}

void replace(Stack *stack, element item){
    if (is_empty(stack)){
        printf("EMPTY\n");
        return;
    }
    stack->arr[stack->top] = item;
}

int howmanypops(Stack *stack, element item){
    if (is_empty(stack))
        return -1;
    Stack temp;
    init_stack(&temp);
    int tf = 0;
    while (is_empty(stack) == 0){
        push(&temp, pop(stack));
        if (temp.arr[temp.top] == item){
            tf = 1;
            break;
        }
    }

    if (is_empty(stack)){
       while(is_empty(&temp) == 0){
           push(stack, pop(&temp));
       }
       if (tf = 1){
           return stack->top + 1;
       }
       else
            return -2;
    }
    else{
        int num = (temp.top) + 1;
        while (is_empty(&temp) == 0){
            push(stack, pop(&temp));
        }
        return num;
    }
}

void minimize (Stack *stack, int num){
    if (stack->top + 1 <= num){
        printf("WRONG NUM\n");
        return;
    }
    else if (is_empty(stack)){
        printf("EMPTY\n");
        return;
    }
    while (stack->top + 1 > num){
        pop(stack);
    }
}

void replace_by_index (Stack *stack, element item, int idx){
    if (is_empty(stack)){
        printf("EMPTY\n");
        return;
    }
    else if (stack->top + 1 < idx){
        printf("WRONG NUM\n");
        return;
    }
    Stack temp;
    init_stack(&temp);
    while (stack->top + 1 > idx){
        push(&temp, pop(stack));
    }
    replace(stack, item);
    while (is_empty(&temp) == 0){
        push(stack, pop(&temp));
    }
}



int main(){
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    init_stack(stack);
    printf("+: push data to stack\n ex) +a +b\n");
    printf("-: pop data from stack\n");
    printf("=: replace data of top of stack\n ex) =u\n");
    printf("T: print top of stack\n");
    printf("F: is full?\n");
    printf("E: is empty?\n");
    printf("?: is member?\n ex) ?k\n");
    printf("#: count data\n");
    printf("P: peek data\n");
    printf("num: pop data 'num' times\n");
    printf("L: print stack\n");
    printf("H: how many pops to get data?\n ex) Ha Hb\n");
    printf("M: minimize stack\n ex) M2 M3\n");
    printf("R: replace data by index\n ex) R3a R4b\n");
    printf("Q: quit\n");
    while (1){
        printf("COMMAND: ");
        char command[20];
        gets(command);
        if (command[0] == 'Q')
            break;
        for (int i = 0; command[i] != '\0'; i++){
            if (command[i] == '+'){
                push(stack, command[i+1]);
                i++;
            }
            else if (command[i] == '-'){
                printf("%c RETURNED\n", pop(stack));
            }
            else if (command[i] == '='){
                replace(stack, command[i+1]);
                i++;
            }
            else if (command[i] == 'T'){
                top_stack(stack);
            }
            else if (command[i] == 'P'){
                if (peek(stack) == 0)
                    printf("EMPTY\n");
                else
                    printf("%c\n", peek(stack));
            }
            else if (command[i] == 'F'){
                if (is_full(stack))
                    printf("TRUE\n");
                else
                    printf("FALSE\n");
            }
            else if (command[i] == 'E'){
                if (is_empty(stack))
                    printf("TRUE\n");
                else
                    printf("FALSE\n");
            }
            else if (command[i] == '?'){
                if (is_member(stack, command[i+1]) == -1)
                    printf("EMPTY\n");
                else if (is_member(stack, command[i+1]))
                    printf("TRUE\n");
                else
                    printf("FALSE\n");
                i++;
            }
            else if (command[i] == '#'){
                printf("%d\n", element_count(stack));
            }
            else if (command[i] > '0' && command[i] <= '9'){
                int num = command[i] - 48;
                while (num > 0){
                    pop(stack);
                    num--;
                }
            }
            else if (command[i] == 'L'){
                print_stack(stack);
            }
            else if (command[i] == 'H'){
                if (howmanypops(stack, command[i+1]) == -1){
                    printf("EMPTY\n");
                }
                else if (howmanypops(stack, command[i+1]) == -2){
                    printf("NO DATA\n");
                }
                else{
                    printf("YOU NEED %d TIMES OF POP\n", howmanypops(stack, command[i+1]));
                }
                i++;
            }
            else if (command[i] == 'M'){
                minimize(stack, command[i+1] - 48);
                i++;
            }
            else if (command[i] == 'R'){
                int idx = command[i+1] - 48;
                replace_by_index(stack, command[i+2], idx);
                i += 2;
            }
            else if (command[i] == 'C'){
                clear_stack(stack);
            }
        }
    }
    free(stack);
    return 0;
}