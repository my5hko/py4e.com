import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Mykhailo</name>
  <phone type="intl">
     +380 67 505 4259
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text) # type: ignore
print('Phone type:', tree.find('phone').get('type')) # type: ignore
print('Phone:', tree.find('phone').text.lstrip()) # type: ignore