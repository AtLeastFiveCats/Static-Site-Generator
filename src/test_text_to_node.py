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

    def test_italic_to_node(self):
        input_text = "This is __italic__"
        expected_nodes = [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC)
                ]
        new_nodes = markdown_to_textnode(input_text)
        self.assertListEqual(expected_nodes, new_nodes)

    def test_code_to_node(self):
        input_text = "This is ```codeword```"
        expected_nodes = [
                TextNode("This is ", TextType.TEXT),
                TextNode("codeword", TextType.CODE)
                ]
        new_nodes = markdown_to_textnode(input_text)
        self.assertListEqual(expected_nodes, new_nodes)

    def test_image_to_node(self):
        input_text = "This is an ![image](https://image.com)"
        expected_nodes = [
                TextNode("This is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.com")
                ]
        new_nodes = markdown_to_textnode(input_text)
        self.assertListEqual(expected_nodes, new_nodes)

    def test_link_to_node(self):
        input_text = "This is a [link](https://link.com)"
        expected_nodes = [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.com")
                ]
        new_nodes = markdown_to_textnode(input_text)
        self.assertListEqual(expected_nodes, new_nodes)

    def test_multiple_node(self):
        input_text = "This has both **bold** and ```code``` in it"
        expected_nodes = [
                TextNode("This has both ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" in it", TextType.TEXT)
                ]
        new_nodes = markdown_to_textnode(input_text)
        self.assertListEqual(expected_nodes, new_nodes)

