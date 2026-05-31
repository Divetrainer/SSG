import re
from textnode import TextType, TextNode

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("Delimiters not formatted correctly")

        for i in range(len(parts)):
            if parts[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(f"{parts[i]}", TextType.PLAIN))
            else:
                new_nodes.append(TextNode(f"{parts[i]}", text_type))

    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches



def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        current_text = old_node.text
        image_metadata = extract_markdown_image(current)
        for image in image_metadata:
            parts = current_text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            for i in range(len(parts)):
                if parts[i] == '':
                    continue
                new_nodes.append(TextNode(f"{parts[i]}", TextType.PLAIN))




    return new_nodes


def split_nodes_link(old_nodes)
    pass
