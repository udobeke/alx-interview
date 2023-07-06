#!/usr/bin/python3
"""Lockboxes challenge solution"""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked"""
    if not isinstance(boxes, list) or not all(isinstance(item, list) for item in boxes):
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    def dfs(box: int) -> None:
        """Depth-first search algorithm"""
        visited[box] = True
        for key in boxes[box]:
            if not visited[key]:
                dfs(key)

    dfs(0)

    return all(visited)
