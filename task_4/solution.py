from typing import Iterable, Optional

from task_4.source_impl import Node, draw_tree


def build_tree_from_heap(heap: Iterable) -> Optional[Node]:
    arr = list(heap)
    if not arr:
        return None

    nodes: list[Optional[Node]] = [Node(v) if v else None for v in arr]

    for i, node in enumerate(nodes):
        if node is None:
            continue
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < len(nodes):
            node.left = nodes[li]
        if ri < len(nodes):
            node.right = nodes[ri]

    return nodes[0]


def visualize_heap(heap: Iterable) -> None:
    root = build_tree_from_heap(heap)
    if root is None:
        print("No data for visualization: heap is empty or root is missing.")
        return
    draw_tree(root)


if __name__ == "__main__":
    example_heap = [0, 4, 1, 5, 10, 7]
    visualize_heap(example_heap)
