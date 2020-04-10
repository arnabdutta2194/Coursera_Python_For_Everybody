import xml.etree.ElementTree as ET
data='''
<person>
    <name>Arnab</name>
    <phone type="int1">+91 7469953331</phone>
    <email hide="yes" />
</person>
'''
tree=ET.fromstring(data)
print("Name: ",tree.find('name').text)
print("Attribute: ",tree.find('email').get('hide'))
print("Attribute: ",tree.find('phone').get('type'))