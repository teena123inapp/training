def scramble(w):
  if len(w)<3:
      return w
  first = w[:1]
  last = w[-1:]
  mid = w[1:-1]

  if last == '.' or last ==',' or last =="'":
    last = w[-2:]
    mid = w[1:-2]
  return str(first) + str(middle(mid)) + str(last)

def middle(w):
    if len(w) == 1:
        return w

    else:
     half = int(len(w) / 2)
     first = w[:half][::-1]
     last = w[half:len(w)][::-1]


    return str(first + last)[::-1]



fh=open("source.txt","w+")
fh.write("Scrambling words is very interseting . Because even if they are scrambled , it doesn't impact our reading . If you don't beleive it , scramble this file and read again . Sounds surprising , isn't it . Because we don't read letter by letter , we read the whole word as a whole . ")
fh.close()
fh1=open("source.txt","r+")
sentence =fh1.read()
fh2=open("destination.txt","w+")
for line in sentence:
    sentence1 = sentence.strip()
    new =""
    for word in sentence1.split(" "):
        new += scramble(word)+" "
fh2.write(new)
fh1.close()
fh2.close()

