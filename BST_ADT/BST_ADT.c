#include <stdio.h>
#include <stdlib.h>

typedef int element;

typedef struct Node {
	struct Node* left;
	struct Node* right;
	element data;
} NODE;

void init_node(NODE* node, element item);
void insert_node(NODE** root, element item);
NODE* search_node(NODE* root, element item);
void inorder(NODE* root); //need \n
void RRL(NODE* root); // \n
void print_tree(NODE* root); //cant print root node data, need \n
NODE* get_min(NODE* root);
NODE* get_max(NODE* root);
int count_node(NODE* root);
int height(NODE* root); 
int node_status(NODE* node);
void delete_node(NODE** root, element item);
void clear(NODE* root); //need to set root pointer to NULL
int string_to_int(char str[], int* idx);

int main() {
	NODE* root = NULL;
    char command[30];
    printf("+: insert node\n ex) +23\n");
    printf("-: delete node\n ex) -36\n");
    printf("P: print tree\n");
    printf("I: inorder traversal\n");
    printf("R: right->root->left traversal\n");
    printf("M: get max\n");
    printf("m: get min\n");
    printf("F: find node\n ex) F23\n");
    printf("H: get tree's height\n");
    printf("#: count node\n");
    printf("r: get right child\n ex) r30\n");
    printf("l: get left child\n ex) l20\n");
    printf("C: clear tree\n");
	printf("Q: quit\n");

    while (1){
        printf("COMMAND: ");
        gets(command);
		if (command[0] == 'Q')
			break;
        for (int i = 0; command[i] != '\0'; i++){
            if (command[i] == '+'){
                i++;
                insert_node(&root, string_to_int(command, &i));
            }
            else if (command[i] == '-'){
                i++;
                delete_node(&root, string_to_int(command, &i));
            }
			else if (command[i] == 'P'){
				if (root == NULL){
					printf("NO DATA\n");
				}
				else{
					printf("%d", root->data);
					print_tree(root);
					printf("\n");
				}
			}
			else if (command[i] == 'I'){
				inorder(root);
				printf("\n");
			}
			else if (command[i] == 'R'){
				RRL(root);
				printf("\n");
			}
			else if (command[i] == 'M'){
				NODE* max = get_max(root);
				if (max == NULL){
					printf("ERROR\n");
				}
				else{
					printf("%d\n", max->data);
				}
			}
			else if (command[i] == 'm'){
				NODE* min = get_min(root);
				if (min == NULL){
					printf("ERROR\n");
				}
				else{
					printf("%d\n", min->data);
				}
			}
			else if (command[i] == 'F'){
				i++;
				NODE* node = search_node(root, string_to_int(command, &i));
				if (node == NULL){
					printf("NO DATA\n");
				}
				else{
					int data = node->data;
					NODE* cur = root;
					printf("ROOT ");
					while (data != cur->data){
						if (cur->data > data){
							printf("LEFT ");
							cur = cur->left;
						}
						else{
							printf("RIGHT ");
							cur = cur->right;
						}
					}
					printf("\n");
				}
			}
			else if (command[i] == 'H'){
				printf("%d\n", height(root));
			}
			else if (command[i] == '#'){
				printf("%d\n", count_node(root));
			}
			else if (command[i] == 'r'){
				i++;
				NODE* rightnode = search_node(root, string_to_int(command, &i));
				if (rightnode == NULL){
					printf("NULL\n");
				}
				else{
					rightnode = rightnode->right;
					printf("%d\n", rightnode->data);
				}
			}
			else if (command[i] == 'l'){
				i++;
				NODE* leftnode = search_node(root, string_to_int(command, &i));
				if (leftnode == NULL){
					printf("NULL\n");
				}
				else{
					leftnode = leftnode->left;
					printf("%d\n", leftnode->data);
				}
			}
			else if (command[i] == 'C'){
				clear(root);
				root = NULL;
			}
        }
    }
	return 0;
}



void init_node(NODE* node, element item) {
	node->left = NULL;
	node->right = NULL;
	node->data = item;
}

void insert_node(NODE** root, element item) {
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

NODE* search_node(NODE* root, element item) {
	NODE* cur = root;
	while (cur != NULL) {
		if (cur->data == item) {
			return cur;
		}
		else if (cur->data > item)
			cur = cur->left;
		else
			cur = cur->right;
	}

	return NULL;
}

NODE* search_parent_node(NODE* root, element item) {
	NODE* cur = root;
	NODE* parent = NULL;
	while (cur != NULL) {
		if (cur->data == item) {
			return parent;
		}
		else if (cur->data > item) {
			parent = cur;
			cur = cur->left;
		}
		else {
			parent = cur;
			cur = cur->right;
		}
	}
	return NULL;
}

void inorder(NODE* root) {
	if (root != NULL) {
		inorder(root->left);
		printf("%d ", root->data);
		inorder(root->right);
	}
}

void RRL(NODE* root) {
	if (root != NULL) {
		RRL(root->right);
		printf("%d ", root->data);
		RRL(root->left);
	}
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

NODE* get_min(NODE* root) {
	if (root == NULL)
		return NULL;
	NODE* cur = root;
	while (cur->left != NULL) {
		cur = cur->left;
	}
	return cur;
}

NODE* get_max(NODE* root) {
	if (root == NULL)
		return NULL;
	NODE* cur = root;
	while (cur->right != NULL) {
		cur = cur->right;
	}
	return cur;
}

int count_node(NODE* root) {
	if (root == NULL)
		return 0;
	return 1 + count_node(root->left) + count_node(root->right);
}

int height(NODE* root) {
	if (root == NULL)
		return 0;
	int left = height(root->left);
	int right = height(root->right);
	if (left > right)
		return left + 1;
	else
		return right + 1;
}

int node_status(NODE* node) {
	if (node == NULL)
		return -1;
	if (node->left == NULL && node->right == NULL)
		return 0;
	else if (node->right == NULL)
		return 1;
	else if (node->left == NULL)
		return 2;
	else
		return 3;
}

void delete_node(NODE** root, element item) {
	NODE* cur = search_node(*root, item);
	if (cur == NULL) {
		printf("NO DATA\n");
		return;
	}
	NODE* parent = search_parent_node(*root, item);
	NODE* successor;
	NODE* scparent;

	switch (node_status(cur))
	{
	case 0:
        if (cur == *root){
            free(*root);
            *root = NULL;
            return;
        }
		if (parent->left == cur)
			parent->left = NULL;
		else
			parent->right = NULL;
		free(cur);
		break;

	case 1: //left
        if (cur == *root){
            NODE* temp = *root;
            *root = (*root)->left;
            free(temp);
            return;
        }
		successor = cur->left;        
		if (parent->left == cur)
			parent->left = successor;
		else
			parent->right = successor;
		free(cur);
		break;

	case 2: //right;
        if (cur == *root){
            NODE* temp = *root;
            *root = (*root)->right;
            free(temp);
            return;
        }
		successor = cur->right;
		if (parent->left == cur)
			parent->left = successor;
		else
			parent->right = successor;
		free(cur);
		break;

	case 3: //left & right
		successor = cur->right;
		scparent = NULL;
		while (successor->left != NULL) {
			scparent = successor;
			successor = successor->left;
		}
		if (successor->right == NULL) {
			if (scparent == NULL) {
				cur->data = successor->data;
				cur->right = NULL;
				free(successor);
			}
			else {
				cur->data = successor->data;
				scparent->left = NULL;
				free(successor);
			}
		}
		else {
			if (scparent == NULL) {
				cur->data = successor->data;
				cur->right = successor->right;
				free(successor);
			}
			else {
				cur->data = successor->data;
				scparent->left = successor->right;
				free(successor);
			}
		}
		break;
	}
}

void clear (NODE* root){
    if (root != NULL){
        clear(root->left);
        clear(root->right);
        free(root);
    }
    return;
}

int string_to_int(char str[], int* idx){
    int x = 0;

    while (str[*idx] >= '0' && str[*idx] <= '9'){
        x *= 10;
        x += str[*idx] - 48;
        (*idx)++;
    }
    (*idx)--;
    return x;
}