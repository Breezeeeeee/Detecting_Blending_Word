import editdistance
import textdistance
import wordfilter
import report
'''
def checkSpell(token, word):
    if abs(len(token)-len(word))>1:
        return False
    elif abs(len(token)-len(word)==1):

    else:
        i = 0
        mismatch = 0
        while i<len(token):
            i+=1
            if mismatch>2:
                return False
            if token[i]!=word[i]:
                mismatch+=1
        if mismatch==1:
            
        elif mismatch==2:

        else:
            return False
'''
#read file
dictionary=open("dict.txt")
candidates=open("report_3_repeat_character")
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


recordFlag=True
Result=open("report_3_spell_mistake","w")
for token in candidatesList:
    for word in wordList:
        if abs(len(token)-len(word))>1:
            continue
        elif report.globalEditDistance(token,word)>=(min(len(token),len(word))-1):
            print("error spell: ",token,word)
            recordFlag=False
            break;

    if recordFlag==True:
        resultList.append(token)
    else:
        recordFlag=True
for wor in resultList:
    Result.write(wor)
    Result.write("\n")
print("The percise of is: ",report.checkPercise(resultList,blendword))
print("The recall of is: ",report.checkRecall(resultList,blendword))