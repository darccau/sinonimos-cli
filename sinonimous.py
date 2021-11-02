import sys
import requests
from bs4 import BeautifulSoup

target_word = sys.argv[1]
full_url = "https://www.sinonimos.com.br/" + target_word

page = requests.get(full_url)

soup = BeautifulSoup(page.text, "html.parser")

raw_sinon = soup.find_all(class_="s-wrapper")

print(f"Sinônimo de {target_word}")

for index in raw_sinon:
    sinon = index.text.split(":")
    sinon = sinon[0] + ":\n" + sinon[1] + "\n"
    # for i in range(len(sinon)):
    #    if sinon[i] == ":":
    #        sinon[i] = "\n"
    #        break
    # broken_line = sinon.find(":")
    # sinon = sinon[broken_line] "\n"

    print(sinon)
