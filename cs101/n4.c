#include <stdio.h>
struct location{
float latitude;
float longitude;
char continent[10];
};
void main()
{
struct location *gps;
 scanf("%f",&(gps->latitude));
 scanf("%f",&(gps->longitude));
 scanf("%s",&(gps->continent));
 printf("%.4f\n%.4f\n",gps->latitude,gps->longitude);
 for(int i=0;i<14;i++){
    printf("%c",gps->continent[i]);
 }
}
