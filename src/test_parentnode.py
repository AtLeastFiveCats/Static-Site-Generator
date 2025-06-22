import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("child", "span")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("grandchild", "b")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_empty_children(self):
        child_node = LeafNode(None)
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(repr(parent_node.children), '[None, None, None, ]')

        parent2_node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            self.assertEqual(parent2_node.to_html(), "<p></p>")

    def test_empty_tag(self):
        child_node = LeafNode("this is value", "p")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_children_with_boolean_values(self):
        child_node = LeafNode("This is True", "div", props={"untrue": True})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.children[0].props["untrue"], True)

    def test_without_children(self):
        parent_node = ParentNode("a", None)
        with self.assertRaises(ValueError):
            self.assertEqual(parent_node.to_html(), "<a></a>")

    def test_with_multiple_children(self):
        grandchild_node = LeafNode("painting", "div")
        child_node = ParentNode("span", [grandchild_node])
        child2_node = LeafNode("Tis but a scratch", "p")
        parent_node = ParentNode("div", [child_node, child2_node])
        self.assertEqual(parent_node.to_html(), "<div><span><div>painting</div></span><p>Tis but a scratch</p></div>")
  
    def test_deeply_nested_children(self):
        greatgrandchild_node = LeafNode("Colossal DreadMaw", "title")
        grandchild_node = ParentNode("div", [greatgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("body", [child_node])
        grandparent_node = ParentNode("div", [parent_node])
        greatgrandparent_node = ParentNode("span", [grandparent_node])
        self.assertEqual(greatgrandparent_node.to_html(), "<span><div><body><span><div><title>Colossal DreadMaw</title></div></span></body></div></span>")

    def test_children_with_props(self):
        child_node = LeafNode("Colossal DreadMaw", "a", props={"href": "https://scryfall.com/Colossal%29DreadMaw"})
        parent_node = ParentNode("title", [child_node])
        self.assertEqual(parent_node.to_html(), '<title><a href="https://scryfall.com/Colossal%29DreadMaw">Colossal DreadMaw</a></title>')

if __name__ == "__name__":
    unittest.main()



