import requests
import sqlite3

con = sqlite3.connect('test25.db')

con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("""
 CREATE TABLE IF NOT EXISTS Tabela (
 NUMER VARCHAR NOT NULL,
 DRUZYNA VARCHAR (30) NOT NULL,
 MECZE INT NOT NULL,
 PUNKTY INT NOT NULL,
 Z INT NOT NULL,
 R INT NOT NULL,
 P INT NOT NULL,
 BRAMKI VARCHAR (10) NOT NULL ) """)

page = requests.get('http://ekstraklasa.org/rozgrywki/tabela/ekstraklasa-2')

# Extract the content
c = page.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(c, 'html.parser')

# print(soup.prettify())

# find results within table
table = soup.find('table')
results = table.find_all('tr')

# create and write headers to a list
header = []
header.append(['NUMER','DRUZYNA', 'MECZE', 'PUNKTY', 'Z', 'R', 'P', 'BRAMKI'])


print('Lista:\n')

# loop over results
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue

# write columns to variables
    DRUZYNA = data[3].getText(strip=True)

    print(DRUZYNA)

team = input('\nProszę wybrać drużynę z listy: ')


for result in results:
# find all columns per result
    data = result.find_all('td')
# check that columns have data
    if len(data) == 0:
            continue

# write columns to variables
    NUMER = data[0].getText(strip=True)
    DRUZYNA = data[3].getText(strip=True)
    MECZE = data[4].getText(strip=True)
    PUNKTY = data[5].getText(strip=True)
    Z = data[6].getText(strip=True)
    R = data[7].getText(strip=True)
    P = data[8].getText(strip=True)
    BRAMKI = data[9].getText(strip=True)

    MECZE = int(MECZE)
    PUNKTY = int(PUNKTY)
    Z = int(Z)
    R = int(R)
    P = int(P)

    if team == DRUZYNA:

        cur.execute("INSERT INTO Tabela VALUES(?, ?, ?, ?, ?, ?, ?, ?)",(NUMER, DRUZYNA, MECZE, PUNKTY, Z, R, P, BRAMKI))

        cur.execute("""
        SELECT * FROM Tabela
        """)
        
        wynik = cur.fetchall()

        wynik = cur.fetchall()
        for Tabela in wynik:
            print(Tabela[NUMER],Tabela [DRUZYNA], Tabela [MECZE], Tabela [PUNKTY],  Tabela [Z], Tabela [R], Tabela [P], Tabela [BRAMKI])
  
            con.commit()
            con.close()

        print('Twój zespół to: \n')

        print(NUMER, DRUZYNA, MECZE, PUNKTY, Z, R, P, BRAMKI)

        con.commit()
        con.close()










