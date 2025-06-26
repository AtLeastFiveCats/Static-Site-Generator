import unittest
from textnode import TextNode
from textnode import TextType
from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def print_out_split_nodes(self):
        node1 = TextNode("This is ```test``` text", TextType.TEXT)
        new_node = split_nodes_delimiter(node1, "```", TextType.CODE)
        self.assertNotEqual(node1, new_node)
    
    def testing_text_nodes(self):
        node1 = TextNode("This is some text", TextType.TEXT)
        split_node = split_nodes_delimiter(node1, "**", TextType.TEXT)
        self.assertEqual(node1, split_node[0])

    def testing_code_nodes(self):
        node1 = TextNode("This is some ```code``` text", TextType.TEXT)
        split_node = split_nodes_delimiter(node1, "```", TextType.TEXT)
        self.assertEqual(TextNode("code", TextType.CODE, None), split_node[1])

    def testing_bold_nodes(self):
        node1 = TextNode("This is some **bold** text", TextType.TEXT)
        split_node = split_nodes_delimiter(node1, "**", TextType.TEXT)
        self.assertEqual(TextNode("bold", TextType.BOLD, None), split_node[1])

    def testing_italic_nodes(self):
        node1 = TextNode("This is some __italian__ text", TextType.TEXT)
        split_node = split_nodes_delimiter(node1, "__", TextType.TEXT)
        self.assertEqual(TextNode("italian", "__", TextType.ITALIC), split_node[1])

    def testing_incorrect_syntax(self):
        node1 = TextNode("This is some **incorrect syntax", TextType.TEXT)
        self.assertRaises("Invalid markdown, please use a closing delimiter", split_nodes_delimiter(node1, "**", TextType.TEXT))

