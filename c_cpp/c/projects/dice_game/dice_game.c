#include <stdio.h>
#include <string.h>
#include "support.h"
#include <stdlib.h>

int main(){

	int balance = 1000;
	int bet = 0;
	int guess = 0;
	int game_session = 0;
	char name[20];

	printf("Welcome to Dice Game! \n\nWhat is your Name: ");
	scanf("%s", name);
	printf("\nHello! %s... Merry Christmas to you.\nDo you want to play this Dice Game: ? (yes/no): ", name);

	char sesh[5];
	scanf("%s", sesh);

	if (!strcmp(sesh, "yes")){
		game_session = 1;
		how_to_play();
	}else{
		printf("\nOK then... Go Home!!\n");
	}

	while (game_session) {

		printf("\nYour Current Balance: %d\n", balance);

		printf("Enter BET amount: ");
		fflush(stdout);
		scanf("%d", &bet);

		printf("Guess the Number: ");
		fflush(stdout);
		scanf("%d", &guess);

		int roll_result = dice_roll_logic();
		printf("\nRoll result = %d", roll_result);
		if(roll_result == guess){
			balance = balance - bet;
			int winnings = bet  * 3;
			balance = balance + winnings;
			printf("\nRight Guess !!!\nYour Balance: %d", balance);
		}else {
			balance = balance - bet;
			printf("\nSorry, your guess was incorrect\nYour Balance: %d", balance);
		}

		if(balance <= 0){
			printf("\n\nBalance Over!! You Lose\n");
			break;
		}
		printf("\n\nDo you want to play AGAIN ? (yes/no): ");

		char sesh[5];
		scanf("%s", sesh);

		if (!strcmp(sesh, "yes")){
			game_session = 1;
			system("clear");
		}else{
			printf("\nOk! Your Final Balance is: %d\n", balance);
			break;
		}


	}
}
