#include <stddef.h>


int add(int n, int k){
  return n+k;
}

int fill_array(char* arr, char x, size_t len) {
  while(len--){
    *arr++ = x;
  }
}

int square(int n){
  return n*n;
}
