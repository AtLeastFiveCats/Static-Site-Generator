import re


def extract_markdown_images(text):
    extract = re.findall("\![\w+\]\(\w+\)")
