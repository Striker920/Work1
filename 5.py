# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)
#
# arr = [7, 2, 1, 6, 8, 5, 3, 4]
# print(quicksort(arr))


# def partition(arr, left, right):
#     pivot = arr[right]
#     i = left
#     for j in range(left, right):
#         if arr[j] <= pivot:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#     arr[i], arr[right] = arr[right], arr[i]
#     return i
#
# def quickselect(arr, left, right, k):
#     if left == right:
#         return arr[left]
#     pivot_index = partition(arr, left, right)
#     if k == pivot_index:
#         return arr[k]
#     elif k < pivot_index:
#         return quickselect(arr, left, pivot_index - 1, k)
#     else:
#         return quickselect(arr, pivot_index + 1, right, k)
#
# def kth_largest(arr, k):
#     return quickselect(arr.copy(), 0, len(arr) - 1, len(arr) - k)
#
# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print(kth_largest(arr, k))


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def search_bst(root, target):
#     if not root:
#         return False
#     if root.val == target:
#         return True
#     elif target < root.val:
#         return search_bst(root.left, target)
#     else:
#         return search_bst(root.right, target)
#
# root = TreeNode(8)
# root.left = TreeNode(3)
# root.right = TreeNode(10)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(6)
# root.right.right = TreeNode(14)
#
# print(search_bst(root, 6))


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# def preorder(root):
#     if not root:
#         return []
#     return [root.val] + preorder(root.left) + preorder(root.right)
#
# def inorder(root):
#     if not root:
#         return []
#     return inorder(root.left) + [root.val] + inorder(root.right)
#
# def postorder(root):
#     if not root:
#         return []
#     return postorder(root.left) + postorder(root.right) + [root.val]
#
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)
#
# print(preorder(root))
# print(inorder(root))
# print(postorder(root))

# номер 5
# from collections import deque
#
# def shortest_path_bfs(graph, start, end):
#     if start == end:
#         return 0
#     visited = set([start])
#     queue = deque([(start, 0)])
#     while queue:
#         node, distance = queue.popleft()
#         for neighbor in graph.get(node, []):
#             if neighbor == end:
#                 return distance + 1
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append((neighbor, distance + 1))
#     return -1
#
# graph = {
#     'A': ['B', 'D'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['A', 'C']
# }
#
# print(shortest_path_bfs(graph, 'A', 'C'))


# номер 6
import heapq

def x_max_elements(arr, x):
    if x <= 0:
        return []
    if x >= len(arr):
        return sorted(arr, reverse=True)
    min_heap = []
    for num in arr:
        if len(min_heap) < x:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    return sorted(min_heap, reverse=True)

arr = [5, 1, 9, 3, 14, 7]
x = 3
print(x_max_elements(arr, x))