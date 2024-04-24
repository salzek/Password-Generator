from variables import specialChars
import exrex, functions
from datetime import datetime
from helper import myMix
from variables import ROOT_DIR

MIN_PASS_LEN = 6
PASSWORD_LEN = 12
MIN_YEAR = datetime.today().year - 1
MAX_YEAR = MIN_YEAR  + 2



def rule_1(passPol, user_or_domain_or_commonPasswords, name=None, surname=None, domainName=None):
    wordlist = []
    
    if user_or_domain_or_commonPasswords == 0:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{domainName}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{domainName}.txt", "a", encoding="utf-8")
    elif user_or_domain_or_commonPasswords == 1:
        f = open(f"{ROOT_DIR}\\raw-files\\w-general.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-general.txt", "a", encoding="utf-8")
    else:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{name}-{surname}.txt", "w", encoding="utf-8")

    for word in f.readlines():
        word = word.rstrip('\n')
        numberOfSeries = functions.generateNumberSeries(9,9)

        for i in range(MIN_PASS_LEN, PASSWORD_LEN):
            fark =  i - len(word)
            if fark <= 0:
                continue

            for w in range(0, 9 - fark + 1):
                string = numberOfSeries[w:w+fark]

                if not passPol:
                    wordlist += myMix(word, string) + myMix(word, string[::-1]) if int(string) > 10 and (int(string)/int(string[::-1])) != 1 else myMix(word, string)
                
                for specialChar in specialChars:
                    wordlist += myMix(word, string, specialChar) + myMix(word, string[::-1], specialChar) if int(string) > 10 and (int(string)/int(string[::-1])) != 1 else myMix(word, string, specialChar)
            
            if fark == 1:
                continue
            for j in range(0,10):
                numberOfSeries2 = ''.join(list(exrex.generate(str(j)+"{"+str(fark)+"}")))
                if not passPol:
                    wordlist += myMix(word, numberOfSeries2)
                for specialChar in specialChars:
                    wordlist += myMix(word, numberOfSeries2, specialChar) + myMix(word, numberOfSeries2, specialChar, specialChar)
        
    else:
        for i in wordlist:
            f2.write(i+'\n')

    #duplicates = functions.find_duplicate_names("o-user.txt")
    #print("Tekrarlanan isimler:", duplicates)

def rule_2(birthday, passPol, user_or_domain_or_commonPasswords, name=None, surname=None, domainName=None, RAW_DIR=None, OUTPUT_DIR=None):
    wordlist = []

    if user_or_domain_or_commonPasswords == 0:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{domainName}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{domainName}.txt", "a", encoding="utf-8")
    elif user_or_domain_or_commonPasswords == 1:
        f = open(f"{ROOT_DIR}\\raw-files\\w-general.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-general.txt", "a", encoding="utf-8")
    else:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{name}-{surname}.txt", "a", encoding="utf-8")

    for word in f.readlines():
        word = word.rstrip('\n')
        yearRange = list(range(MIN_YEAR, MAX_YEAR)) + [birthday] if birthday else range(MIN_YEAR, MAX_YEAR)
        
        for year in yearRange:
            year = str(year)

            if not passPol:
                wordlist +=  myMix(word, year)
            if user_or_domain_or_commonPasswords == 1 and len(word+year) > 12:
                continue
            for specialChar in specialChars:
                wordlist +=  myMix(word, year, year, specialChar)+myMix(word, year, specialChar, specialChar)+myMix(word, year, specialChar)
    else:
        for i in wordlist:
            f2.write(i+'\n')

def rule_3(passPol, user_or_domain_or_commonPasswords, name=None, surname=None, domainName=None, RAW_DIR=None, OUTPUT_DIR=None):
    wordlist = []

    if user_or_domain_or_commonPasswords == 0:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{domainName}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{domainName}.txt", "a", encoding="utf-8")
    elif user_or_domain_or_commonPasswords == 1:
        f = open(f"{ROOT_DIR}\\raw-files\\w-general.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-general.txt", "a", encoding="utf-8")
    else:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{name}-{surname}.txt", "a", encoding="utf-8")

    for word in f.readlines():
        word = word.rstrip('\n')
        for i in range(0,100):
            i = str(i)
            if int(i) < 10:
                i = '0' + i
            
            if not passPol:
                wordlist += myMix(word, i)

            for specialChar in specialChars:
                wordlist += myMix(word, i, specialChar) + myMix(word, i, i, specialChar) + myMix(word, i, specialChar, specialChar) + myMix(word, i, specialChar * 3)
    else:
        for i in wordlist:
            f2.write(i+'\n')

def rule_4(passPol, user_or_domain_or_commonPasswords, name=None, surname=None, domainName=None, RAW_DIR=None, OUTPUT_DIR=None):
    wordlist = []

    if user_or_domain_or_commonPasswords == 0:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{domainName}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{domainName}.txt", "a", encoding="utf-8")
    elif user_or_domain_or_commonPasswords == 1:
        f = open(f"{ROOT_DIR}\\raw-files\\w-general.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-general.txt", "a", encoding="utf-8")
    else:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{name}-{surname}.txt", "a", encoding="utf-8")

    for word in f.readlines():
        word = word.rstrip('\n')
        for i in range(1,13):
            if i < 10:
                i = '0' + str(i)
            for j in range(1,31):
                if j < 10 :
                    j = '0' + str(j)
                
                date_ = ''.join((str(j),str(i)))

                if not passPol:
                    wordlist +=  myMix(word,date_)

                for specialChar in specialChars:
                    wordlist += myMix(word, date_, specialChar, specialChar)
    else:
        for i in wordlist:
            f2.write(i+'\n')

def rule_5(passPol, user_or_domain_or_commonPasswords, name=None, surname=None, RAW_DIR=None, OUTPUT_DIR=None):
    wordlist = []

    if user_or_domain_or_commonPasswords == 0:
        f = open(f"{ROOT_DIR}\\raw-files\\w-general.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-general.txt", "a", encoding="utf-8")
    else:
        f = open(f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt", "r", encoding="utf-8")
        f2 = open(f"{ROOT_DIR}\\output\\o-{name}-{surname}.txt", "a", encoding="utf-8")

    for word in f.readlines():
        word = word.rstrip('\n')

        for i in range(8):
            sequenceNumber = str(i)+str(i+1)+str(i+2)
            doubleSequenceNumber = str(i)*2+str(i+1)*2+str(i+2)*2
            if i < 8:
                reverseSequenceNumber = str(i+2)+str(i+1)+str(i)
                if not passPol:
                    wordlist += myMix(word,sequenceNumber,reverseSequenceNumber)
                for specialChar in specialChars:
                    wordlist += myMix(word,sequenceNumber,reverseSequenceNumber, specialChar)+myMix(word,sequenceNumber+reverseSequenceNumber, specialChar, specialChar)
            if i < 5:
                reverseNumber = str(i+2+3)+str(i+2+2)+str(i+2+1)
                if not passPol:
                    wordlist += myMix(word,sequenceNumber,reverseNumber)

                for specialChar in specialChars:
                    wordlist += myMix(word,sequenceNumber,reverseNumber,specialChar)+myMix(word,sequenceNumber+reverseNumber,specialChar, specialChar)
            
            if not passPol: 
                wordlist += myMix(word, sequenceNumber, sequenceNumber)+myMix(word,doubleSequenceNumber)
            for specialChar in specialChars:
                wordlist += myMix(word, sequenceNumber, sequenceNumber, specialChar)+myMix(word,doubleSequenceNumber, specialChar)+myMix(word, sequenceNumber, sequenceNumber, specialChar, specialChar)+myMix(word,doubleSequenceNumber, specialChar, specialChar)
    else:
        wordlist  = list(set(wordlist))
        for i in wordlist:
            f2.write(i+'\n')            

def rule_6(passPol, name, surname):
    f = open(f"{ROOT_DIR}\\raw-files\\w-{name}-{surname}.txt", "r", encoding="utf-8")
    f2 = open(f"{ROOT_DIR}\\output\\o-{name}-{surname}.txt", "a", encoding="utf-8")
    
    for word in f.readlines():
        wordlist = []
        word = word.rstrip('\n')
        if len(word) > 2:
            continue
        for day in range(1,32):
            day = str(day)
            if int(day) < 10:
                day = '0' + day
            for month in range(1,13):
                month = str(month)
                if int(month) < 10:
                    month = '0' + month
                for year in range(70,100):
                    year = str(year)
                    if not passPol:
                        wordlist += myMix(word, day+month+year)
                    for specialChar in specialChars:
                        wordlist += myMix(word, day+month+year, specialChar) + myMix(word, day+month+year, specialChar, specialChar)
                for year in range(0, int(str(datetime.today().year)[2:])):
                    year = str(year)
                    if int(year) < 10 :
                        year = '0' + year
                    if not passPol:
                        wordlist += myMix(word, day+month+year)
                    for specialChar in specialChars:
                        wordlist += myMix(word, day+month+year, specialChar) + myMix(word, day+month+year, specialChar, specialChar)
        else:
            for i in wordlist:
                f2.write(i+'\n')  