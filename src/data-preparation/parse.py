import json

f = open('../../gen/data-preparation/temp/public-attitudes-press-conference.json','r', encoding='utf-8')

con = f.readlines()

outfile = open('../../gen/data-preparation/temp/parsed-data.csv', 'w', encoding = 'utf-8')

outfile.write('id\tcreated_at\ttext\n')

for i in con:
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


    outfile.write(obj.get('id_str')+'\t'+obj.get('created_at')+'\t'+text+'\n')

print('done')
