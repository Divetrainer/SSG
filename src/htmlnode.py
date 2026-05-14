from textnode import TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError

        if self.tag != None:
            tag = self.tag
            value = self.value

            if self.props == None: return f'<{tag}>{value}</{tag}>'

            return f'<{tag}{self.props_to_html()}>{value}</{tag}>'
        else:
            if self.props == None:
                return f'{self.value}'
            return f'{self.props_to_html()}{self.value}'

    def props_to_html(self):
        if self.props is None:
            return ''
        output = ''
        for i in self.props:
            output += f' {i}="{self.props[i]}"'
        return output

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props


    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props

    def __repr__(self):
        raise NotImplimentedError

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing, please include a tag")
        if self.children is None:
            raise ValueError("No children present")
        output = ''
        for child in self.children:
            output += child.to_html()
        return f'<{self.tag}>{output}</{self.tag}>'


def text_node_to_html_node(text_node):
    if text_node.text_type != "TextType.BOLD":
        raise Exception("Selected text type not supported at this time")
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
