#include <stdio.h>
#include <math.h>
#include <cs50.h>

int main()
{   
    float c; int m; int q = 25; int d = 10; int n = 5;
    do {
        printf("How much change is owed? ");
        c = GetFloat();
            
    }while (c < 0);
    
    c=roundf(c*100);
    m = c;

    int i = 0;
    while (m>=q) {
    //quarters
        i += m/q;
        m = m % q;
    }
    
    while (m>=d) {
    //dimes
        i +=m/d;
        m = m%d;
    }
    
    while (m>=n) {
    //nickels
        i += m/n;
        m = m%n;
    }
    //pennies
    i+=m;
    printf("%i\n", i);
}
