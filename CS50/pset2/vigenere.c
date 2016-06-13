#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    
    //Check for keyword argument
    while (argc != 2) 
    {
        printf("Incorrect number of input\n");
        return 1;
    } 
    
    string key = argv[1]; 
    int length = strlen(key);
    int i; int k; int j; int m;  
    int count; int slen;
    string s;
    
    //Check keyword to make sure it's letters
    for (i = 0; i < length; i++)
    {
        if (isalpha(key[i]))
        {
            continue;
        }
        else 
        {
            printf("Not alpha\n");
            return 1;
        }
    }
   //Change keyword letters to ints
    int keyints[length];
    for (j = 0; j < length; j++)
    {
        if (isupper(key[j]))
        {
            keyints[j]=(int) key[j];
            keyints[j]-=65;
        }
        else
        {
            keyints[j]=(int) key[j];
            keyints[j]-=97;
        }
    }
    
    //Get message to cipher
    s = GetString();
    slen = strlen(s);
    
    //Iterate over string and encrypt
    for (k = 0, m = 0; k < slen; k++)
    {
        if (isalpha(s[k]))
        {
            count = m%length;
            if (isupper(s[k]))
            {
                int newcharnum = (int) s[k];
                newcharnum -= 65;
                newcharnum = (newcharnum + keyints[count]) % 26;
                newcharnum += 65;
                printf("%c", (char) newcharnum);
                m++;
            }
            else 
            {
                int newcharnum = (int) s[k];
                newcharnum -= 97;
                newcharnum = (newcharnum + keyints[count]) % 26;
                newcharnum += 97;
                printf("%c", (char) newcharnum);
                m++;
            
             }
        }
        else 
        {
            printf("%c",s[k]);
        }
    }
    printf("\n");
    return 0;
}
