import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()

