from collections import deque
import time

from task_4.solution import build_tree_from_heap
from task_4.source_impl import draw_tree


def _hex(r, g, b):
    return f"#{r:02X}{g:02X}{b:02X}"


def _gradient(n):
    if n <= 0:
        return []
    if n == 1:
        return [_hex(10, 42, 107)]
    start = (10, 42, 107)   # dark blue
    end = (168, 199, 255)   # light blue
    res = []
    for i in range(n):
        t = i / (n - 1)
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        res.append(_hex(r, g, b))
    return res


def _count_nodes(root):
    if not root:
        return 0
    q = [root]
    seen = set()
    cnt = 0
    while q:
        n = q.pop()
        if not n or n.id in seen:
            continue
        seen.add(n.id)
        cnt += 1
        q.append(n.left)
        q.append(n.right)
    return cnt


def _visit_step(node, root, colors, idx, visited):
    # returns (processed_flag, new_idx)
    if not node or node.id in visited:
        return False, idx
    node.color = "#FF0000"  # highlight current node
    draw_tree(root)
    time.sleep(0.5)
    node.color = colors[idx]
    idx += 1
    visited.add(node.id)
    return True, idx


def visualize_dfs(heap):
    root = build_tree_from_heap(heap)
    if root is None:
        print("No data for visualization: heap is empty or root is missing.")
        return
    colors = _gradient(_count_nodes(root))
    idx = 0
    stack = [root]
    visited = set()
    while stack:
        node = stack.pop()
        processed, idx = _visit_step(node, root, colors, idx, visited)
        if not processed:
            continue
        # Push right child first so that left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def visualize_bfs(heap):
    root = build_tree_from_heap(heap)
    if root is None:
        print("No data for visualization: heap is empty or root is missing.")
        return
    colors = _gradient(_count_nodes(root))
    idx = 0
    q = deque([root])
    visited = set()
    while q:
        node = q.popleft()
        processed, idx = _visit_step(node, root, colors, idx, visited)
        if not processed:
            continue
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


if __name__ == "__main__":
    example_heap = [7, 3, 9, 1, 5, 8, 10, None, None, 2]
    print("DFS visualization...")
    visualize_dfs(example_heap)
    print("BFS visualization...")
    visualize_bfs(example_heap)
