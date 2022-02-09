# Linear Search Algorithm
# def linear_search(n, arr, x):
#     for i in range(n):
#         if arr[i] == x:
#             return "The number is present at {} index".format(i)
#     return "Not found"
#
#
# n = int(input())
# arr = list(map(int, input().split()))
# x = int(input())
# print(linear_search(n, arr, x))


#Binary Search
# def binary_search(arr,l,r,x):
#     if r >= l:
#         mid = l + (r-l) // 2
#         if arr[mid] == x:
#             return mid
#         elif x < arr[mid]:
#             return binary_search(arr, l, mid-1, x)
#         elif x > arr[mid]:
#             return binary_search(arr, mid+1, r, x)
#     else:
#         return -1
#
#
# arr = sorted(list(map(int, input().split())))
# r = len(arr)-1
# x = int(input())
# print(*arr)
# print(binary_search(arr, 0, r, x))

#Jumpsearch algorithm

# import math
#
# def jumpsearch(n, arr, x):
#     jump = math.sqrt(n)
#     prev = 0
#     while arr[int(jump)-1] < x:
#         prev = jump
#         jump += math.sqrt(n)
#         if prev >= n:
#             return -1
#     while arr[int(prev)] < x:
#         prev += 1
#         if prev == jump:
#             return -1
#     if arr[int(prev)] == x:
#         return prev
#     return -1
#
#
# arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
# x = 55
# n = len(arr)
#
# # Find the index of 'x' using Jump Search
# index = jumpsearch(n, arr, x)
#
# # Print the index where 'x' is located
# print("Number" , x, "is at index", "%.0f" % index)


#Interpolation Search
# def interpolationSearch(arr, lo, hi, x):
#     # Since array is sorted, an element present
#     # in array must be in range defined by corner
#     if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
#
#         # Probing the position with keeping
#         # uniform distribution in mind.
#         pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
#                     (x - arr[lo]))
#
#         # Condition of target found
#         if arr[pos] == x:
#             return pos
#
#         # If x is larger, x is in right subarray
#         if arr[pos] < x:
#             return interpolationSearch(arr, pos + 1,
#                                        hi, x)
#
#         # If x is smaller, x is in left subarray
#         if arr[pos] > x:
#             return interpolationSearch(arr, lo,
#                                        pos - 1, x)
#     return -1
#
#
# # Driver code
#
#
# # Array of items in which
# # search will be conducted
# arr = [10, 12, 13, 16, 18, 19, 20,
#        21, 22, 23, 24, 33, 35, 42, 47]
# n = len(arr)
#
# # Element to be searched
# x = 18
# index = interpolationSearch(arr, 0, n - 1, x)
#
# if index != -1:
#     print("Element found at index", index)
# else:
#     print("Element not found")
