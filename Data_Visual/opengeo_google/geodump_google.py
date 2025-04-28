import sqlite3
import json
import codecs

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if len(js['results']) == 0: continue

    # getting the id of the place of locality type to filter out the results with country type
    id = [i for i in range(0, len(js['results'])) if js['results'][i]['address_components'][0]['types'][0] == 'locality'] 

    # using the first id to get information about the place
    try:
        lat = js['results'][id[0]]['geometry']['location']['lat']
        lng = js['results'][id[0]]['geometry']['location']['lng'] 
        where = js['results'][id[0]]['formatted_address']
        # lat = js['features'][0]['geometry']['coordinates'][1]
        # lng = js['features'][0]['geometry']['coordinates'][0]
        # where = js['features'][0]['properties']['display_name']
        where = where.replace("'", "")
    except:
        print('Unexpected format')
        print(js)

    try :
        print(where, lat, lng) # type: ignore

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']" # type: ignore
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

