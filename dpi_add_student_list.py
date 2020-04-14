import requests
from bs4 import BeautifulSoup
import os
import webbrowser

print("Wait! Programming Running")

if os.path.exists('index.html'):  # True or False
    os.remove("index.html")

# id = []             # 300
# image = []          # 300_image

# is_empty = "/img/admission/thumbnail/"

start = 700
end = 750

value = start != end   # False

while(value):

    print("Form No: {}".format(start))

    final_link = "http://dpi.edu.bd/temp_students/view/" + str(start)

    r = requests.get(final_link)
    soup = BeautifulSoup(r.content, "html.parser")

    link = str(soup.find(class_="thumbnail")).split('"')

    image.append(link[7])
    id.append(start)
    start += 1

    if start == end:
        break
xx = dict(zip(id, image))
tr = []
for id , iu in xx.items():
    tr.append('<a href="http://dpi.edu.bd/temp_students/view/{}"><img src="http://dpi.edu.bd/{}"/></a>'.format(id, iu))
with open('index.html', 'a') as file:
    for i in tr:
        file.write(i)
    webbrowser.open('file://' + os.path.realpath("index.html"))
    quit()
