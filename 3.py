# # # # def p(s: str):
# # # #     matching = {')': '(', '}': '{', ']': '['}
# # # #     stack = []
# # # #
# # # #     for char in s:
# # # #         if char == '(' or char == '{' or char == '[':
# # # #             stack.append(char)
# # # #         elif char == ')' or char == '}' or char == ']':
# # # #             if not stack:
# # # #                 return False
# # # #             top = stack.pop()
# # # #             if top != matching[char]:
# # # #                 return False
# # # #
# # # #     return len(stack) == 0
# # # #
# # # #
# # # # def run_tests():
# # # #     test_cases = [
# # # #         ("()[]{}", True),
# # # #         ("(]", False),
# # # #         ("([)]", False),
# # # #         ("{[]}", True),
# # # #         ("(", False),
# # # #         ("", True),
# # # #         ("([{}])", True)
# # # #     ]
# # # #
# # # #     for s, expected in test_cases:
# # # #         result = p(s)
# # # #         print(f"{s} {result} {expected})")
# # # #
# # # #
# # # # if __name__ == "__main__":
# # # #     run_tests()
# # #
# # #
# # # class Stack:
# # #     def __init__(self):
# # #         self._items = []
# # #
# # #     def push(self, x):
# # #         self._items.append(x)
# # #
# # #     def pop(self):
# # #         return self._items.pop()
# # #
# # #     def top(self):
# # #         return self._items[-1]
# # #
# # #     def is_empty(self):
# # #         return len(self._items) == 0
# # #
# # #
# # # def task2_stack_demo():
# # #     stack = Stack()
# # #
# # #     stack.push(5)
# # #     stack.push(10)
# # #     stack.push(15)
# # #
# # #     print(stack.top())
# # #     print(stack.pop())
# # #     print(stack.pop())
# # #     print(stack.is_empty())
# # #     print(stack.pop())
# # #     print(stack.is_empty())
# # #     return stack
# # # if __name__ == "__main__":
# # #     task2_stack_demo()
# # #
# # #
# # class Queue:
# #     def __init__(self):
# #         self._items = []
# #
# #     def enqueue(self, x):
# #         self._items.append(x)
# #
# #     def dequeue(self):
# #         return self._items.pop(0)
# #
# #     def front(self):
# #         return self._items[0]
# #
# #     def is_empty(self):
# #         return len(self._items) == 0
# #
# #
# # def task3_queue_demo():
# #     queue = Queue()
# #     queue.enqueue(1)
# #     queue.enqueue(2)
# #     queue.enqueue(3)
# #
# #     print(queue.front())
# #     print(queue.dequeue())
# #     print(queue.dequeue())
# #     print(queue.is_empty())
# #     print(queue.dequeue())
# #     print(queue.is_empty())
# #
# #     return queue
# #
# #
# # if __name__ == "__main__":
# #     task3_queue_demo()
#
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
#
# def bubble():
#     test_array = [5, 2, 9, 1, 5]
#     sorted_array = bubble_sort(test_array.copy())
#     print(sorted_array)
#     return sorted_array
#
#
# if __name__ == "__main__":
#     bubble()



def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def selection():
    test_array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(test_array.copy())
    print(sorted_array)
    return sorted_array


if __name__ == "__main__":
    selection()