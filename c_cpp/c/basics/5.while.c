/*Learning while loops
 *Print 1 to i
 * */
#include <stdio.h>

int main() {

  int i = 9;
  int start_point = i - i + 1;

  while (start_point <= i) {

    printf("%d\n", start_point);
    start_point++;
  }
  return 0;
}
