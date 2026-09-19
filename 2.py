# номер 1

# def has_duplicates(arr):
#     seen = set()
#     for element in arr:
#         if element in seen:
#             return True
#         seen.add(element)
#     return False
# def main():
#     test_cases = [
#         ([1, 2, 3, 4, 5], False),
#         ([1, 2, 3, 4, 2], True),
#     ]
#     for i, (input_arr, expected) in enumerate(test_cases, 1):
#         result = has_duplicates(input_arr)
#         print(f"Входные данные{input_arr}")
#         print(f"Результат{result}")
#         print(f"Ожидалось{expected}")
#         print()
# if __name__ == "__main__":
#     main()

# номер 2
# def count_frequencies(arr):
#     freq = {}
#     for element in arr:
#         if element in freq:
#             freq[element] += 1
#         else:
#             freq[element] = 1
#     return freq
# def main():
#     test_cases = [
#         [1, 2, 2, 3, 3, 3],
#         [1, 1, 1, 1],
#         []
#     ]
#     for i, arr in enumerate(test_cases, 1):
#         result = count_frequencies(arr)
#         for key, value in result.items():
#             print(f" {key} {value}")
#         print()
# if __name__ == "__main__":
#     main()


# номер 3
# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
#     return -1
# def main():
#     test_cases = [
#         ([2, 7, 11, 15], 9, [0, 1]),
#         ([3, 2, 4], 6, [1, 2]),
#     ]
#     for i, (nums, target, expected) in enumerate(test_cases, 1):
#         result = two_sum(nums, target)
#         print(f"Массив {nums}")
#         print(f"Таргет {target}")
#         print(f"Результат {result}")
#         print(f"Ожидалось {expected}")
# if __name__ == "__main__":
#     main()

# номер 4
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def count_linked_list(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count
def main():
    test_cases = [
        ([5, 8, 12, 7], 4),
        ([], 0),
        ([1], 1),
    ]
    for i, (values, expected) in enumerate(test_cases, 1):
        if not values:
            head = None
        else:
            head = ListNode(values[0])
            current = head
            for val in values[1:]:
                current.next = ListNode(val)
                current = current.next
        result = count_linked_list(head)
        print(f"Список: {''.join(map(str, values)) if values else 'пусто'}")
        print(f"Результат{result}")
        print(f"Ожидалось{expected}")
        print()
if __name__ == "__main__":
    main()