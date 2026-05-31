import unittest
from inline_markdown import split_node_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode


class TestSplitNode(unittest.TestCase):

    def test_bold_typing(self):
        node = TextNode("Sample **bold** word", TextType.PLAIN)
        output = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(output, 
                    [
                        TextNode("Sample ", TextType.PLAIN), 
                        TextNode("bold", TextType.BOLD), 
                        TextNode(" word", TextType.PLAIN)
                    ]
                )

    def test_italic_typeing(self):
        node = TextNode("Sample _italic_ word", TextType.PLAIN)
        output = split_node_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(output, 
                    [
                        TextNode("Sample ", TextType.PLAIN), 
                        TextNode("italic", TextType.ITALIC), 
                        TextNode(" word", TextType.PLAIN)
                    ]
                )

    def test_code_typeing(self):
        node = TextNode("Sample `code` word", TextType.PLAIN)
        output = split_node_delimiter([node], "`", TextType.CODE)
        self.assertEqual(output, 
                    [
                        TextNode("Sample ", TextType.PLAIN), 
                        TextNode("code", TextType.CODE), 
                        TextNode(" word", TextType.PLAIN)
                    ]
                )

    def test_no_delimiter(self):
        node = TextNode("Sample plain word", TextType.PLAIN)
        output = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(output, 
                    [
                        TextNode("Sample plain word", TextType.PLAIN)
                    ]
                )

    def test_mulitple_bold_words(self):
        node = TextNode("This has **bold one** and **bold two**.", TextType.PLAIN)
        output = split_node_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(output, 
                    [
                        TextNode("This has ", TextType.PLAIN),
                        TextNode("bold one", TextType.BOLD),
                        TextNode(" and ", TextType.PLAIN),
                        TextNode("bold two", TextType.BOLD),
                        TextNode(".", TextType.PLAIN)
                    ]
                )

    def test_endtoend_grouping(self):
        node = TextNode("_all italic_", TextType.PLAIN)
        output = split_node_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(output,
                    [
                        TextNode("all italic", TextType.ITALIC)
                    ]
                )

    def test_raise_error_check(self):
        node = TextNode("This has a `unterminated code", TextType.PLAIN)
        # output = split_node_delimiter([node], "`", TextType.CODE)
        with self.assertRaises(Exception):
            split_node_delimiter([node], "`", TextType.CODE)


    def test_extract_image(self):
        test = "This is a text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(test)
        self.assertEqual(output, 
                    [
                        ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                        ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
                    ]
                )

    def test_extract_image(self):
        test = "This is a text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(test)
        self.assertEqual(output, 
                    [
                        ("to boot dev", "https://www.boot.dev"),
                        ("to youtube", "https://www.youtube.com/@bootdotdev")
                    ]
                )






if __name__ == "__main__":
    unittest.main()
