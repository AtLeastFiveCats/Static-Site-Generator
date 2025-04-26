import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_that__repr___works(self):
#Testing if __repr__ works as expected
        node1 = HTMLNode(tag="p", value="This is some test text")
        expected = f'p, This is some test text, None,  '
        self.assertEqual(repr(node1), expected)

#Testing if props_to_html works without any input
        self.assertEqual(node1.props_to_html(), " ")

#Testing if props_to_html works as expected
        node2 = HTMLNode(tag="a", value="Goodle!", props={"href": "https://goodle.com", "target": "_blank"})
        expected = f' href="https://goodle.com" target="_blank"'
        self.assertEqual(node2.props_to_html(), expected)

#Need to add testing for children
        childnode1 = HTMLNode(tag="p", value="This is some test text")
        childnode2 = HTMLNode(tag="a", value="Click Here!", props={"href": "https://scamsite.com", "target": "_blank"})
        parentnode1 = HTMLNode(tag="div", children=[childnode1, childnode2], )

#Testing parent node 1
        self.assertEqual(parentnode1.tag, "div")
        self.assertEqual(len(parentnode1.children), 2)

#Testing child node 1
        self.assertEqual(parentnode1.children[0].tag, "p")
        self.assertEqual(parentnode1.children[0].value, "This is some test text")

#Testing child node 2
        self.assertEqual(parentnode1.children[1].tag, "a")
        self.assertEqual(parentnode1.children[1].props["href"], "https://scamsite.com")

#Testing edge cases

#Testing empty values
        node3 = HTMLNode()
        self.assertIsNone(node3.tag)
        self.assertIsNone(node3.value)
        self.assertIsNone(node3.children)
        self.assertIsNone(node3.props)

        node4 = HTMLNode(tag="", value="")
        self.assertEqual(node4.tag, "")
        self.assertEqual(node4.value, "")

        node5 = HTMLNode(tag="", value="", props="")
        self.assertEqual(node5.props, "")

#Testing special characters in props
        node5 = HTMLNode(tag="a", value="Tricky", props={"data-value": "text and or \" '"})
        self.assertEqual(node5.props["data-value"], "text and or \" '")
    
#Testing nested children structure
        childnode3 = HTMLNode(tag="div", children=[childnode1, childnode2])
        parentnode2 = HTMLNode(tag="p", children=[childnode3])
        self.assertEqual(len(parentnode2.children), 1)
        self.assertEqual(parentnode2.children[0].children[0].tag, "p")
        self.assertEqual(parentnode2.children[0].children[1].props["href"], "https://scamsite.com")

#Testing props with boolean values
        node6 = HTMLNode(tag="input", props={"disabled": False})
        self.assertEqual(node6.props["disabled"], False)


if __name__ == "__name__":
    unittest.main()
