from htmlnode import HTMLNode, LeafNode, ParentNode, text_to_html_node
from textnode import TextType, TextNode

def split_node_delimiters(old_nodes, delimiter, text_type):
    if old_nodes.text_type != "TextType.PLAIN":
        return old_nodes
    new_group = old_nodes.text.split()
    nodetype = str()
    validation = 0
    for word in new_group:
        if word[0] == delimiter:
            nodetype += word
            validation += 1
        if word[-1] == delimiter:
            nodetype += f'/n {word}'
            validation -= 1
    if validation > 0 or validation < 0:
        raise Exception("Incorrectly formatted text node")


