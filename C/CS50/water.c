#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("How long in minutes do you spend showering?\n");
    int minutes = GetInt();
    printf("Calculating...\n");
    int waterUsed = minutes*1.5*128;
    printf("Do you know you use %i gallons ounces of water when you shower?\n", waterUsed);
    int bottles = waterUsed/16;
    printf("You use %i bottles of water for each shower!\n", bottles);
}
