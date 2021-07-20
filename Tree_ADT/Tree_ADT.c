#include <stdio.h>
#include <stdlib.h>
typedef char element;
typedef struct Node{
    element data;
    struct Node *left;
    struct Node *right;
} NODE;

void init_node(NODE* node);
void insert_child(NODE *parent, element item);
void insert_sibling(NODE *node, element item);
void print_tree(NODE *node1, NODE *node2);
NODE* search_node(NODE *root, element item);
NODE* get_parent_bt(NODE *root, NODE *node); //이진트리로 변환했을 때 부모 노드
NODE* get_parent(NODE *root, NODE *node); //진짜 부모 노드
int is_leftchild(NODE *parent, NODE* node);
int is_rightchild(NODE *parent, NODE* node);
void get_child(NODE *parent);
void get_sibling(NODE* root, NODE* node);
int level_of_node(NODE* root, NODE* node);
void level_of_tree(NODE* root, NODE* node, int* level);
void delete_node(NODE* root, NODE* node);
void get_ancestors(NODE* root, NODE* node);
void get_descendants(NODE* node);
int degree_of_node(NODE* node);
void degree_of_tree(NODE* root, int* degree);
int count(NODE* root);
NODE* copy_tree(NODE* root);
NODE* join_trees(NODE* newroot, NODE* root1, NODE* root2);
void clear(NODE** root, NODE* node); //후위순회로 node free
int count_child(NODE* node);

int main(){
    NODE* roots[10];
    int idx = -1;
    int len = 0;
    int is_binary = 0;
    printf("+^: make root node\n ex) +^A\n");
    printf("+: insert child node\n ex) +A(BCD)\n");
    printf("-: delete node\n ex) -B\n");
    printf("=: insert sibling\n ex) =B(IJ)\n");
    printf("P: get parent\n ex) P(B)\n");
    printf("C: get child\n");
    printf("S: get sibling\n");
    printf("A: get ancestors\n");
    printf("D: get descendants\n");
    printf("L: level of tree / L(node): level of node\n");
    printf("G: degree of tree / G(node): degree of node\n");
    printf("#: count node of tree / #(node): count child of node\n");
    printf("J: join trees with new node\n ex) J(PAB)\n");
    printf("K: clear tree\n");
    printf("M: move tree index\n ex) M0 M2\n");
    printf("T: print current tree\n");
    printf("R: print root nodes and index\n");
    printf("Q: QUIT\n");
    printf("DONT INPUT SPACE BETWEEN NODES / '(' AND ')' CANNOT BE DATA OF NODE\n");
    printf("WANT BINARY TREE? (YES: 1 / NO: 0) >> ");
    scanf("%d", &is_binary);
    getchar();
    while (1){
        char command[30];
        printf("COMMAND: ");
        gets(command);
        if (command[0] == 'Q'){
            for(int i = 0; i < len; i++){
                clear(&roots[i], roots[i]);
            }
            break;
        }
        for (int i = 0; command[i] != '\0'; i++){
            if (command[i] == '+'){
                if (command[i+1] == '^'){
                    NODE* root = (NODE*)malloc(sizeof(NODE));
                    init_node(root);
                    root->data = command[i+2];
                    idx = len;
                    roots[idx] = root;
                    len++;
                    i += 2;
                }
                else if (command[i+2] == '('){
                    NODE* node = search_node(roots[idx], command[i+1]);
                    if (node == NULL){
                        printf("%c IS NOT MEMBER OF TREE %d\n", command[i+1], idx);
                    }
                    else{
                        i += 3;
                        while (command[i] != ')'){
                            if (is_binary && count_child(node) == 2){
                                printf("ERROR (MORE THAN TWO CHILD NODES)\n");
                                break;
                            }
                            insert_child(node, command[i]);
                            i++;
                        }
                    }
                    while (command[i] != ')')
                        i++;
                }
            }
            else if (command[i] == 'T'){
                if (idx == -1){
                    printf("NO TREE\n");
                }
                else{
                    print_tree(roots[idx], roots[idx]);
                }
            }
            else if (command[i] == '-'){
                NODE* node = search_node(roots[idx], command[i+1]);
                if (node == NULL){
                    printf("%c IS NOT MEMBER OF TREE %d\n", command[i+1], idx);
                }
                else{
                    delete_node(roots[idx], node);
                }
                i++;
            }
            else if (command[i] == '='){
                NODE* node = search_node(roots[idx], command[i+1]);
                if (node == NULL){
                    printf("%c IS NOT MEMBER OF TREE %d\n", command[i+1], idx);
                }
                else{
                    i += 3;
                    while (command[i] != ')'){
                        if (is_binary == 1 && count_child(get_parent(roots[idx], node)) == 2){
                            printf("ERROR (MORE THAN TWO CHILD NODES\n");
                            break;
                        }
                        insert_sibling(node, command[i]);
                        i++;
                    }
                }
                while (command[i] != ')')
                    i++;
            }
            else if (command[i] == 'P'){
                NODE* parent = get_parent(roots[idx], search_node(roots[idx], command[i+2]));
                if (parent == NULL){
                    printf("ERROR\n");
                }
                else{
                    printf("%c\n", parent->data);
                }
                i += 3;
            }
            else if (command[i] == 'C'){
                if (search_node(roots[idx], command[i+2]) == NULL){
                    printf("%c IS NOT MEMBER OF TREE %d\n", command[i+2], idx);
                }
                else
                    get_child(search_node(roots[idx], command[i+2]));
                i += 3;
            }
            else if (command[i] == 'S'){
                NODE* node = search_node(roots[idx], command[i+2]);

                if (node == NULL){
                    printf("%c IS NOT MEMBER OF TREE %d\n", command[i+2], idx);
                }
                else{
                    get_sibling(roots[idx], node);
                }
                i += 3;
            }
            else if (command[i] == 'A'){
                NODE* node = search_node(roots[idx], command[i+2]);
                
                if (node == NULL){
                    printf("%c IS NOT MEMBER OF TREE %d\n", command[i+2], idx);
                }
                else{
                    get_ancestors(roots[idx], node);
                }
                i += 3;
            }
            else if (command[i] == 'D'){
                NODE* node = search_node(roots[idx], command[i+2]);

                if (node == NULL){
                    printf("%c IS NOT MEMBER OF TREE %d\n", command[i+2], idx);
                }
                else{
                    get_descendants(node);
                }
                i += 3;
            }
            else if (command[i] == 'L'){
                if (command[i+1] == '('){
                    NODE *node = search_node(roots[idx], command[i+2]);
                    if (node == NULL){
                        printf("%c IS NOT MEMBER OF TREE %d\n", command[i+2], idx);
                    }
                    else{
                        printf("LEVEL OF NODE %c IS %d\n", command[i+2], level_of_node(roots[idx], node));
                    }
                    i += 3;
                }
                else{
                    int level = 0;
                    level_of_tree(roots[idx], roots[idx], &level);
                    printf("LEVEL OF TREE %d is %d\n", idx, level);
                }
            }
            else if (command[i] == 'G'){
                if (command[i+1] == '('){
                    NODE* node = search_node(roots[idx], command[i+2]);
                    if (node == NULL){
                        printf("%c IS NOT MEMBER OF TREE %d\n", command[i+2], idx);
                    }
                    else{
                        printf("DEGREE OF NODE %c is %d\n", command[i+2], degree_of_node(node));
                    }
                    i += 3;
                }
                else{
                    int degree = 0;
                    degree_of_tree(roots[idx], &degree);
                    printf("DEGREE OF TREE %d is %d\n", idx, degree);
                }
            }
            else if (command[i] == '#'){
                if (command[i+1] == '('){
                    NODE* node = search_node(roots[idx], command[i+2]);
                    if (node == NULL){
                        printf("%c IS NOT MEMBER OF TREE %d\n", command[i+2], idx);
                    }
                    else{
                        printf("NODE %c HAS %d CHILD NODE\n", command[i+2], count_child(node));
                    }
                    i += 3;
                }
                else{
                    printf("TREE %d HAS %d NODE\n", idx, count(roots[idx]));
                }
            }
            else if (command[i] == 'J'){
                int idx1 = -1;
                int idx2 = -1;
                for(int j = 0; j < len; j++){
                    if (roots[j]->data == command[i+3])
                        idx1 = j;
                    else if (roots[j]->data == command[i+4])
                        idx2 = j;
                }
                if (idx1 == -1 || idx2 == -1){
                    printf("ERROR\n");
                }
                else{
                    idx = len;
                    NODE* newroot = (NODE*)malloc(sizeof(NODE));
                    init_node(newroot);
                    newroot->data = command[i+2];
                    roots[idx] = join_trees(newroot, roots[idx1], roots[idx2]);
                    len++;
                }
                i += 5;
            }
            else if (command[i] == 'K'){
                if (idx == -1){
                    printf("NO TREE\n");
                }
                else{
                    clear(&roots[idx], roots[idx]);
                    for (int j = idx; j < len; j++){
                        roots[j] = roots[j + 1];
                    }
                    len--;
                    if (len == idx){
                        idx--;
                    }
                }    
            }
            else if (command[i] == 'M'){
                if (command[i+1] >= '0' && command[i+1] <= '9'){
                    idx = command[i+1] - 48;
                }
                else{
                    printf("WRONG INDEX\n");
                }
                i++;
            }
            else if (command[i] == 'R'){
                if (idx == -1){
                    printf("NO TREE\n");
                }
                else{
                    for(int i = 0; i < len; i++){
                        printf("ROOT OF TREE %d: %c\n", i, roots[i]->data);
                    }
                    printf("CURRENT INDEX: %d\n", idx);
                }
            }
        }
    }
    return 0;
}

void init_node(NODE* node){
    if (node == NULL){
        return;
    }
    node->left = NULL;
    node->right = NULL;
}

void insert_child(NODE *parent, element item){
    NODE * node = (NODE*)malloc(sizeof(NODE));
    node->right = NULL;
    node->left = NULL;
    node->data = item;

    if (parent->left == NULL){
        parent->left = node;
        return;
    }
    else{
        NODE * cur = parent->left;
        while (cur->right != NULL){
            cur = cur->right;
        }
        cur->right = node;
    }
}

void insert_sibling(NODE *sib, element item){
    NODE * node = (NODE*)malloc(sizeof(NODE));
    node->right = NULL;
    node->left = NULL;
    node->data = item;
    NODE *cur = sib;
    while (cur->right != NULL){
        cur = cur->right;
    }
    cur->right = node;
}

void print_tree(NODE *node1, NODE *node2){
    NODE *cur = node2->left;
    if (node1 == node2){
        printf("%c", node1->data);
    }
    if (node1->left == NULL){
        printf("\n");
        return;
    }
    printf("(");
    while (cur != NULL){
        printf("%c", cur->data);
        if (cur->left != NULL)
            print_tree(node1, cur);
        if (cur->right != NULL)
            printf(",");
        cur = cur->right;   
    }
    printf(")");
    if (node1 == node2){
        printf("\n");
    }
}

NODE* search_node(NODE* root, element item){
    if (root == NULL)
        return NULL;
    if (root->data == item)
        return root;

    NODE *cur;
    cur = search_node(root->left, item);
    if (cur != NULL)
        return cur;
    cur = search_node(root->right, item);
    if (cur != NULL)
        return cur;
    return NULL;
}   

NODE* get_parent_bt(NODE *root, NODE *node){
    if (root == NULL)
        return NULL;
    if (root->left == node || root->right == node)
        return root;
    NODE *cur;
    cur = get_parent_bt(root->left, node);
    if (cur != NULL)
        return cur;
    cur = get_parent_bt(root->right, node);
    if (cur != NULL)
        return cur;
    return NULL;
}

int is_leftchild(NODE* parent, NODE* node){
    if (parent->left == node)
        return 1;
    else
        return 0;
}

int is_rightchild(NODE* parent, NODE* node){
    if (parent->right == node)
        return 1;
    else 
        return 0;
}

NODE* get_parent(NODE* root, NODE* node){
    if (get_parent_bt(root, node) == NULL)
        return NULL;
    NODE *cur = node;
    while (!is_leftchild(get_parent_bt(root, cur), cur)){
        cur = get_parent_bt(root, cur);
    }
    return get_parent_bt(root, cur);
}

void get_child(NODE* parent){

    if (parent->left == NULL){
        printf("NO CHILD\n");
        return;
    }
    NODE* cur = parent->left;
    while (cur != NULL){
        printf("%c ", cur->data);
        cur = cur->right;
    }
    printf("\n");
}

void get_sibling(NODE* root, NODE* node){
    NODE* cur = get_parent(root, node);
    if (cur == NULL){
        printf("%c IS ROOT NODE\n", node->data);
        return;
    }
    cur = cur->left;
    while (cur != NULL){
        if (cur->data != node->data)
            printf("%c ", cur->data);
        cur = cur->right;
    }
    printf("\n");
}

int level_of_node(NODE* root, NODE* node){
    int level = 0;
    NODE* cur = node;
    while (cur != root){
        cur = get_parent(root, cur);
        level++;
    }
    return level;
}

void level_of_tree(NODE* root, NODE* node, int* level){
    if (node != NULL){
        level_of_tree(root, node->left, level);
        level_of_tree(root, node->right, level);
        if (level_of_node(root, node) > *level)
            *level = level_of_node(root, node);
    }
    return;
}

void delete_node(NODE* root, NODE *node){
    if (node->left != NULL){
        printf("%c IS PARENT NODE. CANT DELETE.\n", node->data);
        return;
    }

    NODE* parent = get_parent_bt(root, node);
    if (node->right == NULL){ //변환이진트리에서 단말노드인 경우
        if(is_leftchild(parent, node)){
            parent->left = NULL;
        }
        else{
            parent->right = NULL;
        }
        free(node);
    }
    else{ //변환이진트리에서 단말노드가 아닌 경우
        NODE *child = node->right;
        if (is_leftchild(parent, node)){
            parent->left = child;
        }
        else{
            parent->right = child;
        }
        free(node);
    }
}

void get_ancestors(NODE* root, NODE* node){
    if (root == node){
        printf("NO ANCESTORS\n");
        return;
    }
    NODE* cur = node;
    while (cur != root){
        cur = get_parent(root, cur);
        printf("%c ", cur->data);
    }
    printf("\n");
}

void get_descendants(NODE* node){
    element temp = node->data;
    node->data = 8; //백스페이스
    print_tree(node, node);
    node->data = temp;
}

int degree_of_node(NODE* node){
    int degree = 0;
    NODE* cur = node->left;
    while (cur != NULL){
        degree++;
        cur = cur->right;
    }
    return degree;
}

void degree_of_tree(NODE* root, int* degree){
    if (root != NULL){
        degree_of_tree(root->left, degree);
        degree_of_tree(root->right, degree);
        if (degree_of_node(root) > *degree){
            *degree = degree_of_node(root);
        }
    }
    return;
}

int count(NODE* root){
    if (root != NULL){
        return 1 + count(root->left) + count(root->right);
    }
    return 0;
}

NODE* copy_tree(NODE* root){
    if (root != NULL){
        NODE* node = (NODE*)malloc(sizeof(NODE));
        node->data = root->data;
        node->left = copy_tree(root->left);
        node->right = copy_tree(root->right);
        return node;
    }
    return NULL;
}

NODE* join_trees(NODE* newroot, NODE* root1, NODE* root2){
    NODE* node1 = copy_tree(root1);
    NODE* node2 = copy_tree(root2);
    newroot->left = node1;
    node1->right = node2;
    return newroot;
}

void clear(NODE** root, NODE* node){ 
    if (node != NULL){
        clear(root, node->left);
        clear(root, node->right);
        free(node);
    }
    return;
} //have to set root node (0, NULL, NULL)

int count_child(NODE* node){
    if (node == NULL)
        return -1;
    else if (node->left == NULL)
        return 0;
    else{
        int num = 0;
        NODE* cur = node->left;
        while (cur != NULL){
            cur = cur->right;
            num++;
        }
        return num;
    }
}