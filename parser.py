import bs4
import requests
import re
import json


# thank you unicde-table so much!
url = 'https://unicode-table.com/ru/sets/krasivye-bukvy/'


content = requests.get(url).content

soup = bs4.BeautifulSoup(content)


letters = list(
    filter(
        lambda l: re.match("Буква \w", l.text),
        soup.find_all("h3", {"class": "character-list__subtitle"}),
    )
)

dct = {}
for letter_obj in letters:
    options = list(map(lambda li: li.find('a')['data-symbol'], letter_obj.parent.find("ul").find_all("li")))
    letter = re.search('Буква (\w)', letter_obj.text).group(1)
    dct[letter] = options

json_dict = json.dumps(dct, indent=4)

with open('letters.py', 'w') as f:
    f.write(f"""LETTERS_DICT = {json_dict}""")
