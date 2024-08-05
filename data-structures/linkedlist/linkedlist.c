#include <stdio.h>
#include <stdlib.h>

struct myStructure {
	int myNum;
	char myLetter;
	char myString[30];
};


void testFun (int a) {
	printf("Value of pointer function %d", a);
}

int main() {
	int age = 43;
	int *ptr = &age;
	int **scndptr = &ptr;

	void (*fun_ptr)(int) = testFun;

	(*fun_ptr)(10);

	int myNums[4] = {1,2,3,4};

	printf("%d", *(myNums + 3));

	struct myStructure *s1 = NULL;
	
	//The first part is just a type cast, saying the type of s1 is the myStructure struct
	//Then the malloc allocates memory sufficient to hold the structure
	s1 = (struct myStructure*) malloc(sizeof(struct myStructure));

	s1->myNum = 20;

	printf("%d", s1->myNum);

	return 0;
}
