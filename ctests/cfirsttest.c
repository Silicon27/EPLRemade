// make it so that the following code will compile to a shared library so a python script can call the function in it
/* REMINDER:
 * Editing this file in ANY way would require the regeneration of the shared libraries, so please make sure to generate them AFTER you're done editing*/


#include <stdio.h>

void firsttest() {
    printf("Hello from firsttest\n");
}

int add (int a, int b) {
    return a + b;
}

int main() {
    firsttest();
    printf("The sum of 3 and 4 is %d\n", add(3, 4));
    return 0;
}



// for windows use `gcc -shared -o cfirsttest.dll -fPIC cfirsttest.c`
// for linux use gcc -shared -o `UNIX/cfirsttest.so -fPIC ctests/cfirsttest.c`
// mac and linux use the same command to create the shared library