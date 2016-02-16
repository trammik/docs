letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def mostFrequentLetter(line):
    sdd=['a']
    for letter in line:
        if letter in letters:
            fre=line.count(letter)
            if fre > line.count(sdd[0]):
                sdd.append(letter)
                sdd.remove(sdd[0])
            elif fre == line.count(sdd[0]):
                sdd.append(letter)
    sdd.sort()
    print "Most frequent letter in %s == %s" % (line,sdd[0].lower())

mostFrequentLetter("Hello World!") == "l"
mostFrequentLetter("How do you do?") == "o"
mostFrequentLetter("One") == "e"
mostFrequentLetter("Oops!") == "o"
mostFrequentLetter("AAaooo!!!!") == "a"
mostFrequentLetter("abe") == "a"
