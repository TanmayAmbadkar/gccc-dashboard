from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

quests = ['Explore Machine Learning Models with Explainable AI',
          'Integrate with Machine Learning APIs',
          'Engineer Data in Google Cloud',
          'Insights from Data with BigQuery',
          'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
          'Deploy to Kubernetes in Google Cloud',
          'Build and Secure Networks in Google Cloud',
          'Deploy and Manage Cloud Environments with Google Cloud',
          'Set up and Configure a Cloud Environment in Google Cloud',
          'Perform Foundational Infrastructure Tasks in Google Cloud',
          'Getting Started: Create and Manage Cloud Resources',
]



def getDetailsForProfile(url):

    try:
        r = requests.get(url)
    except:
        return -1, -1

    soup = BeautifulSoup(r.content, 'html.parser')

    name_h1 = soup.find("h1", {"class": "l-mbm"})
    labs_quests_p = soup.find("p", {"class": "public-profile__hero__details"})
    badges_divs = soup.find_all("div", {"class": "public-profile__badge"})


    if name_h1 is None:
        return -1, -1
    c=0
    for badge in badges_divs:
        b_arr = badge.text.strip().rsplit("\n")
        if b_arr[0] in quests:
            c+=1


    labs_quests = labs_quests_p.text.strip().rsplit("\n")

    return int(labs_quests[0]), c


def execute(filename='test_urls.csv'):

    print(filename)
    #try:
    data = pd.read_csv(filename)
    #except:
    #    print('Error occured')
    #    return

    i=0
    labs = []
    quests = []
    start_time = time.time()
    for i in range(len(data)):
        out = getDetailsForProfile(data['URL'][i])
        labs.append(out[0])
        quests.append(out[1])
        print(f'\r{i+1}/{len(data)}', end = '')
    print()
    data['labs']=labs
    data['quests']=quests

    diff = time.time() - start_time
    print("Finished in", int(diff/60), "min", "{:7.4f}".format(float(diff%60)), "sec")
    return data

if __name__ == '__main__':
    execute()
