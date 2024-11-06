import xmltodict
import json

xml = open("schedule.xml", 'r', encoding='utf-8').read()
dict_data = xmltodict.parse(xml)
open("res1.json", "w", encoding='utf-8').write(json.dumps(dict_data, ensure_ascii=False, indent=4))
