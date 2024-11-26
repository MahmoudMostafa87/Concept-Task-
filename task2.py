

while True:
    library=[]
    casee=input("(to add book 1)(the most and least borrowed book enter 2)(average enter 3)(know unique title enter 4)(sort books enter 5)")
    if(casee==1):
        while True:
            condition=input("if you want add book enter 1 if not enter any thing")
            if(condition==1):
                book=str(input("Book Title = "))
                days=str(input("Days Borrowed = "))
                books={'book':book,'day':days}
                library.append(books)
            else:break
    elif(casee==2):
        minnum=0
        maxnum=0
        for x in library:
                if(minnum>int(x['day'])):minnum=int(x['days'])
                if(maxnum<int(x['days'])):maxnum=int(x['days'])
        print(f"most book = {maxnum}")
        print(f"least book = {minnum}")
    elif(casee==3):
            sum=0
            for x in library:
                sum+=int(x['days'])
            print(sum/len(library))
    elif(casee==4):
        unique_books=[]
        for x in library:
            unique_books.append(x['book'])
        for x in unique_books:
            if(unique_books.count(x)==1):
                break
        print(x)       
    elif(casee==5):
        library.sort(reverse=True)
        for x in library:
            print(f"Book Title {x['book']} Days Borrowed {x['days']}")
    else:
        break
