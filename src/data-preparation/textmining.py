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
    school=0
    contact=0
    nursing=0
    hospitality=0
    event=0
    general=0
    if "school" in text.lower() or "onderwijs" in text.lower() or "scholen" in text.lower():
        school=1
    if "kapper" in text.lower() or "contactberoep" in text.lower():
        contact=1
    if "verpleeghuis" in text.lower() or "verpleeghuizen" in text.lower():
        nursing=1
    if "horeca" in text.lower() or "restaurant" in text.lower() or "terras" in text.lower() or "kroeg" in text.lower() or "bar" in text.lower():
        hospitality=1
    if "evenement" in text.lower() or "festival" in text.lower():
        event=1
    if (school+contact+nursing+hospitality+event) == 0:
        general+=1
    data.loc[i, 'Schools'] = school
    data.loc[i, 'Contact-Based Professions'] = contact
    data.loc[i, 'Nursing homes'] = nursing
    data.loc[i, 'Hospitality'] = hospitality
    data.loc[i, 'Events'] = event
    data.loc[i, 'General'] = general
    text_en=translator.translate(text_cleaned, dest="en").text

    ## VADER

data.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

print('done!')


data.to_csv('../../gen/data-preparation/output/dataset.csv', index = False)

print('done.')
