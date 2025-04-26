from textnode import TextNode
from textnode import TextType

def main():
    new_node = TextNode("Test test", TextType.TEXT, "https://www.google.com")
    print(new_node)

if __name__ == "__main__":
    main()
