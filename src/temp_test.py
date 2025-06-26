from split_delimiter import split_nodes_delimiter
from textnode import TextNode
from textnode import TextType

node1 = TextNode("Testing, 1234", TextType.TEXT)
node2 = TextNode("Testing, 5678", TextType.TEXT)
node3 = TextNode("This is code", TextType.CODE)

new_list = []

new_list.append(node1)
new_list.append(node2)
new_list.append(node3)

print(f"Appened List: {new_list}")

extended_list = []

extended_list.extend(new_list)

print(f"Extended List: {extended_list}")
