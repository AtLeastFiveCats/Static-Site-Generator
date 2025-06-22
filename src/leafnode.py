from htmlnode import HTMLNode


#Should this class does not take children, I couldn't figure out how to not include it in the constructor
class LeafNode(HTMLNode):
    def __init__(self, value, tag=None,children=None, props=None):
        super().__init__(value, tag, children, props)

    def to_html(self):
           
        #If value is empty
        if self.value == None:
            raise ValueError("LeafNode cannot have no value")
           
        #If tag is empty
        if not self.tag:
            return f"{self.value}"
           
       #Otherwise return the formated string
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


