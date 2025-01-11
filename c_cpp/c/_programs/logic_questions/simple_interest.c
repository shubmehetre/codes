#include<stdio.h>

int interestCalculator(int p,int n,int r){

    return (p*n*r)/100 ;

}

int main(){
    int principle, rate, time;

    printf("Enter Principle, Rate and time:\n");
    scanf("%d", &principle);
    scanf("%d", &rate);
    scanf("%d", &time);

    int interest = interestCalculator(principle, rate, time);

    printf("\nInterest is => %d\n", interest);
    
}
