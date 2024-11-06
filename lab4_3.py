from lark import Lark, Transformer
import json

grammar = """
    ?start: element+

    ?element: "<" tag ">" content "</" tag ">"   -> tag_content

    ?content: element+                          -> nested
            | value                             -> text

    tag: /[a-zA-Z_][a-zA-Z0-9_-]*/
    value: /[^<]+/

    %import common.WS_INLINE
    %ignore WS_INLINE
    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='start')

class XMLToDict(Transformer):
    def tag_content(self, items):
        tag, content = items
        return {tag: content}
    
    def text(self, items):
        return items[0]

    def nested(self, items):
        result = {}
        for item in items:
            result.update(item)
        return result

    def start(self, items):
        result = {}
        for item in items:
            result.update(item)
        return result

parse_tree = parser.parse(open("s.xml", encoding='utf-8').read())

def tree_to_dict(tree):
    if tree.data == 'tag_content':
        tag = tree.children[0].children[0].value
        content = tree_to_dict(tree.children[1])
        return {tag: content}
    elif tree.data == 'text':
        k = tree.children[0].children[0].value
        return k
    elif tree.data == 'nested':
        result = {}
        for child in tree.children:
            result.update(tree_to_dict(child))
        return result
    elif tree.data == 'start':
        result = {}
        for child in tree.children:
            result.update(tree_to_dict(child))
        return result
    return None

result = tree_to_dict(parse_tree)
print(json.dumps(result, ensure_ascii=False, indent=4))