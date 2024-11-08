def slidewindow(arr, k):
   current_window_sum = sum(arr[:k])
   max_sum = current_window_sum
   print(current_window_sum)
   for i in range (len(arr) - k):
      current_window_sum = current_window_sum - arr[i] + arr[i + k]
      print(current_window_sum)
      max_sum = max(current_window_sum, max_sum)
   print(max_sum)

def main():
   inputarray = [1, 4, 2, 10, 23, 3, 1, 0, 20]
   k = 4
   slidewindow(inputarray, k)

if __name__ == "__main__":
   main()