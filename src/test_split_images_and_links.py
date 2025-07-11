import unittest
from split_images_and_links import split_nodes_image
from split_images_and_links import split_nodes_links
from textnode import TextNode
from textnode import TextType
class TestSplitImagesLinks(unittest.TestCase):
    def test_split_images(self):
        node = TextNode("This is some text with a ![image](https://somelink.com)", TextType.TEXT)

        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("This is some text with a ", TextType.TEXT),
                    TextNode("image", TextType.IMAGE, "https://somelink.com")
                    ],
                new_nodes
                )
    def test_split_links(self):
        node = TextNode('This is some text with a [link](https://someimage.com)', TextType.TEXT)

        new_nodes = split_nodes_links([node])
        self.assertListEqual(
                [
                    TextNode("This is some text with a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://someimage.com")
                    ],
                new_nodes
                )

    def test_no_image(self):
        node = TextNode("text no ![url}", TextType.TEXT)

        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [node])

    def test_no_alt(self):
        node = TextNode("text no alt (https://noimage.com)", TextType.TEXT)

        new_nodes = split_nodes_image([node])
        self.assertListEqual(new_nodes, [node])

    def test_no_link(self):
        node = TextNode("text no [link]", TextType.TEXT)

        new_nodes = split_nodes_links([node])
        self.assertListEqual(new_nodes, [node])

    def test_no_link_alt(self):
        node = TextNode("text without (https://altless.com)", TextType.TEXT)

        new_nodes = split_nodes_links([node])
        self.assertListEqual(new_nodes, [node])

    def test_split_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_multiple_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
    )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,

        )

    def test_empty_test(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual([], new_nodes)

    def test_non_text_nodes(self):
        node = [
                TextNode("This is a link", TextType.LINK, "https://link.com"),
                TextNode("And this is code", TextType.CODE),
                ]
        new_nodes = split_nodes_image(node)
        self.assertListEqual(node, new_nodes)

    def link_at_start(self):
        node = TextNode("[green boi](https://loz.com) with the princess", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("green boi", TextType.LINK, "https://loz.com"),
                    TextNode(" with the princess", TextType.TEXT)
                    ],
                new_nodes
                )

    def image_at_start(self):
        node = TextNode("![green boi](https://loz.com) with the princess", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("green boi", TextType.IMAGE, "https://loz.com"),
                    TextNode(" with the princess", TextType.TEXT)
                    ],
                new_nodes
                )

    def image_at_end(self):
        node = TextNode("front text with ![red boi](https://peach.com)", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
                [
                    TextNode("front text with ", TextType.TEXT),
                    TextNode("red boi", TextType.IMAGE, "https://peach.com")
                    ],
                new_nodes
                )

    def link_at_end(self):
        node = TextNode("front text with a [green boi](https://loz.com)", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
                [
                    TextNode("front text with a ", TextType.TEXT),
                    TextNode("green boi", TextType.LINK, "https://loz.com")
                    ],
                new_nodes
                )


