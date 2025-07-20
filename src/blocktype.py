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
    expected_number = 1
    hash_count = 0

    for text in block:
        for character in text:
            if character == "#":
                hash_count += 1
            else:
                continue

        if len(text[:hash_count]) <= len(text) and hash_count <= 6:
            if text[hash_count] + text[hash_count + 1] == "# ":
                return BlockType.HEADING

        elif text[:2] == "```" and text[-3::] == "```":
            return BlockType.CODE

        elif text[0] == ">":
            return BlockType.QUOTE

        elif text[:1] == "- ":
            return BlockType.UNORDERED_LIST

        elif text[:2] == f"{expected_number}. ":
            return BlockType.ORDERED_LIST
        
        else:
            return TextType.TEXT

