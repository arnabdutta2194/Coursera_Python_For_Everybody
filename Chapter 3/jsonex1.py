import json

data='''{
    "note": "This file contains the sample data for testing",
    "comments": [
        {
            "name": "Romina",
            "count": 97
        },
        {
            "name": "Laurie",
            "count": 97
        },
        {
            "name": "Bayli",
            "count": 90
        },
        {
            "name": "Siyona",
            "count": 90
        },
        {
            "name": "Taisha",
            "count": 88
        },
        {
            "name": "Alanda",
            "count": 87
        },
        {
            "name": "Ameelia",
            "count": 87
        },
        {
            "name": "Prasheeta",
            "count": 80
        },
        {
            "name": "Asif",
            "count": 79
        },
        {
            "name": "Risa",
            "count": 79
        },
        {
            "name": "Zi",
            "count": 78
        },
        {
            "name": "Danyil",
            "count": 76
        },
        {
            "name": "Ediomi",
            "count": 76
        },
        {
            "name": "Barry",
            "count": 72
        },
        {
            "name": "Lance",
            "count": 72
        },
        {
            "name": "Hattie",
            "count": 66
        },
        {
            "name": "Mathu",
            "count": 66
        },
        {
            "name": "Bowie",
            "count": 65
        },
        {
            "name": "Samara",
            "count": 65
        },
        {
            "name": "Uchenna",
            "count": 64
        },
        {
            "name": "Shauni",
            "count": 61
        },
        {
            "name": "Georgia",
            "count": 61
        },
        {
            "name": "Rivan",
            "count": 59
        },
        {
            "name": "Kenan",
            "count": 58
        },
        {
            "name": "Hassan",
            "count": 57
        },
        {
            "name": "Isma",
            "count": 57
        },
        {
            "name": "Samanthalee",
            "count": 54
        },
        {
            "name": "Alexa",
            "count": 51
        },
        {
            "name": "Caine",
            "count": 49
        },
        {
            "name": "Grady",
            "count": 47
        },
        {
            "name": "Anne",
            "count": 40
        },
        {
            "name": "Rihan",
            "count": 38
        },
        {
            "name": "Alexei",
            "count": 37
        },
        {
            "name": "Indie",
            "count": 36
        },
        {
            "name": "Rhuairidh",
            "count": 36
        },
        {
            "name": "Annoushka",
            "count": 32
        },
        {
            "name": "Kenzi",
            "count": 25
        },
        {
            "name": "Shahd",
            "count": 24
        },
        {
            "name": "Irvine",
            "count": 22
        },
        {
            "name": "Carys",
            "count": 21
        },
        {
            "name": "Skye",
            "count": 19
        },
        {
            "name": "Atiya",
            "count": 18
        },
        {
            "name": "Rohan",
            "count": 18
        },
        {
            "name": "Nuala",
            "count": 14
        },
        {
            "name": "Maram",
            "count": 12
        },
        {
            "name": "Carlo",
            "count": 12
        },
        {
            "name": "Japleen",
            "count": 9
        },
        {
            "name": "Breeanna",
            "count": 7
        },
        {
            "name": "Zaaine",
            "count": 3
        },
        {
            "name": "Inika",
            "count": 2
        }
    ]
}'''

info=json.loads(data)
print(info)

for items in info:
    print(items[1])
# print("Phone Number:",info["phone number"]["number"])
