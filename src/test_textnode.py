import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node3 = TextNode("__This is bold__", TextType.ITALIC)
        node4 = TextNode("```This is code```", TextType.CODE)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("[link](https://boot.dev)", TextType.LINK, "https://boot.dev")
        node6 = TextNode("[link](https://boot.dev)", TextType.LINK, "https://boot.dev")
        self.assertEqual(node5, node6)

        node7 = TextNode("More regular text", TextType.BOLD)
        node8 = TextNode("More regular text", TextType.CODE)
        self.assertNotEqual(node7, node8)

        node9 = TextNode("The lazy brown fox", TextType.TEXT, None)
        node10 = TextNode("The lazy brown fox", TextType.TEXT, None)
        self.assertEqual(node9, node10)

        node11 = TextNode("Jumped over the quick red dog", TextType.TEXT, None)
        node12 = TextNode("Jumped over the quick red dog", TextType.QUOTE, None)
        self.assertNotEqual(node11, node12)

if __name__ == "__main__":
    unittest.main()
