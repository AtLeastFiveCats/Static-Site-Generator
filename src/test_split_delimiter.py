import unittest
from textnode import TextNode
from textnode import TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def print_out_split_nodes(self):
        node1 = TextNode("This is ```test``` text", TextType.TEXT)
        new_node = split_nodes_delimiter([node1], "```", TextType.CODE)
        self.assertNotEqual(node1, new_node)
    
    def testing_text_nodes(self):
        node1 = TextNode("This is some text", TextType.TEXT)
        split_node = split_nodes_delimiter([node1], "**", TextType.TEXT)
        self.assertEqual(node1, split_node[0])

    def testing_code_nodes(self):
        node1 = TextNode("This is some ```code``` text", TextType.TEXT)
        node2 = TextNode("This is some ", TextType.TEXT)
        node3 = TextNode("code", TextType.CODE)
        node4 = TextNode(" text", TextType.TEXT)
        split_node = split_nodes_delimiter([node1], "```", TextType.TEXT)
        self.assertListEqual(
                [
                    node2,
                    node3,
                    node4
                    ],
                split_node
                )

    def testing_bold_nodes(self):
        node1 = TextNode("This is some **bold** text", TextType.TEXT)
        split_node = split_nodes_delimiter([node1], "**", TextType.TEXT)
        self.assertListEqual(
                [
                    TextNode("This is some ", TextType.TEXT),
                    TextNode("bold", TextType.BOLD),
                    TextNode(" text", TextType.TEXT)
                    ],
                split_node
                )

    def testing_italic_nodes(self):
        node1 = TextNode("This is some __italian__ text", TextType.TEXT)
        split_node = split_nodes_delimiter([node1], "__", TextType.TEXT)
        self.assertListEqual(
                [
                    TextNode("This is some ", TextType.TEXT),
                    TextNode("italian", TextType.ITALIC),
                    TextNode(" text", TextType.TEXT)
                    ],
                split_node
                )

    def testing_incorrect_syntax(self):
        node1 = TextNode("This is some **incorrect syntax", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, node1, "**", TextType.TEXT)

