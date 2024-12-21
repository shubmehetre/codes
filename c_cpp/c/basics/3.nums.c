/*Learning about ints */
#include <stdio.h>

int main() {

  int x, y;
  printf("Enter two number: ");

  //%anything is call a format string
  scanf("%d %d", &x, &y);

  printf("The 2 numbers you entered were %d and %d\n", x, y);

  return 0;
}
