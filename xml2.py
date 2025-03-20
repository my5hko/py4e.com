import xml.etree.ElementTree as ET

input = '''
<animals>
    <dogs>
        <dog age="5">
            <id>001</id>
            <name>Bert</name>
        </dog>
        <dog age="3">
            <id>002</id>
            <name>Archi</name>
        </dog>
    </dogs>
</animals> '''

animals = ET.fromstring(input)
dogs = animals.findall('dogs/dog')

print('Dogs number:', len(dogs))

for dog in dogs:
    print('Name: ', dog.find('name').text, ', ', 'Age: ', dog.get('age'), sep='') # type: ignore