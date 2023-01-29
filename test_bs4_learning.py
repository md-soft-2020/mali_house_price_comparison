import requests
from bs4 import BeautifulSoup 

# Download the web page
url = "https://www.bamako-immobilier.com/Location_Appartements.html"
page = requests.get(url)

# Create a BeautifulSoup class to parse the page.
soup = BeautifulSoup(page.text, "html.parser")

# best (lisible) way read the HMTL code of the page
# print(soup.prettify())

# annonces titles
annonce = soup.find_all(class_= "line mt1")
a_titles = [a.get_text() for a in annonce]

# appartement locations 
step1 = soup.find_all(class_= "row1")
temp1 = []
a_locations1 = []
for i in range(len(step1)):
    step2 = step1[i].find_all(class_= "col w10 txtcenter pa1")
    temp1 = [x.get_text(strip= True) for x in step2]
    a_locations1 = a_locations1 + temp1

# step1 = soup.find_all(class_= "row0")
# temp2 = []
# a_locations2 = []
# for i in range(len(step1)):
#     step2 = step1[i].find_all(class_= "col w10 txtcenter pa1")
#     temp2 = [x.get_text(strip= True) for x in step2]
#     a_locations2 = a_locations2 + temp2

print(a_locations1)
print("##############")
# print(a_locations2)


