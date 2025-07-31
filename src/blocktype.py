from enum import Enum
from textnode import TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
   # Defining our variables
    heading = ""
    blocks = block.split("\n")
    # Baby's first list comprehension!
    lines = [line.strip() for line in blocks]

    if not block:
        return BlockType.PARAGRAPH

    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE
    
    for i in range(6):
        heading += "#"
        for line in lines:
            if line.startswith(f"{heading} "):
                return BlockType.HEADING


    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
 
    elif all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
        
    else:
        return BlockType.PARAGRAPH 

