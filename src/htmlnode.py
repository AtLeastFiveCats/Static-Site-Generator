
class HTMLNode:
        def __init__(self, value=None, tag=None, children=None, props=None):
            self.tag = tag
            self.value = value
            self.children = children
            self.props = props

        def to_html(self):
            raise NotImplementedError

        def props_to_html(self):
            if not self.props:
                return ""

            results = ""
            for key, value in self.props.items():
                results += f' {key}="{value}"'
            return results

        def __repr__(self):
            str_children = str(self.children)
            str_props = str(self.props)
            return f"{self.tag}, {self.value}, {str_children}, {self.props_to_html()}"

       
