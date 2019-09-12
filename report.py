def checkPercise(list1,list2):
    set1=set(list1)
    set2=set(list2)
    set3=set1 & set2
    l1 = float(len(set3))
    l2 = float(len(set1))
    return l1/l2
def checkRecall(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    set3=set1 & set2
    l1=float(len(set3))
    l2=float(len(set2))
    return l1/l2
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    if s1[0]!=s2[0] or s1[-1]!=s2[-1]:
        return 99999
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def globalEditDistance(token, word):
    editList = []
    for row in range(len(word)+1):
        editList.append([])
        for num in range(len(token)+1):
            if row == 0:
                editList[row].append((-1)*num)
            elif num==0:
                editList[row].append((-1)*row)
            elif word[row-1] == token[num-1]:
                editList[row].append(max(editList[row][num-1]-1,editList[row-1][num]-1,editList[row-1][num-1]+1))
            else:
                editList[row].append(
                    max(editList[row][num - 1] - 1, editList[row - 1][num] - 1, editList[row - 1][num - 1] - 1))

    return editList[row][num]

def localEditDistance(token, word):
    editList = []
    for row in range(len(word)+1):
        editList.append([])
        for num in range(len(token)+1):
            if row == 0:
                editList[row].append(0)
            elif num==0:
                editList[row].append(0)
            elif word[row-1] == token[num-1]:
                editList[row].append(max(editList[row][num-1]-1,editList[row-1][num]-1,editList[row-1][num-1]+1,0))

            else:
                editList[row].append(
                    max(editList[row][num - 1] - 1, editList[row - 1][num] - 1, editList[row - 1][num - 1] - 1,0))

    maxNumber = 0
    for row in range(len(word) + 1):
        if maxNumber < max(editList[row]):
            maxNumber = max(editList[row])
    return maxNumber

def NGramDistance(token, word, n):
    tokenList = []
    wordList = []
    str =""
    for i in range(0,len(token)+n-1):
        if i<n-1:
            for l in range(n-1-i):
                str+="#"
            str += token[0:i+1]
        elif i<len(token):
            str += token[i-(n-1):i+1]
        else:
            str+= token[-(n-(i-len(token)+1)):]

            for m in range(i-len(token)+1):
                str+="#"
        tokenList.append(str)
        str = ""
    for i in range(0,len(word)+n-1):
        if i<n-1:
            for l in range(n-1-i):
                str+="#"
            str += word[0:i+1]
        elif i<len(word):
            str += word[i-(n-1):i+1]
        else:
            str+= word[-(n-(i-len(word)+1)):]

            for m in range(i-len(word)+1):
                str+="#"
        wordList.append(str)
        str = ""
    set1 = set(tokenList)
    set2 = set(wordList)
    set3 = set1 & set2
    return len(wordList)+len(tokenList)-2*len(set3)