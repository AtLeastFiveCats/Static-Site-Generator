from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, props)

    def to_html(self):
           
        #If value is empty
        if not self.value:
            raise ValueError
           
        #If tag is empty
        if not self.tag:
            return f"{self.value}"
           
       #Otherwise return the formated string
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


