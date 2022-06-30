#!/usr/bin/env python
'''
    ReWordle
    2022/6/30 Ayakosan

    word search for WORDLE
'''
import re
import sqlite3
import os, sys

class edic:
    ''' read words from dic '''
    ### https://github.com/kujirahand/EJDict
    dbname = './ejdic-hand-sqlite/ejdict.sqlite3'

    def __init__(self):
        if not os.path.exists(self.dbname):
            print('dic file not found', self.dbname)
            sys.exit(0)
        self.conn = sqlite3.connect(self.dbname)

    def accessAll(self, l=5):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM items')
        #n = 0
        d = []
        for a in cur.fetchall():
            if len(a[1]) == 5:
                d.append(a[1])
                #print(a[1])
                #n = n + 1

        cur.close()

        return d

    def close(self):
        self.conn.close()

class edic2:
    ''' read words from dic '''
    ### http://www.mieliestronk.com/wordlist.html
    dbname = './corncob_lowercase.txt'

    def __init__(self):
        if not os.path.exists(self.dbname):
            print('dic file not found', self.dbname)
            sys.exit(0)

    def accessAll(self, l=5):
        d = []
        n = 0
        with open(self.dbname) as f:
            for w in f.readlines():
                n = n + 1
                w = w.strip()
                if len(w) == l:
                    d.append(w)
        # print(n)
        return d

def wordle_search(rex = ('^ab', 't$', 'o', 't', 'R'), w5 = None, debug_ = False):
    if w5 is None:
        dic = edic2()
        w5 = dic.accessAll()

    for x in rex:
        if x.startswith('-d'):
            debug_ = True
            print('--- debug on')
            continue
        if x.startswith('-D'):
            debug_ = False
            print('--- debug off')
            continue

        if x.startswith('#'):
            rex2 = list(x[1:])
            w5 = wordle_search(rex2, w5, debug_)
        else:
            sw = True
            if x.isupper():
                sw = False

            try:
                prog = re.compile(x, re.IGNORECASE)
            except Exception as e:
                print("regex error", e)
                sys.exit(-1)

            n = 0
            w = []
            for s in w5:
                ret = prog.search(s)

                if sw:
                    if ret:
                        w.append(s)
                        n = n + 1
                else:
                    if ret is None:
                        w.append(s)
                        n = n + 1
            w5 = w

            if debug_:
                if n < 10:
                    print(x, n, w5)
                else:
                    print(x, n)
    return w5

def main():
    if len(sys.argv) == 1:
        print('usage: ReWordle.py [-d] [rrr ^s s$ c ...  C ...]')
        print('\toptions')
        print('\t-d : debug print on')
        print('\t-D : debug print off')
        print('\tregex')
        print('\trrr: reg exp')
        print('\t^s : start with s')
        print('\ts$ : end with s')
        print('\tc  : contain c')
        print('\tC  : not contain c')
        print('\t#cC: c & C by string')
        print('\tex : %s ^ab t$ o u R    for about' % os.path.basename(sys.argv[0]))

        print('---')
        ##### Instant Run
        ##### Please modify list below on this source code
        #####
        ##rex = ['-d',  'ch$',  't', 'O', 'P', 'L', 'A', 'N', 'E', 'F', 'I', 'G']
        rex = ['-d',  'ch$', '#tOPLANEFIG']
        print('$ wordle_search([' + ' '.join(rex) + '])')
        print(wordle_search(rex))
        print('---')
        sys.exit(0)

    #print(sys.argv)
    print(wordle_search(sys.argv[1:]))

if __name__ == '__main__':
    main()
