# pylint: disable = unidiomatic-typecheck, missing-module-docstring, line-too-long, too-many-lines, no-name-in-module, import-error, multiple-imports, pointless-string-statement, wrong-import-order, invalid-name, unspecified-encoding, missing-function-docstring, redefined-outer-name, f-string-without-interpolation, no-else-return, no-else-break, bare-except
import re
import difflib
import os
print(f"{os.path.getsize('words.txt')/1e+6} GB")
words_file = open("words.txt", "r")
words = words_file.read().lower()
words_array = words.split('\n')
regex = re.compile('[^a-zA-Z ]')
limit = 85
def scan(word_list_rray) -> str | list:
    accurates = [] # for duplicates
    most_accurate = ""
    for word_ in word_list_rray:
        print("Scanning...")
        word_sub = regex.sub(' ', word_)
        k = word_sub.split(' ')
        spelt_correct = len(k)
        for i in m:
            print("Digging..")
            if not i.lower() in words:
                print("Finding..")
                spelt_correct -= 1
        if get_word_accuracy(word_) >= limit:
            print("Gold!")
            most_accurate = word_
            accurates.append(word_)
        else:
            #TODO: make better algorithm ong
            #print(spelt_correct/len(m) * 100)
            print("Dirt!")
    if len(accurates) > 1:
        print("Diamonds!")
        return accurates #list
    else:
        print("Steel!")
        return most_accurate #string

def get_word_accuracy(word_str: str) -> int:
    word_str_subbed = regex.sub(' ', word_str)
    m = word_str_subbed.split(' ')
    curr = len(m)
    for i in m:
        if not i.lower() in words:
            print("Calculating..")
            curr -= 1
    return curr/len(m)*100
while True:
    f = input()
    if f == "?b":
        break
    elif f.startswith("?sl ") and len(f.split(' ')) == 2:
        try:
            limit = int(f.split(' ')[1])
        except:
            print("Something went wrong setting scan percentage limit.")
    else:
        f_subbed = regex.sub(' ', f)
        m = f_subbed.split(' ')
        iterations = []
        words_spelt_correctly = len(m)
        for i in m:
            if not i.lower() in words:
                similar_word = difflib.get_close_matches(i, words_array)
                if len(similar_word) >= 1:
                    print(
                        '\n' + i + " is spelled incorrectly! Did you mean "
                        + similar_word[0] + "?\n")
                    print("All possible words:\n")
                    for similar in similar_word:
                        print(similar + "\n")
                    iterations.append(f.replace(i, similar_word[0]))
                else:
                    print(i + " is spelled incorrectly! No similar words found.")
                words_spelt_correctly -= 1
        str_to_print = str(words_spelt_correctly/len(m) * 100) + \
            "% of words were spelt correctly!"
        print(str_to_print)
        # index = len(iterations)-1 if len(iterations) > 0 else len(iterations)
        result = scan(iterations)
        if type(result) is str:
            print(f"Correct {'sentence' if len(result.split(' ')) > 1 else 'word'} would be: {result} *(Scan Result Percentage: {str(get_word_accuracy(result))}%)")
        elif type(result) is list:
            for res in result:
                print(f"Correct sentence #{str(result.index(res)+1)}: {res} *(Scan Result Percentage: {str(get_word_accuracy(res))}%)")
        