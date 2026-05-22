from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitnode import split_nodes_delimiter

test_html = HTMLNode("a", None, None, '{"href":"https://www.google.com"}')
test_node = TextNode("sample alt text", "link", "link to image")


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType.__members__:
        raise Exception("Selected text type not supported at this time")
    

print(test_node)
print(test_html)
