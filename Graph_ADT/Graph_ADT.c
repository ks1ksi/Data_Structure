#include <stdio.h>
#include <stdlib.h>

typedef char element;

typedef struct _edge{
    struct _vertex* linked_vertex;
    struct _edge* next;
} Edge;

typedef struct _vertex{
    element data;
    struct _vertex* next; //전체 verticies 확인용
    struct _edge* e_head; //vertex에 연결된 edge들로 인접 verticies찾기
    int visited;
} Vertex;

typedef struct _undirected_graph{
    int count;
    struct _vertex* v_head;
} Graph;

void init_graph(Graph* g);
Vertex* init_vertex(element item);
void insert_vertex(Graph* g, element item);
void insert_edge(Vertex* v1, Vertex* v2);
void print_graph(Graph* g); //\n
void delete_vertex(Graph* g, element item);
void delete_edge(Vertex* v1, Vertex* v2);
int degree_of_v(Vertex* v);
int is_connected(Graph* g);
int is_empty(Graph *g);
void adjacent(Vertex* v);
int path_exist(Vertex* v1, Vertex* v2);
int num_of_v(Graph* g);
int num_of_e(Graph* g);
void rename_v(Vertex* v, element item);
void clear(Graph* g);
Vertex* search_v(Graph* g, element item);
void reset_visited(Graph* g);




int main(){
    Graph g;
    init_graph(&g);
    char command[30];
    printf("+: insert vertex\n ex) +A +B\n");
    printf("E: insert edge\n ex) E(AB)\n");
    printf("-: delete vertex\n ex) -A -B\n");
    printf("D: delete edge\n ex) D(BC)\n");
    printf("L: print graph\n");
    printf("C: is connected?\n");
    printf("N: is empty?\n");
    printf("V: print degree of vertex\n ex) V(A)\n");
    printf("A: print adjacent vertex\n ex) A(B)\n");
    printf("P: path exist?\n ex) P(BC)\n");
    printf("X: count vertex\n");
    printf("H: count edge\n");
    printf("R: rename vertex\n ex) R(AF)\n");
    printf("K: clear\n");
    printf("Q: quit\n");
    
    while(1){
        printf("COMMAND: ");
        gets(command);
        if (command[0] == 'Q')
            break;
        for (int i = 0; command[i] != '\0'; i++){
            if (command[i] == '+'){
                insert_vertex(&g, command[i+1]);
                i++;
            }
            else if (command[i] == 'E'){
                Vertex* v1_e = search_v(&g, command[i+2]);
                Vertex* v2_e = search_v(&g, command[i+3]);
                if (v1_e == NULL || v2_e == NULL){
                    printf("NO DATA\n");
                }
                else{
                    insert_edge(v1_e, v2_e);
                }
                i += 4;
            }
            else if (command[i] == '-'){
                delete_vertex(&g, command[i+1]);
                i++;
            }
            else if (command[i] == 'D'){
                Vertex* v1_d = search_v(&g, command[i+2]);
                Vertex* v2_d = search_v(&g, command[i+3]);
                if (v1_d == NULL || v2_d == NULL){
                    printf("NO DATA\n");
                }
                else{
                    int tf = 0;
                    Edge* ecur = v1_d->e_head;
                    while (ecur != NULL){
                        if (ecur->linked_vertex == v2_d){
                            tf = 1;
                            break;
                        }
                        ecur = ecur->next;
                    }
                    if (tf = 0){
                        printf("NOT CONNECTED\n");
                    }
                    else{
                        delete_edge(v1_d, v2_d);
                    }
                }
                i += 4;
            }
            else if (command[i] == 'L'){
                print_graph(&g);
                printf("\n");
            }
            else if (command[i] == 'C'){
                if (is_connected(&g)){
                    printf("TRUE\n");
                }
                else{
                    printf("FALSE\n");
                }
            }
            else if (command[i] == 'N'){
                if (is_empty(&g)){
                    printf("TRUE\n");
                }
                else{
                    printf("FALSE\n");
                }
            }
            else if (command[i] == 'V'){
                Vertex* v_d = search_v(&g, command[i+2]);
                if (v_d == NULL){
                    printf("NO DATA\n");
                }
                else{
                    printf("%d\n", degree_of_v(v_d));
                }
                i += 3;
            }

            else if (command[i] == 'A'){
                Vertex* v_a = search_v(&g, command[i+2]);
                if (v_a == NULL){
                    printf("NO DATA\n");
                }
                else{
                    adjacent(v_a);
                }
                i += 3;
            }
            else if (command[i] == 'P'){
                Vertex* v1 = search_v(&g, command[i+2]);
                Vertex* v2 = search_v(&g, command[i+3]);
                if (v1 == NULL || v2 == NULL){
                    printf("NO DATA\n");
                }
                else{
                    if (path_exist(v1, v2)){
                        printf("TRUE\n");
                    }
                    else{
                        printf("FALSE\n");
                    }
                }
                i += 4;
                reset_visited(&g);
            }
            else if (command[i] == 'X'){
                printf("%d\n", num_of_v(&g));
            }
            else if (command[i] == 'H'){
                printf("%d\n", num_of_e(&g));
            }
            else if (command[i] == 'R'){
                Vertex* v = search_v(&g, command[i+2]);
                if (v == NULL){
                    printf("NO DATA\n");
                }
                else{
                    rename_v(v, command[i+3]);
                }
                i += 4;
            }
            else if (command[i] == 'K'){
                clear(&g);
            }
        }
    }

    return 0;
}

void init_graph(Graph* g){
    g->count = 0;
    g->v_head = NULL;
}

Vertex* init_vertex(element item){
    Vertex* v = (Vertex*)malloc(sizeof(Vertex));
    v->data = item;
    v->e_head = NULL;
    v->next = NULL;
    v->visited = 0;
    return v;
}

void insert_vertex(Graph* g, element item){
    Vertex* v = init_vertex(item);
    v->next = g->v_head;
    g->v_head = v;
    g->count++;
}

void insert_edge(Vertex* v1, Vertex* v2){ //무방향
    Edge* e1 = (Edge*)malloc(sizeof(Edge));
    Edge* e2 = (Edge*)malloc(sizeof(Edge));
    
    e1->linked_vertex = v1;
    e1->next = v2->e_head;
    v2->e_head = e1; //v2에 e1 연결, e1 따라가면 v1

    e2->linked_vertex = v2;
    e2->next = v1->e_head;
    v1->e_head = e2; //v1에 e2연결, e2 따라가면 v2
}


void print_graph(Graph* g){
    Vertex* vcur = g->v_head;
    Edge* ecur;
    while (vcur != NULL){
        printf("%c", vcur->data);
        if (vcur->e_head != NULL){
            ecur = vcur->e_head;
            printf("(");
            while (ecur != NULL){
                printf("%c", ecur->linked_vertex->data);
                ecur = ecur->next;
                if (ecur != NULL)
                    printf(",");
            }
            printf(")");
        }
        vcur = vcur->next;
        printf(" ");
    }
}

void delete_edge(Vertex* v1, Vertex* v2){
    Edge* ecur = v1->e_head;
    Edge* tmp;

    while (ecur != NULL){
        if (ecur->linked_vertex == v2){
            if (ecur == v1->e_head){
                v1->e_head = v1->e_head->next;
                free(ecur);
                break;
            }
            else{
                tmp->next = ecur->next;
                free(ecur);
                break;
            }
        }
        else{
            tmp = ecur;
            ecur = ecur->next;
        }
    }

    ecur = v2->e_head;

    while (ecur != NULL){
        if (ecur->linked_vertex == v1){
            if (ecur == v2->e_head){
                v2->e_head = v2->e_head->next;
                free(ecur);
                break;
            }
            else{
                tmp->next = ecur->next;
                free(ecur);
                break;
            }
        }
        else{
            tmp = ecur;
            ecur = ecur->next;
        }
    }
}


void delete_vertex(Graph* g, element item){
    Vertex* vcur = g->v_head;
    Vertex* tmp;
    while (vcur != NULL && vcur->data != item){
        tmp = vcur;
        vcur = vcur->next;
    }
    if (vcur == NULL){
        printf("NO DATA\n");
        return;
    }

    Edge* ecur = vcur->e_head;

    while (ecur != NULL){
        Edge* ncur = ecur->next;
        delete_edge(ecur->linked_vertex, vcur);
        ecur = ncur;
    }

    if (vcur == g->v_head){
        g->v_head = g->v_head->next;
        free(vcur);
    }
    else{
        tmp->next = vcur->next;
        free(vcur);
    }

    (g->count)--;
}

int degree_of_v(Vertex* v){
    int degree = 0;
    Edge* ecur = v->e_head;
    while (ecur != NULL){
        ecur = ecur->next;
        degree++;
    }
    return degree;
}



int is_connected(Graph* g){ 

    Vertex* vcur = g->v_head;
    Vertex* vc2;
    while (vcur != NULL){
        vc2 = vcur->next;
        while (vc2 != NULL){
            reset_visited(g);
            if (path_exist(vcur, vc2) == 0){
                return 0;
            }
            vc2 = vc2->next;
        }
        vcur = vcur->next;
    }
    return 1;
}




int is_empty(Graph* g){
    if (g->v_head == NULL)
        return 1;
    else
        return 0;
}

void adjacent(Vertex* v){
    if (v->e_head == NULL){
        printf("NO ADJACENT VERTEX\n");
        return;
    }
    Edge* ecur = v->e_head;

    while (ecur != NULL){
        printf("%c ", ecur->linked_vertex->data);
        ecur = ecur->next;
    }
    printf("\n");
}

int path_exist(Vertex* v1, Vertex* v2){
    if (v1 == v2)
        return 1;
    if (v1->visited == 1)
        return 0;
    Edge* ecur = v1->e_head;
    v1->visited = 1;
    while (ecur != NULL){
        if (path_exist(ecur->linked_vertex, v2)){
            return 1;
        }
        ecur = ecur->next;
    }
    return 0;
}

int num_of_v(Graph* g){
    return g->count;
}

int num_of_e(Graph* g){
    int num = 0;
    Vertex* vcur = g->v_head;
    if (vcur == NULL)
        return 0;

    while (vcur != NULL){
        Edge* ecur = vcur->e_head;
        while (ecur != NULL){
            num++;
            ecur = ecur->next;
        }
        vcur = vcur->next;
    }
    return (num / 2);
}

void rename_v(Vertex* v, element item){
    if (v == NULL)
        return;
    v->data = item;
}

void clear(Graph* g){
    Vertex* vcur = g->v_head;
    Vertex* temp;
    while (vcur != NULL){
        temp = vcur;
        vcur = vcur->next;
        delete_vertex(g, temp->data);
    }
}

Vertex* search_v(Graph* g, element item){
    Vertex* vcur = g->v_head;
    while (vcur != NULL){
        if (vcur->data == item)
            return vcur;
        else
            vcur = vcur->next;
    }
    return NULL;
}

void reset_visited(Graph* g){
    Vertex* vcur = g->v_head;
    while (vcur != NULL){
        vcur->visited = 0;
        vcur = vcur->next;
    }
}