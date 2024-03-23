#include<stdio.h>

typedef struct 
{
    char name;
    float physics,chemistry,maths;    
}  student;


int main(){
    int limit = 2;
    student arr[limit];
    
    for (int i = 0; i < limit; i++)
    {
        printf("Student %d name: ",i);
        scanf("%c",arr[i].name);

        printf("Student %d Physics marks: ",i);
        scanf("%f",arr[i].physics);

        printf("Student %d Chemistry marks: ",i);
        scanf("%f",arr[i].chemistry);

        printf("Student %d Maths marks: ",i);
        scanf("%f",arr[i].maths);

    }

    for (int i = 0; i < limit; i++)
    {
        printf("Student %d name: %c\n",i, arr[i].name);
        printf("Student %d Physics marks: %f\n",i, arr[i].physics);
        printf("Student %d Chemistry marks: %f\n",i,arr[i].chemistry);
        printf("Student %d Maths marks: %f\n",i, arr[i].maths);
    }
    
    





}