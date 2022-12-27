#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    int c;
    char *input = argv[1];
    char temp;
    FILE *f;

    f = fopen(input, "r");

    int number = 0;
    int sum = 0;

    while (fscanf(f, "%d%c", &number, &temp) > 0) {
        sum += number;
        if (temp == '\n') {
            printf("%d\n", sum);
            sum = 0;
        }
    }

    fclose(f);
}