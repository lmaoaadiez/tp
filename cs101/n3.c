#include <stdio.h>
int mult(int x, int y)
{
int m;
m = x * y;
return (y,m,x);
}
void main()
{
int a,b, prod=0;
a=-3; b=6;
prod = mult(a,b);
printf("Prod = %d", prod);
}
