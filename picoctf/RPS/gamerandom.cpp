#include <cstdlib>
#include <ctime>
#include <iostream>

const char *wins[3] = {"paper", "scissors", "rock"};

int main() {
  // Seed the random number generator
  srand(time(0));

  // Output the first three values of rand() % 3
  std::cout << wins[rand() % 3] << std::endl;

  return 0;
}
