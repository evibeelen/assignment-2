import json

f = open('../../gen/data-preparation/temp/public-attitudes-press-conference.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('id\tcreated_at\ttext\n')

counter=0

for i in con:
    if ('{' not in i):
        continue

    obj=json.loads(i)
    try:
        text = obj.get("extended_tweet").get("full_text")
    except:
        try:
            text = obj.get("retweeted_status").get("extended_tweet").get("full_text")
        except:
            try:
                text = obj.get("quoted_status").get("extended_tweet").get("full_text")
            except:
                text = obj.get("text" )

    if "school" in text.lower() or "onderwijs" in text.lower() or "scholen" in text.lower()\
    or "kapper" in text.lower() or "contactberoep" in text.lower() or "verpleeghuis" in text.lower() \
    or "verpleeghuizen" in text.lower() or "horeca" in text.lower() or "restaurant" in text.lower() \
    or "terras" in text.lower() or "kroeg" in text.lower() or "bar" in text.lower() or "evenement" \
    in text.lower() or "festival" in text.lower() or "betaald voetbal" in text.lower() or "eredivisie" \
    in text.lower() or "knvb" in text.lower() or "sporten" in text.lower() or "sportclub" in text.lower():

        text = text.replace('\t', ' ').replace('\n', ' ').replace(';', ' ')

        outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\n')
        counter+=1
    else:
        continue

    #if counter >50:
        #break

print('done')
