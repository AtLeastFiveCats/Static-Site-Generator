import unittest
from split_images_and_links import split_nodes_image
from split_images_and_links import split_nodes_links
from textnode import TextNode
from textnode import TextType

def test_split_images(self):
    node = TextNode("This is some text with a ![image](https://somelink.com)", TextType.TEXT)

    new_nodes = split_nodes_image(node)
    self.assertListEqual(
            [
                TextNode("This is some text with a ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://somelink.com")
                ]
            )
def test_split_images(self):
    node = TextNode('This is some text with a [link](https://someimage.com)', TextType.TEXT)

    new_nodes = split_nodes_links(node)
    self.assertListEqual(
            [
                TextNode("This is some text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://someimage.com")
                ]
            )

