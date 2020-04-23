def wordcount(filename, listword):
	try:
		file = open(filename,"r")
		read = file.readline()
		file.close()
		for word in listword:
			lower = word.lower()
			count = 0
			for sentence in read:
				line = sentence.split()
				for each in line:
					line2 = each.lower()
					line2 = line2.strip(".,""'/?")
					if lower == line2:
						count += 1
			print(lower, ":", count)
	except FileExistsError:
		print("file doesn't exist")
wordcount("a.txt", [input("Enter the word to count:")])