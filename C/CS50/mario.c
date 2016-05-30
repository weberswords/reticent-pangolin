#include <stdio.h>
#include <cs50.h>

int main()
{   
    int n;
    do {
        printf("Height: ");
        n = GetInt();
    }while (n < 0 || n > 23);
    
    int wide = n + 1;
    int blocks = 2;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < wide - blocks; j++) {
            printf(" ");
        }
        for (int k = 0; k < blocks; k++) {
            printf("#");
        }
        blocks++;
        printf("\n");
    }
}    
 