#include<stdio.h>
// #define MAX 10
void your_1d_array(){
    float arr[]={1.2,3.09,3.4,5};
    for (int i = 0; i < 4; i++){
        printf("Element %d is: %f with address %d\n",i,arr[i],&arr[i]);
    }
    

}
int main(){
    your_1d_array();
    return 0;
}