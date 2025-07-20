import unittest
from textnode import TextType
from blocktype import block_to_block_type
from split_blocks import markdown_block_splitter

class Test_block_type(unittest.TestCase):
    def test_regular_text(self):
        input_text = "This is a normal piece of text"
        split_text = markdown_block_splitter(input_text)
        text_type = block_to_block_type(split_text)
        self.assertEqual(text_type, TextType.TEXT)
