#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    
    
    while (argc != 2) 
    {
        printf("Incorrect number of arguments!");
        return 1;
    } 
    
    int key = atoi(argv[1]); string s; int length;
    
    
    if (isdigit(key) != 0)
    {
        printf("Not a number!");
        return 1;
    }
    
   
    s = GetString();
    length = strlen(s);
    
    for (int i = 0; i<length; i++)
    {
        if (isalpha(s[i]))
        {
            if (isupper(s[i]))
            {
                int newcharnum = (int) s[i];
                newcharnum -= 65;
                newcharnum = (newcharnum + key) % 26;
                newcharnum += 65;
                printf("%c", (char) newcharnum);
            }
            else 
            {
                int newcharnum = (int) s[i];
                newcharnum -= 97;
                newcharnum = (newcharnum + key) % 26;
                newcharnum += 97;
                printf("%c", (char) newcharnum);
            
             }
        }
        else 
        {
            printf("%c",s[i]);
        }
    }
    printf("\n");
    return 0;
}
