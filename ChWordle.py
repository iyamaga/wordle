import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from ReWordle import wordle_search

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r'./chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
#print(driver.title)
#print(driver.page_source)

soup = BeautifulSoup(driver.page_source, "html.parser")

#print(soup.find("div", class_="Board-module_board__lbzlf"))
#print(soup.find("div", class_="Row-module_row__dEHfN"))
#print(soup.find_all("div", class_="Tile-module_tile__3ayIZ"))
divTiles = soup.find_all("div", class_="Tile-module_tile__3ayIZ")
tiles = []
for tile in divTiles:
    tiles.append([tile.text, tile["data-state"]])
    #print(tile["data-state"])
    #print(tile.text)
x = [ tiles[x:x+5] for x in range(0, len(tiles), 5) ]
#print(x)
answer = list('.....')
rex = []
for row in x:
    if row[0][0] == '':
        break
    for i in range(5):
        if row[i][1] == 'correct':
            answer[i] = row[i][0]

if '.' in answer:
    pass
else:
    print("ANSWER is ", ''.join(answer))
    driver.quit()
    sys.exit(0)


for row in x:
    if row[0][0] == '':
        break
    check = '#'
    for i in range(5):
        if row[i][1] == 'correct':
            check = check + '.'
        elif row[i][1] == 'present':
            check = check + row[i][0]
        elif row[i][1] == 'absent':  ## yet enter  or row[i][1] == 'tbd':
            if row[i][0] in answer:
                l = list('.....')
                l[i] = row[i][0]
                rex.append('!'+''.join(l))
            else:
                check = check + row[i][0].upper()
        else:
            check = check + '?'
    rex.append(check)


#print(''.join(answer), check)
rex = ['/d', ''.join(answer)] + rex
print('$ wordle_search([' + ' '.join(rex) + '])')
print(wordle_search(rex))
driver.quit()

''' chrome remote debug mode
"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\hoge" https://www.nytimes.com/games/wordle/index.html"
'''
