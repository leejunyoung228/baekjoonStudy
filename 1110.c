#include <stdio.h>

int main(void) {
	int n = 0;
	scanf("%d", &n);
	int num = n;
	int c = 0;
    while(1) {
		num =  num % 10 *10+ (num / 10 + num % 10)%10;
		c++;
		if (num == n) {
			break;
		}
		
	}
	printf("%d\n", c);
	return 0;
}