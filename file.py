fh = open("hello.txt","r")
sentence= fh.read()
fh.close()
#a = sentence.split()
fh1=open("hii.txt","w+")
for i in range(0,len(sentence)):
    if sentence[i]=='a':
     s="\\"+sentence[i]
     fh1.write(s)
    else:
     fh1.write(sentence[i])
