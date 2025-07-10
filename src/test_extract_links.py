import unittest
from extract_links import extract_markdown_images
from extract_links import extract_markdown_links

class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
                )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_markdown_without_anchor(self):
        matches = extract_markdown_links(
                "This is text without anchor text (https://youtube.com)"
                )
        self.assertEqual([], matches)

    def test_markdown_without_image(self):
        matches = extract_markdown_images(
                "This is text without image(https://youtube.com)"
                )
        self.assertEqual([], matches)

    def test_markdown_multiple_matches(self):
        matches = extract_markdown_images(
                "markdown ![markdown](https://markdown.com)![markup](https://markup.com)"
                )
        self.assertListEqual([("markdown", "https://markdown.com"), ("markup", "https://markup.com")], matches)

    def test_markdown_multiplue_links(self):
        matches = extract_markdown_links(
                "link [link1](https://link.com)[butwait](https://but.com)"
                )
        self.assertListEqual([("link1", "https://link.com"), ("butwait", "https://but.com")], matches)

    def test_empty_images(self):
        matches = extract_markdown_images("")
        self.assertEqual([], matches)

    def test_empty_link(self):
        matches = extract_markdown_links("")
        self.assertEqual([], matches)

