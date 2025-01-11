/*
 * This program takes a decimal and replaces the odd digits with 6
*/
#include <stdio.h>

#define F fflush(stdout)

void using_reverse_logic(){
	int user_input, reminder;
	int answer = 0;
	printf("Enter a number: "); F;
	scanf("%d", &user_input);

	while (user_input>0){
		reminder = user_input % 10;

		if (reminder%2 == 1){
			reminder = 6;
		}
		answer = answer * 10 + reminder;

		user_input = user_input / 10;
	}

	// Reverse it now
	int true_ans = 0;
	while(answer > 0){

		true_ans = true_ans * 10 + answer%10;
		answer = answer /10;
	}

	printf("\nAnswer: %d\n", true_ans);



}

void using_inplace_substitution(){
	int user_input, reminder;
	int answer = 0;
	int place = 1;
	printf("Enter a number: "); F;
	scanf("%d", &user_input);

	while (user_input>0){
		reminder = user_input % 10;

		if (reminder%2 == 1){
			reminder = 6;
		}

		answer = answer + reminder * place;
		place *= 10;
		user_input = user_input / 10;
	}
	printf("\nAnswer: %d\n", answer);

}

int main() {

	// using_reverse_logic();

	using_inplace_substitution();

}
