#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>


int main(void) 
{
    string fullname = GetString();
    
    if (fullname != NULL)
    {
        printf("%c", fullname[0]);
        for (int i = 0, n = strlen(fullname); i < n; i++)
        {
            if (isspace(fullname[i]))
            {
                printf("%c", toupper(fullname[i+1]));
            }
            else
            {
                continue;
            }    
        }
    printf("\n");
    }
}
   
