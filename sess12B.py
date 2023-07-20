contacts = [
    {
        "name":"jonnathan",
        "phone": "21334 24563",
        "conversation":[
            "Hi",
            "Hi",
            "This is an awesome day",
            "Let's go and play"
        ]
    },
     {
        "name":"Fionna",
        "phone": "33333 44444",
        "conversation":[
            "Hi",
            "hello",
            "Who are you?",
            "pta nahi?"
        ]
    },{
        "name":"George",
        "phone": "55555 44444",
        "conversation":[
            "Hi",
            "Hi",
            "This is an awesome day",
            "OK"
        ]
    }
]

search_keyword = input("enter keyword to search:- ")

for contact in contacts:
    if contact["name"].lower().__contains__(search_keyword.lower()) or contact["phone"].__contains__(search_keyword):
        print(contact)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
