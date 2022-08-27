## WORDLE
[WORDLE](https://www.nytimes.com/games/wordle/index.html)

## ChWordle.py
### reading tile from web and make answer (require chrome debug mode)

"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\hoge" https://www.nytimes.com/games/wordle/index.html"


## ReWordle.py  
### python script of word search for WORDLE

```
usage: ReWordle.py [/d] [rrr !rrr -word ^s s$ #cC c ...  C ...]
	options
	/d : debug print on
	/D : debug print off
	rrr: reg exp
		regex : regular exp
		!regex : not regex
		-regex : charange word
		^s : start with s
		s$ : end with s
	c  : contain c
	C  : not contain c
	#cC: c & C by string
	#Cc.Cc: 5char wordle input, "." is for exact right char
	example : ReWordle.py ^ab t$ o u R    for about
		start with "ab", end with "t", contain "o" and "u", not contain "r" 
---
$ wordle_search([/d .oven #MeRIT #ABUSe #CDXL])
--- debug on
.oven 2 ['coven', 'woven']
M 2 ['coven', 'woven']
e 2 ['coven', 'woven']
R 2 ['coven', 'woven']
I 2 ['coven', 'woven']
T 2 ['coven', 'woven']
Not .e... 0 []
A 2 ['coven', 'woven']
B 2 ['coven', 'woven']
U 2 ['coven', 'woven']
S 2 ['coven', 'woven']
e 2 ['coven', 'woven']
Not ....e 0 []
C 1 ['woven']
D 1 ['woven']
X 1 ['woven']
L 1 ['woven']
['woven']
---

### This script is using 'corncob_lowercase.txt' for dictionary file from 'http://www.mieliestronk.com/wordlist.html'.
