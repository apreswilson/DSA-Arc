#include <stdio.h>

int main() {
	int age = 43;
	int *ptr = &age;

	printf("%d", *ptr);
}
