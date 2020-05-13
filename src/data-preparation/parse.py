import json

f = open('../../gen/data-preparation/temp/public-attitudes-press-conference.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('id\tcreated_at\ttext\tscholen\tcontactberoep\tverpleeghuis\thoreca\tevenementen\n')

for i in con:
    school=0
    contact=0
    verpleeg=0
    horeca=0
    evenement=0
    if ('{' not in i):
        continue
    obj=json.loads(i)
    try:
        text = obj.get("retweeted_status").get("extended_tweet").get("full_text")
    except:
        try:
            text = obj.get("extended_tweet").get("full_text")
        except:
            try:
                text = obj.get("quoted_status").get("extended_tweet").get("full_text")
            except:
                text = obj.get("text" )
    text = text.replace('\t', ' ').replace('\n', ' ').replace(';', ' ')
    if "school" in text.lower() or "onderwijs" in text.lower() or "scholen" in text.lower():
        school=1
    if "kapper" in text.lower() or "contactberoep" in text.lower():
        contact=1
    if "verpleeghuis" in text.lower() or "verpleeghuizen" in text.lower():
        verpleeg=1
    if "horeca" in text.lower() or "restaurant" in text.lower() or "terras" in text.lower() or "kroeg" in text.lower() or "bar" in text.lower():
        horeca=1
    if "evenement" in text.lower() or "festival" in text.lower():
        evenement=1

    outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\t'+str(school)+'\t'+str(contact)+'\t'+str(verpleeg)+'\t'+str(horeca)+'\t'+str(evenement)+'\n')

print('done!')
