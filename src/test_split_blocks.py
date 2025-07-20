import unittest
from split_blocks import markdown_block_splitter

class Test_split_blocks(unittest.TestCase):
    def test_reg_text(self):
        input_text = """This is a paragraph with a space?"""
        expected_text = ["This is a paragraph with a space?"]
        new_text = markdown_block_splitter(input_text)
        self.assertListEqual(expected_text, new_text)

    def test_paragraphs(self):
        input_text = """
        This is a paragraph

        with a space
        """
        expected_text = ["This is a paragraph", "with a space"]
        new_text = markdown_block_splitter(input_text)
        self.assertListEqual(expected_text, new_text)


    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_block_splitter(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_multiple_whitespaces(self):
        input_text = """
        this is a **bold** graph


        with multiple white spaces
        """
        new_text = markdown_block_splitter(input_text)
        self.assertListEqual(
                [
                    "this is a **bold** graph",
                    "with multiple white spaces"
                    ],
                new_text
                )
    def test_empty_lines(self):
        new_text = markdown_block_splitter("")
        self.assertListEqual([], new_text)

    def test_leading_and_trailing_whitespaces(self):
        input_text = """
            Leading whitespace

            Trailing whitespace     
        """
        new_text = markdown_block_splitter(input_text)
        self.assertListEqual(
                [
                    "Leading whitespace",
                    "Trailing whitespace"
                    ],
                new_text
                )
