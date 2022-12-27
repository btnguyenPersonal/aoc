#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    int c;
    char *input = argv[1];
    char temp;
    FILE *f;

    f = fopen(input, "r");

    int score = 0;
    /*
        R = +1 A
        P = +2 B
        S = +3 C
    */
    /*
        loss = +0 = X
        draw = +3 = Y
        win  = +6 = Z
    */
    char opponent;
    char you;

    while (fscanf(f, "%c%c", &opponent, &temp) > 0) {
        fscanf(f, "%c%c", &you, &temp);
        switch (opponent) {
            case 'A':
                if (you == 'Y') { // rock tie rock
                    score += 3 + 1;
                } else if (you == 'Z') { // paper beat rock
                    score += 6 + 2;
                } else if (you == 'X') { // scissors lose rock
                    score += 0 + 3;
                }
                break;
            case 'B':
                if (you == 'X') { // rock lose paper
                    score += 0 + 1;
                } else if (you == 'Y') { // paper tie paper
                    score += 3 + 2;
                } else if (you == 'Z') { // scissors beat paper
                    score += 6 + 3;
                }
                break;
            case 'C':
                if (you == 'Z') { // rock lose scissors
                    score += 6 + 1;
                } else if (you == 'X') { // paper lose scissors 
                    score += 0 + 2;
                } else if (you == 'Y') { // scissors tie scissors
                    score += 3 + 3;
                }
                break;
        }
        printf("%c ", opponent);
        printf("%c\n", you);
        printf("score: %d\n", score);
    }

    // while (fscanf(f, "%c%c", &opponent, &temp) > 0) {
    //     fscanf(f, "%c%c", &you, &temp);
    //     switch (opponent) {
    //         case 'A':
    //             if (you == 'X') { // rock tie rock
    //                 score += 3 + 1;
    //             } else if (you == 'Y') { // paper beat rock
    //                 score += 6 + 2;
    //             } else { // scissors lose rock
    //                 score += 0 + 3;
    //             }
    //             break;
    //         case 'B':
    //             if (you == 'X') { // rock lose paper
    //                 score += 0 + 1;
    //             } else if (you == 'Y') { // paper tie paper
    //                 score += 3 + 2;
    //             } else { // scissors beat paper
    //                 score += 6 + 3;
    //             }
    //             break;
    //         case 'C':
    //             if (you == 'X') { // rock lose scissors
    //                 score += 6 + 1;
    //             } else if (you == 'Y') { // paper lose scissors 
    //                 score += 0 + 2;
    //             } else { // scissors tie scissors
    //                 score += 3 + 3;
    //             }
    //             break;
    //     }
    //     printf("%c ", opponent);
    //     printf("%c\n", you);
    //     printf("score: %d\n", score);
    // }

    return 0;
    fclose(f);
}
