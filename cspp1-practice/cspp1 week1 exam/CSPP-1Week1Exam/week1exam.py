def getimage(word):
    line = word.split("<img")
    firsttag = "src=\""
    lasttag = "\""
    list1 = []
    count = 0
    result = 0
    for i in line:
        list1.append(i)
        for temp in list1:
            if firsttag in temp:
                start = temp.index(firsttag)
                temp = temp[start+len(firsttag):]
                end = temp.index(lasttag)
                result = temp[:end]
                count = count+1
            print(result)
        print(count)

def getdisplay(word):
    lines = word.split("back")
    starttag = "groundcolor\""
    endtag = "\""
    list2 = []
    counter = 0
    result1 = 0
    for j in lines:
        list2.append(j)
        for temp1 in list2:
            if starttag in temp1:
                first = temp1.index(starttag)
                temp1 = temp1[start+len(starttag)]
                last = temp1.index(endtag)
                result1 = temp[:end]
            counter = counter+1
            print(result1)
        print(counter)



        
def main():
    page = open("file.html", errors = "ignore")
    print(page)
    for word in page:
        #print(word)
        getimage(word)
        getdisplay(word)

if __name__ == '__main__':
    main()