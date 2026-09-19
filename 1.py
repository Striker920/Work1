# # номер 1
# def max_element(arr):
#     max_val = arr[0]
#     for num in arr:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# arr1 = [3, 7, 2, 9, 5]
# print(arr1)
# print(max_element(arr1))
#
# arr2 = [-10, -4, -32, -1]
# print(arr2)
# print(max_element(arr2))

# номер 2
# def max_sorted(arr):
#     if not arr:
#         return None
#     return arr[-1]
#
# arr1 = [1, 4, 6, 9, 15]
# print(arr1)
# print(max_sorted(arr1))
#
# arr2 = [11,42]
# print(arr2)
# print(max_sorted(arr2))

# номер 3
# def k_elements(arr, k):
#     if k <= 0:
#         return []
#
#     if k >= len(arr):
#         return arr[:]
#
#     arr_copy = arr[:]
#     n = len(arr_copy)
#     k_index = n - k
#
#     def partition(left, right):
#         pivot = arr_copy[right]
#         i = left
#
#         for j in range(left, right):
#             if arr_copy[j] <= pivot:
#                 arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
#                 i += 1
#
#         arr_copy[i], arr_copy[right] = arr_copy[right], arr_copy[i]
#         return i
#
#     def select(left, right, target_index):
#         if left == right:
#             return
#
#         pivot_index = partition(left, right)
#
#         if pivot_index == target_index:
#             return
#         elif pivot_index < target_index:
#             select(pivot_index + 1, right, target_index)
#         else:
#             select(left, pivot_index - 1, target_index)
#
#     select(0, n - 1, k_index)
#
#     return arr_copy[k_index:]
#
# arr1 = [5, 1, 9, 3, 14, 7]
# k1 = 3
# result1 = k_elements(arr1, k1)
# print(arr1)
# print(k1)
# print(result1)

# номер 4
# def get_unique_elements(arr):
#     if not arr:
#         return []
#
#     unique_dict = {}
#
#     for num in arr:
#         unique_dict[num] = True
#
#     return list(unique_dict.keys())
#
#
# arr1 = [1, 2, 2, 3, 4, 4, 5]
# result1 = get_unique_elements(arr1)
# print(arr1)
# print(result1)

# номер 5
# def unique_sort(arr):
#     if not arr:
#         return []
#
#     result = [arr[0]]
#
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i - 1]:
#             result.append(arr[i])
#
#     return result
#
# arr1 = [1, 1, 2, 2, 2, 3, 4, 4, 5]
# result1 = unique_sort(arr1)
# print(arr1)
# print(result1)

# номер 6
def bin_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr1 = [1, 3, 5, 7, 9, 11]
target1 = 7
result1 = bin_search(arr1, target1)
print(arr1)
print(result1)