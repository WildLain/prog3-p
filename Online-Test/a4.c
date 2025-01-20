#include <stdio.h>
#include <string.h>
#include <string.h>

void schwabify(char *input, char output[])
{
    char *p;
    strcpy(output, input);
    p = strchr(output, '.');
    while (p != NULL)
    {
        char temp[200];
        strncpy(temp, output, p - output);
        temp[p - output] = '\0';       
        strcat(temp, " ,woisch?");
        strcat(temp, p +1);
        strcpy(output, temp);
        p = strchr(output, '.');
    }

    p = strstr(output, "halt");
    while (p != NULL)
    {
        char temp[200];
        strncpy(temp, output, p - output);
        temp[p - output] = '\0';             
        strcat(temp, "heb");
        strcat(temp, p + strlen("halt"));
        strcpy(output, temp);
        p = strstr(output, "halt");
    }
    p = strstr(output, "ist");
    while (p != NULL)
    {
        char temp[200];
        strncpy(temp, output, p - output);
        temp[p - output] = '\0';
        strcat(temp, "isch");
        strcat(temp, p + strlen("ist"));
        strcpy(output, temp);
        p = strstr(output, "ist");
    }
    printf("%s\n", output);
}

int main()
{
    char output[200] = "";
    schwabify("Das ist interessant.", output);
    schwabify("Mit  diesem Kleber   sollte es halten, oder?", output);
    schwabify("haltisthalt. isthaltist...", output);
    return 0;
}