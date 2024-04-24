from helper import myLower, anti_vowel, myCapitalize, myUpper, myCombination, mix2, myReplace, generateSpecialCharSeries
from variables import leetspeak_dict, monthsTr, citiesTr, popularKeysInTurkey
from itertools import product 
from unidecode  import unidecode
from rules import *
import exrex, re, gui_, os.path as path
from variables import ROOT_DIR

def generateLeetSpeakCombinations(word):
    array = []
    words = []
    for _char in word:
        if _char in leetspeak_dict:
            array.append(leetspeak_dict[_char])

    three_combinations = list(product(*array))
    
    for combination in three_combinations:
        _word = ''
        i = 0
        for _char in word:
            if _char in leetspeak_dict:
                _word += combination[i]
                i += 1
            else:
                _word += _char
        else:
            if  _word in anti_vowel(word):
                continue
            words.append(_word)
    else:
        return words

def generateWordlistForDomain(domainName, passPol):
    
    wordlist =[]
    
    f =  open(f"{ROOT_DIR}\\raw-files\\w-{domainName}.txt", "w", encoding="utf-8")

    if not re.findall('[AEIOU]', domainName[0],  flags=re.IGNORECASE):  
        firstThreeCharVoweled =   re.sub(r'[AEIOU]', '', domainName, flags=re.IGNORECASE)[:3]
        wordlist.extend([firstThreeCharVoweled, myCapitalize(firstThreeCharVoweled), myUpper(firstThreeCharVoweled)])
    
    for i in generateLeetSpeakCombinations(domainName):
        if passPol and (i == myLower(i) or i == myUpper(i)):
            continue
        wordlist.append(i)

    for i in anti_vowel(domainName):
        if passPol and (i == myLower(i) or i == myUpper(i)):
            wordlist.append(i)
        for j in generateLeetSpeakCombinations(i):
            wordlist.append(j)

    for word in wordlist:
        unidecoded = unidecode(word)
        if unidecoded != word:
            f.write(unidecoded+'\n')
        f.write(word+'\n')

def generateGeneralCommonPasswords(passPol):
    f = open(f"{ROOT_DIR}\\raw-files\\w-general.txt", "w", encoding="utf-8")

    wordlist = []

    for word in citiesTr + monthsTr + popularKeysInTurkey:
        unidecoded = unidecode(word)
        if unidecoded != word:
            if passPol:
                wordlist.append(unidecoded)
            else:
                wordlist += myCombination(unidecoded)
        if passPol:
            wordlist.append(word)
        else:
            wordlist += myCombination(word)
    
    for word in wordlist:
            f.write(word+'\n')  

    # wordlist = []

    # for team in teams:
    #     for year in teams[team]:
    #         if not passPol:
    #             for c in myCombination(team):
    #                 wordlist += myMix(c, year)
    #         else:
    #             wordlist += myMix(team, year)
        
    #     unidecoded = unidecode(team)

    #     if unidecoded != team:
    #         if not passPol:
    #             for c in myCombination(unidecoded):
    #                 for year in teams[team]:
    #                     wordlist += myMix(c, year)
    #         else:
    #             wordlist += myMix(unidecoded, year)
    # else:
    #     for i in wordlist:
    #         f.write(i+'\n')
    
def generateWordlistForUsers(name, surname, passPol):
    f = open(f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt", "w", encoding="utf-8")
    
    patterns = [name, surname, name[0], surname[0], myLower(name[:4])] + anti_vowel(name) + anti_vowel(surname)
        
    words = mix2(patterns, passPol)

    for i in patterns:
        unidecoded = unidecode(i)
        if unidecoded != i:
            for j in myCombination(unidecoded):
                words.append(j)
        for j in myCombination(i):
            words.append(j)
    
    removeSameItems(words, name)
    removeSameItems(words, surname)
    words = list(set(words))

    for word in words:
        word = ''.join(word)
        f.write(word+'\n')
    
def generatePopup(gui, text):
    tk = gui_.tk
    popup = tk.Toplevel()
    label = tk.Label(popup, text="{}".format(text))
    popup.title("Warning!")
    label.pack(padx=20, pady=20)
    button = tk.Button(popup, text="Ok", command=popup.destroy)
    button.pack(pady=10)
    gui.eval(f'tk::PlaceWindow {str(popup)} center')

def generate(domainName, year, name, surname, passPol, wifiPol):

    if  wifiPol:
        additionalNames = [additionalName.strip() for additionalName in gui_.entry_additionalName.get().split(",")]
        additionalNames.append(domainName)

        arr = []
        words = []

        for j in additionalNames:
            unidecoded = unidecode(j)
            if unidecoded != j:
                arr.append(unidecoded)
            for i in anti_vowel(j):
                unidecoded = unidecode(i)
                if unidecoded != i:
                    arr.append(unidecoded)
                arr.append(i)

        arr += additionalNames

        arr = list(set(arr))

        combinations = list(product(arr, repeat=2))

        for i in additionalNames:
            removeSameItems(combinations, i)
        
        f = open("wifi.txt", "a", encoding="utf-8")

        currentYear = datetime.today().year
        s1 = [year  for year in range(currentYear-2, currentYear+1)]
        s2 = ['0' + str(num) if num < 10 else num for num in range(1,100)] #+ [('0' + str(num))*2 if num < 10 else num*2 for num in range(1,100)]
        s3 = [serie for serie in generateNumberSeries(9) ]
        s4 = [(str(i)+str(i+1)+str(i+2))*2  for i in range(8)]
        s5 = [str(i)+str(i+1)+str(i+2)+str(i+2)+str(i+1)+str(i) for i in range(8) if i < 8]
        s6 = [str(i)+str(i+1)+str(i+2)+str(i+2+3)+str(i+2+2)+str(i+2+1) for i in range(8) if i < 5]
        s7 = [str(i)*2+str(i+1)*2+str(i+2)*2 for i in range(8)]

        for combination in combinations:
            print(combination)
            o = 'x' + combination[0]+'x' + combination[1] + 'x'
            for leet in generateLeetSpeakCombinations(o):
                for specialChar in generateSpecialCharSeries(2):
                    if len(specialChar) == 1:
                       for suffix in s1:
                           words += myReplace(leet, 'x', specialChar, suffix)
                        
                       for word in words:
                           f.write(word+'\n')

                    if len(specialChar) == 2:
                        for suffix in s1+s2+s3+s4+s5+s6+s7:
                            words += myReplace(leet, 'x', specialChar, suffix)
                        for word in words:
                            f.write(word+'\n')
    
    fname = f"{ROOT_DIR}\\raw-files\\w-{domainName}.txt"
    
    if domainName != "":
        if not path.isfile(fname):
            generateWordlistForDomain(domainName, passPol)
            rule_1(passPol, 0, None, None, domainName)
            rule_2(year, passPol, 0, None, None, domainName)
            rule_3(passPol, 0, None, None, domainName)
            rule_4(passPol, 0, None, None, domainName)
        else:
            generatePopup(gui_.gui, "The Wordlist for {} has already done!".format(domainName))
    
    fname = f"{ROOT_DIR}\\raw-files\\w-general.txt"
    
    if name != "" and surname != "":
        if not path.isfile(fname):
            generateGeneralCommonPasswords(passPol)
            rule_1(passPol, 1)
            rule_2(year, passPol, 1)
            rule_3(passPol, 1)
            rule_4(passPol, 1) 
            rule_5(passPol, 0)

        fname3 = f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt"
        
        if not path.isfile(fname3):
            generateWordlistForUsers(name, surname, passPol)
            rule_1(passPol, 2, name, surname)
            rule_2(year, passPol, 2, name, surname)
            rule_3(passPol, 2, name, surname)
            rule_4(passPol, 2, name, surname)
            rule_5(passPol, 2, name, surname)
            rule_6(passPol, name, surname)
        else:
            generatePopup(gui_.gui, "The Wordlist for {} {} has already done!".format(name, surname))

    filenames = ['{}\\output\\o-{}-{}.txt'.format(ROOT_DIR, name,surname), '{}\\output\\o-{}.txt'.format(ROOT_DIR, domainName), '{}\\output\\o-general.txt'.format(ROOT_DIR)]
    with open('{}\\output\\all-output.txt'.format(ROOT_DIR), 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)            
    
    generatePopup(gui_.gui, "The Wordlist for is created!")
            
def generateNumberSeries(*args):
    argLen = len(args) 
    if argLen >  1:
        min = args[0]
        max = args[1]
        if min == max:
            word = ''
            for i in range(1,max+1):
                word += str(i)
            else:
                return word
    else:
        min = 1
        max = args[0]
    rule = ''

    for i in range(min, max):
        rule += f"{i}("

    rule += str(max)

    for i in range(min, max):
        rule += ")?"

    return list(exrex.generate(rule))

def find_duplicate_names(file_path):

    seen_names = set()
    duplicate_names = set()

    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip()
            if name in seen_names:
                duplicate_names.add(name)
            else:
                seen_names.add(name)

    return duplicate_names

def removeSameItems(arr, word):
    wordlist = []
    string = ''.join(word)
    for i in [string, string[0], string[:4]] + anti_vowel(string):
        for j in myCombination(i):
            unidecoded = unidecode(j)
            if unidecoded != j:
                wordlist.append(unidecoded)
            wordlist.append(j)
    else:
        for i in list(product(wordlist, repeat=2)):
            try:
                arr.remove(i)
            except:
                continue

def on_entry_click(event):
    entry = gui_.entry_additionalName
    if entry.get() == gui_.placeholder:
        entry.delete(0, "end")  
        entry.config(fg='green')  

def on_focus_out(event):
    entry = gui_.entry_additionalName
    if entry.get() == '':
        entry.insert(0, gui_.placeholder)
        entry.config(fg='#343333')     

def labelVisibility(wifi, label, entry):
    if wifi:
        label.grid(row=4,column=0, sticky="w")
        entry.grid(row=4,column=1, sticky="w")
        gui_.gui.geometry("{}x{}".format(gui_.width, gui_.height))
    else:
        label.grid_forget()
        entry.grid_forget()
        gui_.gui.geometry("{}x{}".format(gui_.width, gui_.height-25))
    
