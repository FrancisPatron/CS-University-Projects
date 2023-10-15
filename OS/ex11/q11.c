#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
    char command[300];
    strcpy(command, "wget -q https://www.c-programming-simple-steps.com/support-files/return-statement.zip");
    system(command);
    strcpy(command, "ls | grep return");
    system(command);
    return 0;
}