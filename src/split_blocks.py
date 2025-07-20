#Converts regular text into blocks of text that can more easily be converted into textnodes
def markdown_block_splitter(markdown_text):
    new_text = []
    split_text = markdown_text.split("\n\n")
    for line in split_text:
        stripped_line = line.strip()
        if stripped_line != "":
            new_text.append(stripped_line)
    return new_text
