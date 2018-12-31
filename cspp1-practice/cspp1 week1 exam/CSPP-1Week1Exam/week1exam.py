def getimage(word):
    line = word.split("<img")
    firsttag = "src=\""
    lasttag = "\""
    list1 = []
    count = 0
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

        
def main():
    page = open("file.html", errors = "ignore")
    print(page)
    for word in page:
        #print(word)
        getimage(page)
        # getdisplay(word)

if __name__ == '__main__':
    main()