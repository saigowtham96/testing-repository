def getimage(word):
	line = word.split("<img")
	firsttag = "src=\""
	lasttag = "\""
	list1 = []
	count = 0
	for i in line:
		list1.append(i)
		#print(list1)
	for temp in list1:
		if firsttag in temp:
			start = temp.index(firsttag)
			temp = temp[start+len(firsttag):]
			end = temp.index(lasttag)
			result = temp[:end]
			print(result)
			count = count+1
			print(count)


def getdisplay(word):
	starttag = "background-color\""
	endtag = "\""
	list2 = []
	list3 = []
	count = 0
	for j in lines:
		list2.append(j)
	for temp1 in list2:
		if starttag in temp:
			start = temp1.index(starttag)
			temp1 =temp1[start+len(starttag)]
			end = temp.index(lasttag)
			result1 = temp[:end]
			print(result1)
			if result1 not in list3:
				list3.add(resut1)
				count = count + 1
		print(count)




def main():
	page = open("file.html", errors = "ignore")
	print(page)
	for word in page:
		#print(word)
		getimage(word)
		#getdisplay(word)

if __name__ == '__main__':
    main()