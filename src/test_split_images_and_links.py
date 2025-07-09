import unittest
from split_images_and_links import split_nodes_image
from split_images_and_links import split_nodes_links
from textnode import TextNode
from textnode import TextType
class TestLeafNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode("This is some text with a ![image](https://somelink.com)", TextType.TEXT)

        new_nodes = split_nodes_image(node.text)
        self.assertListEqual(
                [
                    TextNode("This is some text with a ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://somelink.com")
                    ],
                new_nodes
                )
    def test_split_links(self):
        node = TextNode('This is some text with a [link](https://someimage.com)', TextType.TEXT)

        new_nodes = split_nodes_links(node.text)
        self.assertListEqual(
                [
                    TextNode("This is some text with a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://someimage.com")
                    ],
                new_nodes
                )

    def test_no_image(self):
        node = TextNode("text no ![url}", TextType.TEXT)

        new_nodes = split_nodes_image(node.text)
        self.assertListEqual(new_nodes, [node])

    def test_no_alt(self):
        node = TextNode("text no alt (https://noimage.com)", TextType.TEXT)

        new_nodes = split_nodes_image(node.text)
        self.assertListEqual(new_nodes, [node])

    def test_no_link(self):
        node = TextNode("text no [link]", TextType.TEXT)

        new_nodes = split_nodes_links(node.text)
        self.assertListEqual(new_nodes, [node])

    def test_no_link_alt(self):
        node = TextNode("text without (https://altless.com)", TextType.TEXT)

        new_nodes = split_nodes_links(node.text)
        self.assertListEqual(new_nodes, [node])

