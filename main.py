

with open("books/frankenstein.txt", "r") as frankenstein_txt: 
    content = frankenstein_txt.read()


def getSortKey(item: tuple) -> str:
    return item[1]



def wordCount(text:str) -> int:
    wordArray = text.split()
    return len(wordArray)



def characterCount(text: str) -> int:
    lowerCaseText= text.lower()
    uniqueCharacters = {}
    if text is not None: 
        for characters in lowerCaseText:
            if characters in uniqueCharacters.keys():
                uniqueCharacters[characters] += 1
            else:
                uniqueCharacters[characters]  = 1
    return uniqueCharacters



def reportSortedDict(text: str) -> str: 
    reportingItem = list(characterCount(text).items())
    reportingItem.sort(reverse= True, key= getSortKey)
    sortedList = [] 
    for items in reportingItem:
        if items[0].isalpha():
            sortedList.append(items) 
    return sortedList

def printToConsole(text) -> None:
    lettersCount = reportSortedDict(text)
    print(f"Generally, frankenstein.txt has {wordCount(text)} words\n")
    for letters in lettersCount:
        print(f"The '{letters[0]}' character appeared {letters[1]} times\n")
    print(f"All alphabet characters counted, we don't have that many '{lettersCount[-1][0]}' characters")








if __name__ == '__main__':
    printToConsole(content)
    
