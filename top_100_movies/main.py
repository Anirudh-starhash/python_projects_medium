from bs4 import BeautifulSoup
import requests
response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
soup=BeautifulSoup(response.text,'html.parser')


movies=soup.select(selector="h3.title")
movie_names=[]
for x in movies:
    name=x.getText()
    movie_names.append(name)

movies=movie_names[::-1]

with open("D:\\nitw\\academics\\demo_py\\top_100_movies\\movies.txt","w",encoding="utf-8") as f:
    for movie in movies:
        f.write(f"{movie}\n")
    
    
