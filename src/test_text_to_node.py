from text_to_nodes import markdown_to_textnode
from textnode import TextNode
from textnode import TextType
import unittest

class Testtexttonode(unittest.TestCase):
    def test_text_to_node(self):
        node = TextNode("This is text without any markdown.", TextType.TEXT)
        new_nodes = markdown_to_textnode(node)
        self.assertListEqual(
                [
                    node
                    ],
                new_nodes
                )
