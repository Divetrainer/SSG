import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_propValueNotNone(self):
        node = HTMLNode(None,None,None,{"href":"https://www.google.com"})
        self.assertIsNotNone(node.props)

    def test_propnames(self):
        node = HTMLNode("a", "click here", None, {"href":"www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com"')

    def test_propIsNone(self):
        node = HTMLNode("h", "1", None, None)
        self.assertEqual(node.props_to_html(), '')

    def test_leaf_to_html_with_tag_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")

    def test_leaf_to_html_without_tag(self):
        node = LeafNode(None, "Hello World!")
        self.assertEqual(node.to_html(), "Hello World!")

    def test_leaf_to_html_with_tag_b(self):
        node = LeafNode("b", "Hello World!")
        self.assertEqual(node.to_html(), "<b>Hello World!</b>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Click Me!", {"href":"https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')

    def test_leaf_to_html_value_none(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_repr(self):
        node = LeafNode("a", "Click Me!", {"href":"https://www.google.com"})
        self.assertEqual(repr(node), "LeafNode(a, Click Me!, {'href': 'https://www.google.com'})")

    def test_parent_to_html(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_text_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

if __name__ == "__main__":
    unittest.main()

