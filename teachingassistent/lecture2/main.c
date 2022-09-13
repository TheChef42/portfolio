#include <stdio.h>
#include <stdlib.h>

int main(void) {
    /*int m,n;
    scanf("%d %d ",&m,&n);
    int side1 = (m*m)-(n*n);
    int side2 = 2*m*n;
    int hypotenuse = m*m+n*n;
    printf("Side1: %d Side2: %d Hyp: %d",side1,side2,hypotenuse);


    *//* The variable groups is uninitialized */
   /* int classes = 2, groups = 1, students = 280;

    int average_pr_group = 0, average_pr_course = 0;

    average_pr_group = students / groups;
    average_pr_course = students / classes;

    printf("Classes: %d, Groups: %d, Students: %d \n", classes, groups, students);

    printf("There are %d students pr. group.\n", average_pr_group);
    printf("There are %d students pr. class.\n", average_pr_course);

    return EXIT_SUCCESS;
*/

    int c1, c2, c3, c4,   scanRes;

    printf("Enter input on the following line\n");

    scanRes = scanf("%c%c%c%c", &c1, &c2, &c3, &c4);

    printf("c1 = %c, c2 = %c, c3 = %c, c4 = %c\n", c1, c2, c3, c4);
    printf("scanRes = %d\n", scanRes);

    return 0;

}
