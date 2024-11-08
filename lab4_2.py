import re
xml = ""
parsed = dict()
xml = open("schedule.xml", "r", encoding="utf-8").read()
i = 0
TAB = "    "

def parseXML(xml: str) -> dict:
    tag_pattern = re.compile(r'<(\w+)>(.*?)</\1>', re.DOTALL)
    res = dict()

    for m in tag_pattern.finditer(xml):
        name = m.group(1)
        value = m.group(2).strip()
        if re.search(r'<\w+>', value):
            res[name] = parseXML(value)
        else:
            res[name] = value
    
    return res

def pretty(d, indent=0):
   for key, value in d.items():
      print(TAB * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print(TAB * (indent+1) + str(value))

def jsonPrinter(parsedDict: dict, depth = 1):
    output = ""
    last_index_of_element_in_branch = len(parsedDict.keys()) - 1
    for i, key in enumerate(parsedDict.keys()):
        element = parsedDict[key]
        last_str = ""
        if type(element) is not dict:
            last_str = "\n" + TAB * depth + f'"{key}": "{element}"'
        else:
            output += "\n" +TAB * depth + f'"{key}": ' + "{"
            output += jsonPrinter(element, depth + 1)
            last_str = "\n" + TAB * depth + "}"

        if i != last_index_of_element_in_branch:
            last_str += ","
        
        output += last_str
    return output

parsedDict = parseXML(xml)

res = jsonPrinter(parsedDict)

res = "{" + res + "\n}"

open("res2.json", 'w', encoding='utf-8').write(res)
