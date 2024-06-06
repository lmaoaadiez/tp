#include<stdio.h>
typedef struct{
int data;
struct entry *next;
}stack;
void push(stack **top, int a)
{
stack *tmp;
tmp=(stack*)malloc(sizeof(stack));
tmp->data=a;
tmp->next=*top;
*top=tmp;

}
