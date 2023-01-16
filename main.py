import requests
import bs4

pokemon = str(input('Escreva o nome do Pokemón '))
pokemonURL = 'https://www.pikalytics.com/pokedex/gen9vgc2023series1/' + pokemon.lower()

def getPokemonMove1(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#moves_wrapper > div > div:nth-child(1) > div:nth-child(1)')
        return elems[0].text.strip()
    except:
        print('Pokémon não encontrado')
def getPokemonMove2(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#moves_wrapper > div > div:nth-child(2) > div:nth-child(1)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonMove3(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#moves_wrapper > div > div:nth-child(3) > div:nth-child(1)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonMove4(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#moves_wrapper > div > div:nth-child(4) > div:nth-child(1)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonItem(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#items_wrapper > div > div:nth-child(1) > div:nth-child(2)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonAbility(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#abilities_wrapper > div > div:nth-child(1) > div:nth-child(1)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonNature(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(1)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonEVHP(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(2)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonEVATK(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(3)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonEVDEF(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(4)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonEVSPATK(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(5)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonEVSPDEF(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(6)')
        return elems[0].text.strip()
    except:
        pass
def getPokemonEVSPEED(pokemonURL):
    try:
        res = requests.get(pokemonURL)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('#dex_spreads_wrapper > div > div:nth-child(1) > div:nth-child(7)')
        return elems[0].text.strip()
    except:
        pass

golpe_1 = getPokemonMove1(pokemonURL)
golpe_2 = getPokemonMove2(pokemonURL)
golpe_3 = getPokemonMove3(pokemonURL)
golpe_4 = getPokemonMove4(pokemonURL)
item = getPokemonItem(pokemonURL)
habilidade = getPokemonAbility(pokemonURL)
nature = getPokemonNature(pokemonURL)
evhp = getPokemonEVHP(pokemonURL)
evatk = getPokemonEVATK(pokemonURL)
evdef = getPokemonEVDEF(pokemonURL)
evspatk = getPokemonEVSPATK(pokemonURL)
evspdef = getPokemonEVSPDEF(pokemonURL)
evspeed = getPokemonEVSPEED(pokemonURL)

print(str(pokemon.upper()) + ' @' + str(item))
print(str(golpe_1) + ' | ' + str(golpe_2) + ' | ' + str(golpe_3) + ' | ' + str(golpe_4))
print('Habilidade: ' + str(habilidade))
print('Nature: ' + str(nature))
print('EV Spread')
print(str(evhp) + '|' + str(evatk) + '|' + str(evdef) + '|' + str(evspatk) + '|' + str(evspdef) + '|' + str(evspeed))