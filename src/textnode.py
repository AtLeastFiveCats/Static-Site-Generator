from enum import Enum

class TextType(Enum):
    TEXT = "text" 
    BOLD = "bold"
    ITALIC = "italic"
    IMAGE = "image" 
    LINK = "link" 
    CODE = "code"
    QUOTE = "quote"
#These texttypes are not supported just yet
    HEADING = "heading"
    ORDERED_LIST = "ordered list"
    UNORDERED_LIST = "unordered list"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text and self.text_type == other.text_type and self.url == other.url):
            return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


