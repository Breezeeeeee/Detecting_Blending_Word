import wordfilter
import report
#read file
dictionary=open("dict.txt")
candidates=open("candidates.txt")
blends=open("blends.txt")
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



Result=open("report_3_repeat_character","w")
for token in candidatesList:
    token = token.rsplit()[0]
    if not wordfilter.filterword(token):
        resultList.append(token)

print("The percise of is: ",report.checkPercise(resultList,blendword))
print("The recall of is: ",report.checkRecall(resultList,blendword))

for wor in resultList:
    Result.write(wor)
    Result.write("\n")
resultList=[]
for token in wordList:
    token = token.rsplit()[0]
    if not wordfilter.filterword(token):
        resultList.append(token)

print("The percise of dictionary is: ",report.checkPercise(resultList,wordList))
print("The recall of dictionary is: ",report.checkRecall(resultList,wordList))
