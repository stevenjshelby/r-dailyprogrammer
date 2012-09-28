#Python Innapropriate Word Censor
#r/dailyprogrammer
#100 intermediate

import sys, re

#define some statics
CHARS_TO_KEEP = 1
MATCH_PARTIALS = True

#the data
uncensored = sys.stdin.read()
censored = uncensored
filter = [dword.strip() for dword in open('swearWords.txt','r')]

for dword in filter:
	if not MATCH_PARTIALS:
		dword = ' ' + dword + ' '
	
	if re.search(dword,censored,flags=re.I):
		censored = re.sub(dword[CHARS_TO_KEEP:],'*' * (len(dword)-CHARS_TO_KEEP),censored,flags=re.I)

#output
print(censored)
