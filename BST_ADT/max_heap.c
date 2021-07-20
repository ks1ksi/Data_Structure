#include <stdio.h>
#include <stdlib.h>
#define MAX_ELEMENT 200
typedef struct _element
{
    int key; //우선순위
} element;

typedef struct _HEAP
{
    element heap[MAX_ELEMENT];
    int heap_size;
} HEAP;

typedef struct Node {
	struct Node* left;
	struct Node* right;
	int data;
} NODE;

void init(HEAP *h){
    h->heap_size = 0;
}

void insert_heap(HEAP *h, element item){
    int i;
    i = ++(h->heap_size);
    while (i != 1)
    {
        if (item.key > h->heap[i/2].key)
        {
            h->heap[i] = h->heap[i/2];
            i /= 2;
        }
        else
            break;
    }
    h->heap[i] = item;
}

element delete_heap(HEAP *h){ // child, parent 변수 사용?
    element item, temp;
    item = h->heap[1];
    h->heap[1] = h->heap[(h->heap_size--)];
    int i = 1;
    while (i < h->heap_size)
    {
        if (h->heap[i*2].key > h->heap[i].key || h->heap[i*2+1].key > h->heap[i].key)
        {
            if (h->heap[i*2].key < h->heap[i*2+1].key)
            {
                temp = h->heap[i];
                h->heap[i] = h->heap[i*2+1];
                h->heap[i*2+1] = temp;
                i = i*2+1;
            }
            else
            {
                temp = h->heap[i];
                h->heap[i] = h->heap[i*2];
                h->heap[i*2] = temp;
                i = i*2;                
            }
        }
        else
            break;
    }
    return item; 
}

void init_node(NODE* node, int item) {
	node->left = NULL;
	node->right = NULL;
	node->data = item;
}

void insert_node(NODE** root, int item) {
	NODE* newnode = (NODE*)malloc(sizeof(NODE));
	init_node(newnode, item);

	if (*root == NULL) {
		*root = newnode;
		return;
	}
	NODE* cur = *root;
	NODE* parent = NULL;
	while (cur != NULL) {
		if (cur->data > item) {
			parent = cur;
			cur = cur->left;
		}
		else if (cur->data < item) {
			parent = cur;
			cur = cur->right;
		}
		else {
			printf("SAME DATA\n");
			return;
		}
	}
	if (parent->data > item)
		parent->left = newnode;
	else
		parent->right = newnode;
}


void print_tree(NODE* root) {
	if (root == NULL)
		return;
	if (root->right == NULL && root->left == NULL)
		return;
	printf("(");
	if (root->left != NULL)
		printf("%d", root->left->data);
	print_tree(root->left);
	printf(",");
	if (root->right != NULL)
		printf("%d", root->right->data);
	print_tree(root->right);
	printf(")");
}


int main(){

    HEAP h;
    NODE* root = NULL;
    init(&h);
    
    while (1){
        element e;
        printf("수치 입력: (종료는 음수)");
        scanf("%d", &e.key);
        if (e.key < 0)
            break;
        insert_heap(&h, e);
    }

    for(int i = 1; i <= h.heap_size; i++){
        printf("%d ", h.heap[i].key);
        insert_node(&root, h.heap[i].key);
    }
    printf("\n%d", root->data);
    print_tree(root);
    printf("\n");


    return 0;
}