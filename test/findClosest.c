#include <stdlib.h>
#include <stdbool.h>

bool elementExists (int nums[], int size, int element) {
	for (int i = 0; i < size; i++) {
		if (nums[i] == element) {
			return true;
		}
	}
	return false;
}

int main() 
{
	int nums[] = {-4,-2,1,4,8};
	int size = sizeof(nums) / sizeof(nums[0]);
	int closest = nums[0];

	for (int i = 0; i < size; i++)
	{
		if (abs(nums[i]) < abs(closest)) 
		{
			closest = abs(nums[i]);
		}
	}

	if (closest < 0 && elementExists(nums, size, abs(closest))) {
		return abs(closest);
	} else {
		return closest;
	}
	

	return 0;
}
