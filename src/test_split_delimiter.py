import unittest

from split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def print_out_split_nodes(self):
        node1 = TextNode("This is test `test` text", TextType.Text)
        new_node = split_nodes_delimiter([node1], "`", TextType.CODE)

   
