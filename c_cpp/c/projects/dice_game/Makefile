game: dice_game.o support.o
	gcc dice_game.o support.o -o game

dice_game.o: dice_game.c support.h
	gcc -c dice_game.c

support.o: support.c support.h
	gcc -c support.c

clean:
	rm *.o game
