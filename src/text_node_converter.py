from textnode import TextNode
from textnode import TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(text_node.text)

        case TextType.BOLD:
            return LeafNode(text_node.text, tag="b")

        case TextType.ITALIC:
            return LeafNode(text_node.text, tag="i")

        case TextType.CODE:
            return LeafNode(text_node.text, tag="code")

        case TextType.LINK:
            return LeafNode(text_node.text, tag="a", props={"href": text_node.url})

        case TextType.IMAGE:
            return LeafNode("", tag="img", props={"src": text_node.url, "alt": text_node.text})

        case _:
            raise Exception("Not a correct text node")
        

