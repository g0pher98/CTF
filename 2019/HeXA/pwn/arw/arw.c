// gcc -o arw arw.c -m32
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Initialize
    char buffer [32] = {0};
    unsigned long read_addr, write_addr, write_value;
    read_addr = 0;
    write_addr = 0;
    write_value = 0;

    // Arbitrary read
    printf("Where do you want to read? ");
    fgets(buffer, 32, stdin);
    read_addr = strtoul(buffer, NULL, 0);
    printf("%8x\n", *(int *)read_addr);       //leak 

    // Arbitrary write
    printf("Where do you want to write? ");
    fgets(buffer, 32, stdin);
    write_addr = strtoul(buffer, NULL, 0);

    printf("What do you want to write? ");
    fgets(buffer, 32, stdin);
    write_value = strtoul(buffer, NULL, 0);
    *(int *)write_addr = write_value;

    // Helper, GOT overwrite will be helpful :)
    puts("/bin/sh");
}
