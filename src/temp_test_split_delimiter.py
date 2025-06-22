from textnode import TextNode, TextType
from split_delimiter import split_nodes_delimiter

test_node = TextNode("This is a text with `code` in it", TextType.TEXT)
result = split_nodes_delimiter([test_node], "`", TextType.CODE)

print(f"Split Nodes: {result}")

