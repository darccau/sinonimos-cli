import sys
import requests
from bs4 import BeautifulSoup

target_word = sys.argv[1]
full_url = "https://www.sinonimos.com.br/" + target_word

page = requests.get(full_url)

soup = BeautifulSoup(page.text, "html.parser")

raw_sinon = soup.find_all(class_="s-wrapper")

print(f"\n                                    Sinônimo de {target_word}\n")


for index in raw_sinon:
    sinon = index.text.split(":")
    sinon = sinon[0] + ":\n" + sinon[1] + "\n"

    print(sinon)
