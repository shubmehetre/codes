#include "support.h"
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

void how_to_play(){

	printf("\n# How to play:\n\
	1. Bet your amount\n\
	2. Choose a number between 1-6\n\
	3. Dice will roll...\n \
	4. If guess is correct 3x bet added in Balace\n ");
}


int dice_roll_logic(){
	printf("\nRolling Dice...\n");
	sleep(3);

	return (rand() % 6) + 1;

}
