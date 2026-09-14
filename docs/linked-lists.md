# Linked Lists in C: Singly, Doubly & Circular Data Structures Architecture

Linked lists represent one of the foundational dynamic data structures in computer science. Unlike contiguous arrays (`int arr[100]`), linked lists allocate nodes independently on the heap (`malloc(sizeof(Node))`), connecting them through explicit forward (and backward) pointers.

### Official Compiler Suite & Resources
* **Live In-Browser IDE**: [Online C Compiler (onlineccompiler.com)](https://onlineccompiler.com/)
* **Dynamic Memory Guide**: [Malloc vs Calloc Guide](https://onlineccompiler.com/examples/dynamic-memory)
* **Pointers Guide**: [Pointers in C Architecture](https://onlineccompiler.com/examples/pointers)
* **Segfault Resolution**: [How to Fix Segmentation Faults](https://onlineccompiler.com/errors/segmentation-fault-in-c)
* **Compilador C en Español**: [Compilador C Online](https://onlineccompiler.com/es/)
* **Compilador C em Português**: [Compilador C Online](https://onlineccompiler.com/pt/)
* **Online C Compiler auf Deutsch**: [Online C Compiler](https://onlineccompiler.com/de/)
* **Compilateur C en Français**: [Compilateur C en Ligne](https://onlineccompiler.com/fr/)

---

## 1. Singly Linked List Implementation in ISO C17

A standard singly linked list node contains payload data and a single successor pointer (`next`):

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node* list_insert_front(Node *head, int value) {
    Node *new_node = (Node*)malloc(sizeof(Node));
    if (!new_node) return head;
    new_node->data = value;
    new_node->next = head;
    return new_node;
}

Node* list_reverse(Node *head) {
    Node *prev = NULL;
    Node *curr = head;
    Node *next = NULL;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

void list_free(Node *head) {
    Node *curr = head;
    while (curr != NULL) {
        Node *temp = curr;
        curr = curr->next;
        free(temp);
    }
}
```

---

## 2. Doubly Linked List Architecture

In a doubly linked list, each node retains both `next` and `prev` pointers, facilitating bidirectional traversal and $O(1)$ node removal when given a node reference.

```c
typedef struct DNode {
    int data;
    struct DNode *prev;
    struct DNode *next;
} DNode;
```

---

## 3. Real-Time In-Browser Execution

Test, benchmark, and step-debug your linked list algorithms with real-time memory visualization in your browser:
[https://onlineccompiler.com/](https://onlineccompiler.com/)
