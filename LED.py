import report

dictionary=open("/home/breeze/Downloads/2019S2-COMP90049_proj1-data/dict.txt")
candidates=open("/home/breeze/Downloads/2019S2-COMP90049_proj1-data/report_3_repeat_character")
blends=open("/home/breeze/Downloads/2019S2-COMP90049_proj1-data/blends.txt")
candidatesList=[]
wordList=[]
blendList=[]
resultList=[]
blendword = []
for token in candidates.readlines():
    token = token.rsplit()[0]
    candidatesList.append(token)
for word in dictionary.readlines():
    word = word.rsplit()[0]
    wordList.append(word)

for blend in blends.readlines():
    x=blend.split('\t')
    blendword.append(x[0])
    x[2]=x[2].rsplit()[0]
    blendList.append(x)

joResult=open("/home/breeze/Downloads/2019S2-COMP90049_proj1-data/LEDTotal.txt","w")
jaroResult = []
for token in candidatesList:

    maxDistance = -10
    maxWord =""
    similar = []
    for word in wordList:
        dis = report.localEditDistance(token, word)
        if dis>maxDistance:
            maxDistance = dis
            maxWord = word
    resultList.append((token,maxWord,maxDistance))
    print(token, maxWord, maxDistance)
    joResult.write(token)
    joResult.write(' ')
    joResult.write(str(maxDistance))
    joResult.write(' ')
    joResult.write(maxWord)
    joResult.write("\n")




joResult.close()