from text_to_nodes import markdown_to_textnode
from textnode import TextNode
from textnode import TextType
import unittest

class Testtexttonode(unittest.TestCase):
    def test_text_to_node(self):
        input_text = "This is text without any markdown"
        expected_node = [TextNode(input_text, TextType.TEXT)]
        new_nodes = markdown_to_textnode(input_text)
        self.assertEqual(expected_node, new_nodes)

    def test_bold_text_to_node(self):
        input_text = "This is **bold** text"
        expected_nodes = [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
                ]
        new_nodes = markdown_to_textnode(input_text)
        self.assertListEqual(expected_nodes, new_nodes)
