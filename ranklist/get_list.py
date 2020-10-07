from bs4 import BeautifulSoup
import requests
import pandas as pd

def getDetailsForProfile(url):

    try:
        r = requests.get(url)
    except:
        return -1, -1

    soup = BeautifulSoup(r.content, 'html.parser')

    name_h1 = soup.find("h1", {"class": "l-mbm"})
    labs_quests_p = soup.find("p", {"class": "public-profile__hero__details"})

    if name_h1 is None:
        return -1, -1


    labs_quests = labs_quests_p.text.strip().rsplit("\n")

    return int(labs_quests[0]), int(labs_quests[3])


def execute(filename):

    print(filename)
    try:
        data = pd.read_csv(filename)
    except:
        print('Error occured')
        return
    i=0
    labs = []
    quests = []
    for i in range(len(data)):
        out = getDetailsForProfile(data['URL'][i])
        labs.append(out[0])
        quests.append(out[1])
        print(f'\r{i+1}/{len(data)}', end = '')
    print()
    data['labs']=labs
    data['quests']=quests
    print(data)
    return data

if __name__ == '__main__':
    execute()
