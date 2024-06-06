#include<stdio.h>
int main(){
    int i=0;
    int *p =&i;
    printf("%d %d",p,p+1);
    
    }