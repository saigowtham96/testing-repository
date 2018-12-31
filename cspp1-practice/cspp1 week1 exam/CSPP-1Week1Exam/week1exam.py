def getimage(page):
    line = page.split("<img")
    line = line[1:]
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
def getdisplay(page):
    lines = page.split("{")
    startingtag = "background-color\""
    endtag = "\""
    list2 = []
    count = 0
    for item in lines:
        list2.append(item)
        for source in list2:
            if startingtag in source:
                first = source.index(startingtag)
                source = source[first+len(startingtag):]
                last = source.index(endtag)
                output = source[:end]
        count = count+1
        print(output)
    print(output)



        
def main():
    page = open("file.html", errors = "ignore").read()
    # print(page)
    getimage(page)
    getdisplay(page)

if __name__ == '__main__':
    main()