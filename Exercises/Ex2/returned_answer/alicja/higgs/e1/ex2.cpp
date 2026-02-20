#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

    if(argc <= 1){
        printf("You did not feed me arguments. I will die now... :/");
        exit(1);
    }

    int i = atoi(argv[1]);
    std::cout << "Hello world " << i << "\n";
    return(0);
}