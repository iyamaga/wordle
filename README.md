# wordle

ReWordle.py    word search for WORDLE

usage: ReWordle.py [-d] [^s s$ c ...  C ...]
	options
	-d : debug print on
	-D : debug print off
	regex
	^s : start with s
	s$ : end with s
	c  : contain c
	C  : not contain c
	ex : ReWordle.py ^ab t$ o u R    for about
---
$ wordle_search([-d W A U I -D d o r l])   ### search for 2022/6/28 wordle "audio/world/droll"
--- debug on
W 3898
A 2336
U 1728
I 997
--- debug off
['droll', 'drool', 'lords', 'older']
---


This script is using 'corncob_lowercase.txt' for dictionary file from 'http://www.mieliestronk.com/wordlist.html'.
