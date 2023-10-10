
#include <stdio.h>
#define Z_ASCII 90

int main(int argc, const char * argv[]) {
    char str[]="FUDAN UNIVERSITY";
    int length=sizeof(str)/sizeof(str[0]);
    int i=0;
    for (i=0; i<length; i++) {
        if (str[i]==' '){
            printf(" ");
        }else if (str[i]+3<Z_ASCII){
            printf("%c",str[i]+3);
        }else{
            printf("%c",str[i]-23);
        }
    };
    printf("\n");
    return 0;
}
