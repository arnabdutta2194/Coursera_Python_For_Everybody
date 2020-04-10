import xml.etree.ElementTree as ET
data='''
<person>
     <users>
        <worker id="1">
            <name>Arnab</name>
            <phone type="int1">+91 7469953331</phone>
            <email hide="yes" />
        </worker>
        <worker id="2">
            <name>Ronnie</name>
            <phone type="int1">+91 756685552</phone>
            <email hide="yes" />
        </worker>
     </users>
</person>
'''
tree=ET.fromstring(data)
lst=tree.findall('users/worker')
for item in lst:
    print("Name:", item.find('name').text)
    print("Phone: ", item.find('phone').text)
    print("Attr: ", item.get('hide'))
