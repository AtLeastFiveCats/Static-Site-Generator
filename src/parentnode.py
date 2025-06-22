from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None, value=None):
        super().__init__(value, tag, children, props)    

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag")

        if not self.children:
            raise ValueError("No Children")
        
        total_html = f"<{self.tag}>"
        for child in self.children:
            total_html += child.to_html()
        
        total_html += f"</{self.tag}>"
        
        return total_html
