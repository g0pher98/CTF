// gcc -o path_lecture path_lecture.c

#include <stdio.h>
#define LECTURE_LEN 4

const char* lecture_str[LECTURE_LEN] = {
"Let's start to learn about the PATH!",
"PATH contains a colon-separated list of directories in which your system looks for executable files.\n\
(e.g. '/usr/local/bin:/usr/sbin:/usr/bin')",

"When a regular command (e.g., ls, rc-update or ic|emerge) is interpreted by the shell (e.g., bash or zsh),\n\
the shell looks for an executable file with the same name as your command in the listed directories, and executes it.\n\
To run executables that are not listed in PATH, the absoute path to the executable must be given: /bin/ls.\n\n\
 - Source: https://wiki.archlinux.org/index.php/environment_variables",

"Here is an example for you.\n\n\
Let's assume the current PATH variable is '/usr/local/bin:/usr/sbin:/usr/bin'\n\
If you type 'ls', then shell looks for 'ls' executable file from the PATH variable.\n\
In this case, shell looks for '/usr/local/bin' first and if 'ls' does not exist in the directory,\n\
then shell try to search from next directory in the PATH (i.e. '/usr/sbin')\n\
If 'ls' exist in the directory, then stopping the search and execute it."
};

void get_enter(void);
void clear(void);

int main(void)
{
    int i;
    for(i=0; i<LECTURE_LEN; i++) {
        clear();
        printf("\n%s\n", lecture_str[i]);
        get_enter();
    }
}

void get_enter(void)
{
    printf("\nPress enter to continue...\n\n");
    char c = 0;
    while(c != '\n')
        c = getchar();
}

void clear(void)
{
    system("clear");
}
