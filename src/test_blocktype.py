import unittest
from blocktype import block_to_block_type
from split_blocks import markdown_block_splitter
from blocktype import BlockType

class Test_block_type(unittest.TestCase):
    def test_regular_text(self):
        input_text = "This is a normal piece of text"
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.PARAGRAPH)
    
    def test_heading(self):
        input_text = "## Heading"
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.HEADING)

    def test_seven_heading(self):
        input_text = "####### Heading"
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.PARAGRAPH)

    def test_multiple_lines(self):
        input_text = [
                "This is a line",
                "This is a second line",
                "This is a third line"
                ]
        for line in input_text:
            results = block_to_block_type(line)
            self.assertEqual(results, BlockType.PARAGRAPH)

    def test_code(self):
        input_text = "```code here```"
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.CODE)

    def test_multi_line_code(self):
        input_text = """```code 1
        code 2
        code 3
        ```"""
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.CODE)

    def test_unordered_list(self):
        input_text = '''- a line
        - a second line
        - a third line'''
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        input_text = """1. a line
        2. a line
        3. A line"""
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.ORDERED_LIST)

    def test_quotes(self):
        input_text = """ > johnson
        > son of jon
        > father of jon"""
        results = block_to_block_type(input_text)
        self.assertEqual(results, BlockType.QUOTE)


