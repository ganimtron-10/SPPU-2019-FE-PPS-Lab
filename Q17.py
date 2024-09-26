"""
Aledutron
SPPU 2019 FE PPS Lab
SPPU First Year (FE) Programming and Problem Solving (PPS) Lab Assignments (2019 Pattern)
Youtube PPS Playlist Link: https://youtube.com/playlist?list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&si=5RWSN_MmtX1FACb1

Problem Statement:
Q17
To count total characters in file, total words in file, total lines in file and frequency of given word in file.

Explaination Video Link: https://www.youtube.com/watch?v=TKbvMdzczr0&list=PLlShVH4JA0osTzddxh-2s1yaigpyp6DRx&index=18&pp=iAQB
"""

# To count total characters in file, total words in file, total lines in file and frequency of
# given word in file.

file = open('FE-PPS-LAB/input.txt','r')

content = file.read()

charcount = len(list(content))

print("Charcount: ", charcount)


numofline = len(content.split('\n'))

print("Line Count: ", numofline)

words = content.split(' ')

for i in range(len(words)):
	if '\n' in words[i]:
		# words = words + words[i].split('\n')
		# words.remove(words[i])
		sepratewords = words[i]
		words.remove(words[i])
		words = words + sepratewords.split('\n')

wordcount = len(words)

print("Word Count: ", wordcount)


wordfreq = {}

for i in words:
	if wordfreq.get(i):
		wordfreq[i] += 1
	else:
		wordfreq[i] = 1

print("Word Frequency: ",wordfreq)
