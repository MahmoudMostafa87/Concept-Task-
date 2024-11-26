import random as r


words=['hi','gjkl','jgh']

ranword=r.choice(words)
orword=ranword
i=5
while not i==0:
    ranword=r.shuffle(ranword)
    print(ranword)
    print(f"you have {i} from attempts")
    word=str(input("Enter your guess"))
    if(not word.isalpha() or word==""):
        print("invalid data")
        i-=1
        continue
    if(word.lower()==orword.lower()):
        print(f"you are win Congratulations {word}")
        break
    i-=1
    
if(i==0):
    print(orword)







