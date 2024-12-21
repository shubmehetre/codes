#include <stdio.h>
#include <math.h> // Required for the pow() function

int main() {
    double principal, rate, time, compoundInterest, amount;
    int n;

    // Input: Principal amount, interest rate, time in years, and compounding frequency
    printf("Enter the principal amount: ");
    scanf("%lf", &principal);
    
    printf("Enter the annual interest rate (in percentage): ");
    scanf("%lf", &rate);
    
    printf("Enter the time (in years): ");
    scanf("%lf", &time);
    
    printf("Enter the number of times interest is compounded per year: ");
    scanf("%d", &n);

    // Convert interest rate from percentage to decimal
    rate = rate / 100;

    // Compound interest formula: A = P * (1 + r/n)^(n*t)
    amount = principal * pow((1 + rate / n), n * time);

    // Calculate compound interest
    compoundInterest = amount - principal;

    // Output the results
    printf("Future Value (Amount): %.2lf\n", amount);
    printf("Compound Interest: %.2lf\n", compoundInterest);

    return 0;
}

