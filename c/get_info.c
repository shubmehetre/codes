#include <stdio.h>
#include "get_info.h"

int getInfo(){

    char name[20];
    int age;
    printf("What is your name and age?  ");
    scanf("%s", name);
    scanf("%d", &age);
    if (age >= 18){
        printf("Hello, %s! Have a seat", name);
    }else{
        printf("GET OUT!");
    }
}

