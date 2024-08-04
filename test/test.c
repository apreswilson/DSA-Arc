#include <stdio.h>

int main()
{
	int myNums[] = {10, 20, 30, 40, 50};
	int length = sizeof(myNums) / sizeof(myNums[0]);
	int searchForElement = 30;

	int start = 0;
	int end = length - 1;

	while (start <= end)
	{
		int mid = start + (end - start) / 2; // Calculate the middle index

		if (myNums[mid] == searchForElement)
		{
			printf("Element %d found at index %d\n", myNums[mid], mid);
		}

		if (myNums[mid] < searchForElement)
		{
			start = mid + 1;
		}
		else
		{
			end = mid - 1;
		}
	}

	return 0;
}