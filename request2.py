book={}
book['tom']={
    'name':'tom',
    'address':'up kanpur',
    'phone':99564321
}
book['bob']={
    'name':'tom',
    'address':'up kanpur',
    'phone':99564321
}
import json
s=json.dumps(book)
with open("book.txt","w")as f:
    f.write(s)

# f=open("book.txt","r")
# s=f.read()
# print(s)



# import requests
# import json
# a=requests.get("http://saral.navgurukul.org/api/courses")
# print(a)

# b=a.json()
# print(b)



