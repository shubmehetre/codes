#include <stdio.h>
#include <unistd.h>

int main() {

  printf("Testing buffer not flushing");
  fflush(stdout);

  sleep(5);

}
