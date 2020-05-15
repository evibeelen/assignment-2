import pandas as pd
from googletrans import Translator
translator = Translator()
import string
printable = set(string.printable)
import os

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data.csv', sep = '\t')
data.head()


for i, j in data.iterrows():
    print(i)
    text=j['text']

    ## translation
    text_cleaned="".join(filter(lambda x: x in printable, text))
    text_nl=translator.translate(text_cleaned, dest="nl").text

    #subject indication
    school=False
    contact=False
    nursing=False
    hospitality=False
    event=False
    general=False

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
    if school== False and contact== False and nursing== False and hospitality == False and event== False:
        general=True
    data.loc[i, 'Schools'] = school
    data.loc[i, 'Contact-Based Professions'] = contact
    data.loc[i, 'Nursing homes'] = nursing
    data.loc[i, 'Hospitality'] = hospitality
    data.loc[i, 'Events'] = event
    data.loc[i, 'General'] = general

    ## Translate voor sentiment Analysis
    text_en=translator.translate(text_cleaned, dest="en").text

    ## VADER

data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

print('done!')


data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

print('done.')
