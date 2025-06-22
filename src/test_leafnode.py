import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def testing_leaf_node(self):
        #Testing LeafNode works
        node = LeafNode(value="Hello World!", tag="p")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")
        
        #Testing with no value
    def test_with_empty_string(self):
        node1 = LeafNode(value="", tag="p")
        self.assertEqual(node1.to_html(), f"<p></p>")
    
    def test_with_none(self):
        node1 = LeafNode(value=None, tag="p")
        with self.assertRaises(ValueError):
            self.assertEqual(node1.to_html(), None)
       
        #Testing with no tag
        node2 = LeafNode(value="Jon Belion is making music", tag="")
        self.assertEqual(node2.to_html(), "Jon Belion is making music")
        
        #Testing leafnode to_html works as expected
        node3 = LeafNode(value="Youre our 100th Visitor!", tag="a", props={"href": "https://giveusyourmoney.net"})
        self.assertEqual(node3.to_html(), '<a href="https://giveusyourmoney.net">Youre our 100th Visitor!</a>')



