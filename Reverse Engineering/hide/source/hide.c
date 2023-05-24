#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void print_flag(char *buffer)
{
    printf("%s", buffer);
}

int main()
{
    unsigned char *scr = "n1mdaCTF{";

    char buffer[100] = {0};
    char flag[] = "";
    int i;

    printf(*scr);

    signed char secret[] = "";

    print_flag(buffer);

    puts("f14gs_h4rdc0d3d_4r3_n0t_s4f3}");

    return 0;
}
