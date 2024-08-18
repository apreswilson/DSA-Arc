def waveSort(arr):
    for i in range(0, len(arr) - 1, 2):
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if i < len(arr)-1 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]


def main():
   arrayToSort = [10, 90, 49, 2, 1, 5, 23]
   waveSort(arrayToSort)
   print(arrayToSort)

if __name__ == "__main__":
   main()