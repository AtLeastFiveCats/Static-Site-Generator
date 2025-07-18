def markdown_block_split(markdown_text):
    split_text = markdown_text.split("\n\n")
    stripped_text = split_text.strip()
    for line in stripped_text:
        if line == "":
            stripped_text.del[line]
    return stripped_text
