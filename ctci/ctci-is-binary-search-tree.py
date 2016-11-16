#!/usr/bin/env python3

import math
import unittest


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def balanced(tree):
    if tree is None:
        return True, math.inf, -1*math.inf

    if tree.left is None and tree.right is None:
        return True, tree.data, tree.data

    is_left_balanced, left_tree_min, left_tree_max = balanced(tree.left)
    if not is_left_balanced or tree.data <= left_tree_max:
        return False, None, None

    is_right_balanced, right_tree_min, right_tree_max = balanced(tree.right)
    if not is_right_balanced or tree.data >= right_tree_min:
        return False, None, None

    return True, min(tree.data, left_tree_min), max(tree.data, right_tree_max)


def check_binary_search_tree_(tree):
    is_balanced, tree_min, tree_max = balanced(tree)
    return is_balanced


class TestNode(unittest.TestCase):
    def test_null_is_balanced(self):
        is_balanced, tree_min, tree_max = balanced(None)
        self.assertTrue(is_balanced)

    def test_leaf_is_balanced(self):
        is_balanced, tree_min, tree_max = balanced(Node(data=42))
        self.assertTrue(is_balanced)
        self.assertEqual(tree_min, 42)
        self.assertEqual(tree_min, 42)

    def test_binary_is_balanced(self):
        tree = Node(data=2, left=Node(data=1))
        is_balanced, tree_min, tree_max = balanced(tree)
        self.assertTrue(is_balanced)
        self.assertEqual(tree_min, 1)
        self.assertEqual(tree_max, 2)

        tree = Node(data=2, right=Node(data=3))
        is_balanced, tree_min, tree_max = balanced(tree)
        self.assertTrue(is_balanced)
        self.assertEqual(tree_min, 2)
        self.assertEqual(tree_max, 3)

    def test_binary_is_unbalanced(self):
        tree = Node(data=2, left=Node(data=3))
        is_balanced, tree_min, tree_max = balanced(tree)
        self.assertFalse(is_balanced)

        tree = Node(data=2, right=Node(data=1))
        is_balanced, tree_min, tree_max = balanced(tree)
        self.assertFalse(is_balanced)

    def test_complete(self):
        left = Node(data=2, left=Node(data=1), right=Node(data=3))
        right = Node(data=6, left=Node(data=5), right=Node(data=7))
        tree = Node(data=4, left=left, right=right)
        is_balanced, tree_min, tree_max = balanced(tree)
        self.assertTrue(is_balanced)
        self.assertEqual(tree_min, 1)
        self.assertEqual(tree_max, 7)


if __name__ == '__main__':
    unittest.main()
