#include<stdio.h>
#include<math.h>

float CompoundInterestCalc(int p, int r, int t, int f){
    return p * pow((1+(r/f)), f*t);
}
int main (){

    
    int principle, rate, time, freq;

    printf("Enter Principle, Rate freq within a year and time:\n");
    scanf("%d", &principle);
    scanf("%d", &rate);
    scanf("%d", &time);
    scanf("%d", &freq);

    float interest = CompoundInterestCalc(principle, rate, time, freq);

    printf("\nInterest is => %f\n", interest);

}
