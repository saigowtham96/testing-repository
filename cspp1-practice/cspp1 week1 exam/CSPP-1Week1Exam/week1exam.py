def getimage(page):
    line = page.split("<img")
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
    page = open("file.html", errors = "ignore").read()
    # print(page)
    getimage(page)

if __name__ == '__main__':
    main()