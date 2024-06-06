#include<stdio.h>
int add(int x,int y){
    int s;
    s=x+y;
    return;
}
void main(){
    int a,b,sum=1;
    a=5;b=7;
    sum=add(a,b);
    printf("%d",sum);

}