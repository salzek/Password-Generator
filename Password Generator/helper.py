import  re
from unidecode import unidecode
from itertools import product
import exrex


def myReplace(leet, old, new, suffix):
    wordlist = []
    suffix = str(suffix)
    specialCharLen = len(new)
    
    str_ = list(enumerate(leet))
    listStr = list(leet)
    indexesOfX = [index for index, char in str_ if char == 'x' ]
    
    if specialCharLen == 1:
        for index_ in indexesOfX:
            listStr[index_] = new  
            lastWord = ''.join(listStr).replace('x', '')
            wordlist.append(lastWord)
            listStr = list(leet)
            listStr[index_] = suffix + new  
            lastWord = ''.join(listStr).replace('x', '')
            wordlist.append(lastWord)
            listStr = list(leet)
            listStr[index_] = new + suffix  
            lastWord = ''.join(listStr).replace('x', '')
            wordlist.append(lastWord)
            listStr = list(leet)
            listStr[index_] = suffix  
            lastWord = ''.join(listStr).replace('x', '')
            wordlist.append(lastWord)
            if index_ == indexesOfX[0]:
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = ''
                listStr[indexesOfX[indexesOfX.index(index_)+2]] = new
                lastWord = ''.join(listStr)
                wordlist.append(lastWord)
            elif index_ == indexesOfX[1]:
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = new
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = ''
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new
                lastWord = ''.join(listStr)
                wordlist.append(lastWord)
            elif index_ == indexesOfX[2]:
                listStr[indexesOfX[indexesOfX.index(index_)-2]] = new
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr[indexesOfX[indexesOfX.index(index_)-2]] = ''
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = new
                lastWord = ''.join(listStr)
                wordlist.append(lastWord)
            listStr = list(leet)
    if specialCharLen == 2:
        for index_ in indexesOfX:
            if index_ == indexesOfX[0]:
                listStr[index_] = new  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new  
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = suffix
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new  
                listStr[indexesOfX[indexesOfX.index(index_)+2]] = suffix
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = suffix + new  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new + suffix  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0]
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0] + suffix
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = suffix + new[0]
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0]
                listStr[indexesOfX[indexesOfX.index(index_)+2]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0]
                listStr[indexesOfX[indexesOfX.index(index_)+2]] = suffix + new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0]
                listStr[indexesOfX[indexesOfX.index(index_)+2]] = new[1] + suffix
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
            elif index_ == indexesOfX[1]:
                listStr[index_] = new  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new  
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = suffix
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new  
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = suffix
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = suffix + new  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new + suffix  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0]
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0] + suffix
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = suffix + new[0]
                listStr[indexesOfX[indexesOfX.index(index_)+1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0] + suffix
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = suffix + new[0]
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
            elif index_ == indexesOfX[2]:
                listStr[index_] = new  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = suffix + new  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new + suffix  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = new[0] + suffix
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
                listStr[index_] = suffix + new[0]
                listStr[indexesOfX[indexesOfX.index(index_)-1]] = new[1]  
                lastWord = ''.join(listStr).replace('x', '')
                wordlist.append(lastWord)
                listStr = list(leet)
    
    return wordlist
    
def generateSpecialCharSeries(max):
    specialChars = "(~|\!|@|#|\$|%|\^|\&|\*|_|-|\+|=|`|\||\(|\)|\{|\}|:|;|'|<|>|,|\.|\?|/|\")"
    pattern = ""

    for i in range(1, max+1):
        if i == 1:
            pattern += specialChars
        else:
            pattern += '(' + specialChars
    else:
        pattern += ')?' * (max - 1)

    return sorted(list(exrex.generate(pattern)), key=len)

def check(list):
    return all(i == list[0] for i in list)

def myUpper(string):
    i = 0
    for char_ in string:
        if char_ in "i":
            x = string[i:].replace(char_, "İ")
            return (string[:i]+x).upper()
        i += 1
    else:
        return string.upper()

def myLower(string):
    word = ''
    for i in string:
        if i == 'I':
            word += 'ı'
        elif i == 'İ':
            word += 'i'
        else:
            word += i
    else:
        return word.lower()

def anti_vowel(s):
    wordArr = []
    
    unidecoded = unidecode(s)

    if re.findall('[AEIOUÖ]', unidecoded[0],  flags=re.IGNORECASE):
        wordArr.append(s[0]+re.sub(r'[AEIOU]', '', unidecoded, flags=re.IGNORECASE))

    if re.findall('[AEIOU]', s[-1],  flags=re.IGNORECASE):
        wordArr.append(re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE)+s[-1])
    
    if unidecoded != s:
        wordArr.append(re.sub(r'[AEIOU]', '', unidecoded, flags=re.IGNORECASE))
    
    wordArr.append(re.sub(r'[AEIOU]', '', s, flags=re.IGNORECASE))
    
    return list(set(wordArr))

def mix(*args):
    benzersizler = []
    for i in list(product(args, repeat=len(args))):
        if len(set(i)) == len(i):
            benzersizler.append(''.join(i))
        else:
            continue
    else:
        return benzersizler

def mix2(args, passPol):
    wordlist = []
    nameSurnameCombinations = []

    for i in args:
        if not passPol:
            for j in myCombination(i):
                unidecoded = unidecode(j)

                if unidecoded != j:
                    wordlist.append(unidecoded)
                wordlist.append(j)
        else:
            unidecoded = unidecode(i)
            if unidecoded != i:
                wordlist.append(myCapitalize(i))
            wordlist.append(myCapitalize(i))
    
    for i in list(product(wordlist, repeat=2)):
        word = ''.join(i)
        if passPol and len(i) > 1 and myLower(word) == i and myUpper(word) == i:
            continue
        nameSurnameCombinations.append(i)
        
    return nameSurnameCombinations

def mix3(text, suffix):
    special_chars = r'[~\!@#\$%\^&\*_\-+=`|\(\){}:;\'<>,\.\?/"]'
    count = re.findall(special_chars, text)
    wordlist = []

    #if len(count) == 1:
        #arr  = re.findall(r'\w+|' + special_chars+special_chars+'?', text)
    #    for i in arr:
    #        if i == ''.join(count):
    #            for j in suffix:
    #                pass
                    #wordlist.append(re.sub(i, str(j)+i, ''.join(arr)))
                    #wordlist.append(re.sub(i, i+str(j), ''.join(arr)))
                    #wordlist.append(re.sub(i, str(j), ''.join(arr)))

    if len(count) == 2:
        arr  = re.findall(r'\w+|' + special_chars+special_chars+'?', text)
        print(count)
        if len(arr) == 2:
            count = re.findall(special_chars+special_chars, text)
            for i in arr:
                if i == ''.join(count):
                    for j in suffix:
                        wordlist.append(re.sub(i, str(j)+i, ''.join(arr)))
                        wordlist.append(re.sub(i, i+str(j), ''.join(arr)))
                        wordlist.append(re.sub(i, str(j), ''.join(arr)))
        elif len(arr) > 2:
            print(arr)
            for tup in enumerate(arr):
                index, i = tup
                if i not in special_chars:
                    continue
                
                if index == 0:
                    for j in suffix:
                        wordlist.append(re.sub('^'+i, str(j)+i, ''.join(arr)))
                        wordlist.append(re.sub('^'+i, i+str(j), ''.join(arr)))
                        wordlist.append(re.sub('^'+i, str(j), ''.join(arr)))
                elif index == 1:
                    for j in suffix:
                        wordlist.append(re.sub(i, str(j)+i, ''.join(arr), count=1))
                        wordlist.append(re.sub(i, i+str(j), ''.join(arr), count=1))
                        wordlist.append(re.sub(i, str(j), ''.join(arr), count=1))
                elif index == 3:
                    for j in suffix:
                        wordlist.append(re.sub(i+'$', str(j)+i, ''.join(arr)))
                        wordlist.append(re.sub(i+'$', i+str(j), ''.join(arr)))
                        wordlist.append(re.sub(i+'$', str(j), ''.join(arr)))
    return wordlist

def myCapitalize(string):
    converter = {
        'ı':'I',
        'i':'İ',
    }

    if string[0] in converter:
        return converter[string[0]]+string[1:]
    
    return string.capitalize()

def myCombination(word):
    word = myLower(word)

    return [word, myCapitalize(word), myUpper(word)] if len(word) != 1 else [word, myCapitalize(word)]

def myMix(*args):
    array = []
    if isinstance(args, list):
        args = list(*args)
    
    str_args = [str(arg) for arg in args]
    args = str_args
    i = len(args)
    
    if i == 2:
        array += [
            args[0] + args[1],
            args[1] + args[0]
            ]
    if i == 3:
        array += [
            args[0] + args[1] + args[2],
            args[1] + args[0] + args[2],
            args[1] + args[2] + args[0],
            args[2] + args[0] + args[1],
            ]
    if i == 3 and len(set(args)) == len(args):
        array += [
            args[0] + args[2] + args[1],
            args[2] + args[1] + args[0]
            ]
    if i == 4:
        array += [
            args[0] + args[1] + args[2] + args[3],
            args[0] + args[3] + args[1] + args[2],
            args[1] + args[0] + args[2] + args[3],
            args[1] + args[2] + args[0] + args[3],
            args[1] + args[2] + args[3] + args[0],
            #
            args[2] + args[0] + args[3] + args[1],
            args[2] + args[3] + args[1] + args[0],
            args[2] + args[3] + args[0] + args[1],
            #
            args[3] + args[0] + args[1] + args[2],
            args[3] + args[1] + args[2] + args[0],
            args[3] + args[1] + args[0] + args[2],
            ]    
    if i == 4 and len(set(args)) == len(args):
        array += [
            args[0] + args[1] + args[3] + args[2],
            args[0] + args[2] + args[1] + args[3],
            args[0] + args[2] + args[3] + args[3],
            args[0] + args[3] + args[2] + args[1],
            args[1] + args[0] + args[3] + args[2],
            args[1] + args[3] + args[2] + args[0],
            args[2] + args[0] + args[1] + args[3],
            args[2] + args[1] + args[0] + args[3],
            args[2] + args[1] + args[3] + args[0],
            args[3] + args[0] + args[2] + args[1],
            args[3] + args[2] + args[0] + args[1],
            args[3] + args[2] + args[1] + args[0],
            ]  
    return array

def replace_nth_occurrence(string, old, new, n):
    parts = string.split(old)
    
    return old.join(parts[:n]) + new + old.join(parts[n:])