#include<stdio.h>
#include<string.h>
void reverse(char arr[]){
    int len = strlen(arr);
    for(int i=0; i<len/2; i++){
        char temp = arr[i];
        arr[i] = arr[len-i-1];
        arr[len-i-1] = temp;
    }
}
int main(int argc, char* argv[]) {
    char a[10002] = {0};
    char b[10002] = {0};
    char result[10003] = {0};
    char temp[10002] = {0};
    int carry = 0, len = 0;

    scanf("%s %s", a, b);

    reverse(a);
    reverse(b);

    if(strlen(a) > strlen(b)) len = strlen(a);
    else len = strlen(b);

    for(int i=0;i<len;i++){
        int sum = a[i]-'0' + b[i]-'0' + carry;
        if(sum<0)
            sum += '0';
        if(sum>9)
            carry = 1;
        else
            carry = 0;
        result[i] = sum % 10 + '0';
    }
    if(carry == 1)
        result[len] = '1';
    
    reverse(result);
    printf("%s",result);
    return 0;
}