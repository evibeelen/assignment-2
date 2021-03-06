import pandas as pd
from textblob import TextBlob
import os
import shutil
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data.csv', sep = '\t')
data.head()

text_s=""
x=0
for i, j in data.iterrows():
    print(i)
    text=j['text']
    #subject indication
    school=False
    contact=False
    nursing=False
    hospitality=False
    event=False
    soccer=False
    sports=False

    if "school" in text.lower() or "onderwijs" in text.lower() or "scholen" in text.lower():
        school=True
    if "kapper" in text.lower() or "contactberoep" in text.lower():
        contact=True
    if "verpleeghuis" in text.lower() or "verpleeghuizen" in text.lower():
        nursing=True
    if "horeca" in text.lower() or "restaurant" in text.lower() or "terras" in text.lower() or "kroeg" in text.lower() or "bar" in text.lower():
        hospitality=True
    if "evenement" in text.lower() or "festival" in text.lower():
        event=True
    if "betaald voetbal" in text.lower() or "eredivisie" in text.lower() or "knvb" in text.lower():
        soccer=True
    if "sporten" in text.lower() or "sportclub" in text.lower():
        sports=True

    #place in file
    data.loc[i, 'Schools'] = school
    data.loc[i, 'Contact-Based Professions'] = contact
    data.loc[i, 'Nursing homes'] = nursing
    data.loc[i, 'Hospitality'] = hospitality
    data.loc[i, 'Events'] = event
    data.loc[i, 'Paid Soccer'] = soccer
    data.loc[i, 'Sports'] = sports

    ## Translate voor sentiment Analysis
    text_s+=(text.replace("\n", " ")+"\n")
    if x==50 or i==(len(data)-1):
        dutch=TextBlob(text_s)
        text_en=dutch.translate(from_lang="nl", to="en")
        english=text_en.split("\n")
        for tweet in english:
            analyser = SentimentIntensityAnalyzer()
            out = analyser.polarity_scores(tweet)
            data.loc[(i-x), 'English'] = tweet
            data.loc[(i-x), 'Negative'] = out['neg']
            data.loc[(i-x), 'Neutral'] = out['neu']
            data.loc[(i-x), 'Positive'] = out['pos']
            data.loc[(i-x), 'Compound'] = out['compound']
            x-=1
        text_s=""
    x+=1

data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

shutil.move('../../src/data-preparation/Data_description.txt', "../../gen/data-preparation/output/")

print('done!')
