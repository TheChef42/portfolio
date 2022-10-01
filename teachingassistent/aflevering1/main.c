#include <stdio.h>

int main() {
    int input, uger, dage, timer, minutter, sekunder, rest;

    scanf("%d",&input);

    uger = input / 604800;
    rest = input % 604800;
    dage = rest / 86400;
    rest = rest % 86400;
    timer = rest / 3600;
    rest = rest % 3600;
    minutter = rest / 60;
    rest = rest % 60;
    sekunder = rest;

    printf("%d sekunder svarer til: %d uge/r, %d dag/e, %d time/r, %d minutte/r, %d sekund/er\n",input,uger,dage,timer,minutter,sekunder);
    return 0;
}
