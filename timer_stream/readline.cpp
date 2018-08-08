#include <string>
#include <iostream>
#include <stdio.h>
int main(){
  system("stty raw");
  char line[3];
  bool found = false;
  while(!found){
    line[0] = getchar();
    std::cout << line[0] << std::endl;
  }
  system("stty cooked");
  return 0;
}
