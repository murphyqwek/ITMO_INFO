xml = ""
parsed = dict()
xml = open("schedule.xml", "r", encoding="utf-8").readlines()
i = 0
TAB = "    "

def checkForOpenNewBranch(field: str) -> str:
    field = field.strip()
    if field.find("</") != -1:
        return ""
    
    return field[1:-1]

def checkForCloseCurrentBracnh(name: str, field: str) -> bool:
    return f"</{name}>" == field.strip()

def parseElement(field: str) -> tuple[str, str]:
    field = field.strip()

    #Получаем имя поля
    name = field[1:field.find(">")]

    #Получаем значение поля
    value = field[field.find(">") + 1: len(field) - (3 + len(name))]

    return (name, value)
    

def parseBranch(BranchName: str) -> dict:
    global i
    branch = dict()

    stroka = xml[i].replace("\n", "")
    while not checkForCloseCurrentBracnh(BranchName, stroka):
        #Проверяем на новую ветвь
        newBranchName = checkForOpenNewBranch(stroka)
        if newBranchName != "":
            i += 1
            newBranch = parseBranch(newBranchName)
            branch[newBranchName] = newBranch
            if i >= len(xml):
                break
            stroka = xml[i]
            continue
        
        #Парсим элемент
        name, value = parseElement(stroka)
        branch[name] = value
        i += 1
        if i >= len(xml):
            break
        stroka = xml[i]

    i += 1
    return branch


def pretty(d, indent=0):
   for key, value in d.items():
      print(TAB * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print(TAB * (indent+1) + str(value))

def jsonPrinter(parsedDict: dict, depth = 1):
    last_index_of_element_in_branch = len(parsedDict.keys()) - 1
    for i, key in enumerate(parsedDict.keys()):
        element = parsedDict[key]
        last_str = ""
        if type(element) is not dict:
            last_str = TAB * depth + f'"{key}": "{element}"'
        else:
            print(TAB * depth + f'"{key}": ' + "{")
            jsonPrinter(element, depth + 1)
            last_str = TAB * depth + "}"

        if i != last_index_of_element_in_branch:
            last_str += ","
        
        print(last_str)

parsedDict = parseBranch("")

print("{")
jsonPrinter(parsedDict)
print("}")
