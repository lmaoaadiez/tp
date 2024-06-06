#include<stdio.h>
int* foo(int*);
int main(){
    int a[5]={1,2,3,4,5};
    int b[5],*c;
    c=foo(a);
    

}
int *foo(int x[]){
    int i;
    for(i=0;i<5;i++){
        x[i]+=x[i];
        printf("%d ",x[i]);
    }
    return x;
}