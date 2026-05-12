from textnode import TextNode
from htmlnode import HTMLNode

test_html = HTMLNode("a", None, None, '{"href":"https://www.google.com"}')
test_node = TextNode("sample alt text", "link", "link to image")

print(test_node)
print(test_html)
