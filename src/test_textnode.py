import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node=TextNode("This is a text node", TextType.BOLD)
        node2=TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node=TextNode("This is a text node", TextType.BOLD)
        node2=TextNode("This is an image", TextType.IMAGE, url="https://coolurl.com")
        self.assertNotEqual(node, node2)

    def test_notNone(self):
        node=TextNode("This is an image with a url", TextType.IMAGE, url="https://url.com")
        self.assertIsNotNone(node.url)

if __name__ == "__main__":
    unittest.main()
