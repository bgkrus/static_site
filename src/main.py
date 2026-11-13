from textnode import TextType
from textnode import TextNode


def main():
    text = 'This is some anchor text'
    text_type = TextType.LINK_TEXT
    url = 'https://www.boot.dev'
    print(f"TextNode(text={text}, text_type={text_type}, url={url})")

main()