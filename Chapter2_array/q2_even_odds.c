#include<stdio.h>
#define MAX 10
int print_numof_evens_odds(int * arr){
    int evens=0, odds=0;
    for (int i = 0; i < MAX; i++)
    {
        if (arr[i]%2==1){
            odds++;
        }
        else{
            evens++;
        }
    }    
    printf("Odds are: %d\nEvens are: %d\n",odds,evens);
    
}
int main(){
    int arr[]={1,2,3,4,5,6,7,8,9,0};
    print_numof_evens_odds(arr);
    return 0;
}