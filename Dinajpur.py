import requests
from bs4 import BeautifulSoup
import os
import webbrowser

print("Wait! Programming Running")
if os.path.exists('index.html'):
	os.remove("index.html")
id = []
image = []

is_empty = "/img/admission/thumbnail/"

start = 1
end = 50
value = start != end
while(True):
    print("Student No: {}".format(start))
    final_link = "http://dpi.edu.bd/temp_students/view/"+str(start)
    r = requests.get(final_link)
    soup = BeautifulSoup(r.content, "html.parser")
    link = str(soup.find(class_="thumbnail")).split('"')
    image.append(link[7])
    id.append(start)
    start +=1
    if start == end:
        break
        xx = dict(zip(id,image))
        tr = []
        for id,iu in xx.items():
            tr.append('<a href="http://dpi.edu.bd/temp_students/view/{}"><img src="http://dpi.edu.bd/{}"/></a>'.format(id,iu))
            with open('index.html', 'a') as file:
                for i in tr:
                    file.write(i)
                    webbrowser.open('file://' + os.path.realpath("index.html"))
                    quit()