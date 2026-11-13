import unittest
from htmlnode import HTMLNode


class HTMLNodeTest(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=https://example.com target=_blank")   

    def test_props_to_html_none(self):
        node = HTMLNode(tag="a", value="Click here", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'container'})")

if __name__ == "__main__":
    unittest.main()