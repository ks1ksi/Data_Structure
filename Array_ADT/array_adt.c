#include <stdio.h>
#include <string.h>
#define SIZE_OF_ARR 30 //�迭 ũ��
int currentpos = -1; //���� ��ġ (��������) �迭 ��������� -1

void insert_arr(char arr[], char data){ // current position ���� ����, current position + 1
    int size = strlen(arr);
    if (size == SIZE_OF_ARR - 1){
        printf("FULL\n");
        return;
    }
    if (currentpos == size - 1){
        currentpos++;
        arr[currentpos] = data;
    }
    else {
        for (int i = size; i > currentpos; i--){
            arr[i] = arr[i - 1];
        }
        currentpos++;
        arr[currentpos] = data;
    }
}

void delete_arr(char arr[]){ //current position�� �ִ� �ڷ� ����, current position�� �ڷᰡ ���ٸ� current position 0 or -1���� ����
    if (currentpos == -1){
        printf("EMPTY\n");
        return;
    }
    int size = strlen(arr);
    if (currentpos + 1 == size){
        arr[currentpos] = '\0';
        if (size == 1)
            currentpos = -1;
        else
            currentpos = 0;
    }
    else{
        for (int i = currentpos; i < size - 1; i++){
            arr[i] = arr[i+1];
        }
        arr[size - 1] = '\0';
    }
}

void traverse_front(char arr[]){ //current position ����������
    if (currentpos == -1){
        printf("EMPTY\n");
        return;
    }
    int size = strlen(arr);
    if (currentpos + 1 >= size)
        printf("ERROR\n");
    else
        currentpos++;
}

void traverse_rear(char arr[]){ //current position ��������
    if (currentpos == -1){
        printf("EMPTY\n");
        return;
    }    
    if (currentpos - 1 < 0)
        printf("ERROR\n");
    else
        currentpos--;
}

void goto_first(){ 
    currentpos = 0;
}

void goto_last(char arr[]){
    int size = strlen(arr);
    currentpos = size - 1;
}

char get_data(char arr[]){ //current position�� ��ġ�� �ڷ� ��ȯ
    printf("%c returned\n", arr[currentpos]);
    return arr[currentpos];
}

void replace(char arr[], char data){ //current position�� ��ġ�� �ڷḦ data�� ��ü
    arr[currentpos] = data;
}

void empty(char arr[]){ //�� �迭�� �����
    int size = strlen(arr);
    for (int i = 0; i < size; i++){
        arr[i] = '\0';
    }
    currentpos = -1;
}

void move(char arr[], int newpos){ //current position���� new position���� ��ĭ�� ������
    if (currentpos == newpos || newpos >= strlen(arr)
    || newpos < 0)
        return;

    char temp;

    if (currentpos > newpos){
        for (int i = currentpos; i > newpos; i--){
            temp = arr[i - 1];
            arr[i - 1] = arr[i];
            arr[i] = temp;
        }
    }
    else{
        for (int i = currentpos; i < newpos; i++){
            temp = arr[i + 1];
            arr[i + 1] = arr[i];
            arr[i] = temp;
        }
    }
    currentpos = newpos;
}

void print_array(char arr[]){ //�迭�� ���ִ� �ڷ�, current position, Size ���
    if (currentpos == -1){
        printf("EMPTY\n");
        return;
    }
    else{
        int size = strlen(arr);
        for (int i = 0; i < size; i++){
            printf("%c ", arr[i]);
        }
        puts("");
        printf("Current Position: %c\n", arr[currentpos]);
    }
}

void reverse(char arr[]){ //�迭 ������
    char temp;
    int size = strlen(arr);
    for (int i = 0; i < (size / 2); i++){
        temp = arr[i];
        arr[i] = arr[size -1 - i];
        arr[size - 1 - i] = temp;
    }
}

void makehalf(char arr[]){ //�迭 ������ ���̱�
    int size = strlen(arr);
    for (int i = 0; i < size / 2; i++){
        delete_arr(arr);
    }
}

void deleteindex(char arr[], int index){ //�ε��� ���� �Է��Ͽ� �ڷ� �����
    int temp = currentpos;
    currentpos = index;
    delete_arr(arr);
    if (temp > index)
        currentpos = 0;
    else
        currentpos = temp;
}


int main(){
    char arr[SIZE_OF_ARR] = {0};
    printf("+: insert data \n ex) +a +b\n");
    printf("<: go to first data\n");
    printf(">: go to last data\n");
    printf("-: delete data\n");
    printf("N: go to next data\n");
    printf("P: go to previous data\n");
    printf("@: return data\n");
    printf("=: replace data\n ex) =u\n");
    printf("R: reverse array\n");
    printf("H: make array half\n");
    printf("D: delete data by index\n ex) D1\n");
    printf("E: clear array\n");
    printf("M: move data\n ex) MP MN Mn M3\n");
    printf("L: print data\n");
    printf("Q: exit\n");

    while (1){
        char command[21] = {0};
        printf("COMMAND: ");
        gets(command);
        if (command[0] == 'Q'){ // Q �Է½� ����
            printf("EXIT");
            break;
        }
        for (int i = 0; i < strlen(command); i++){
            if (command[i] == '+'){
                insert_arr(arr, command[i+1]);
                i++;
            }
            else if (command[i] == '<')
                goto_first();
            else if (command[i] == '>')
                goto_last(arr);
            else if (command[i] == '-')
                delete_arr(arr);
            else if (command[i] == 'N')
                traverse_front(arr);
            else if (command[i] == 'P')
                traverse_rear(arr);
            else if (command[i] == '@')
                get_data(arr);
            else if (command[i] == 'R')
                reverse(arr);
            else if (command[i] == 'H')
                makehalf(arr);
            else if (command[i] == 'D'){
                deleteindex(arr, command[i+1] - 48);
                i++;
            }
            else if (command[i] == '='){
                replace(arr, command[i+1]);
                i++;
            }
            else if (command[i] == 'E')
                empty(arr);
            else if (command[i] == 'M'){
                if (command[i+1] == 'P'){
                    move(arr, currentpos - 1);
                    i++;
                }
                else if (command[i+1] == 'N'){
                    move(arr, currentpos + 1);
                    i++;
                }
                else if (command[i+1] == 'n'){
                    move(arr, strlen(arr) - 1);
                    i++;
                }
                else{
                    move(arr, command[i+1] - 48);
                    i++;
                }
            }
            else if (command[i] == 'L')
                print_array(arr);
        }
    }
    return 0;
}