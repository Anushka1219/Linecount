f=open("activity.txt")
f1=f.readlines()

print("There are ", len(f1)," lines in the file")

def countwords(f1):
    
    wordcount=0
    for lines in f1:
        word=lines.split()
        wordcount=wordcount+len(word)
    print("The number of words are :",wordcount)

countwords(f1)



