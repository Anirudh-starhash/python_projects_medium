from bs4 import BeautifulSoup

# with open("D:\\nitw\\academics\\demo_py\\bs4-start\\website.html",encoding="utf8") as f:
#     c=f.read()
    
# soup=BeautifulSoup(c,'html.parser')
# # print(soup.title)
# # print(soup.prettify())

# # anchor_tags=soup.find_all(name="a")
# # for tag in anchor_tags:
# #     print(f"Text = {tag.getText()}")
# #     print(f"href = {tag.get("href")}")
    
# # print(soup.find(name="h1",id="name"))

# # print(soup.find(name="h3",class_="heading"))

# # print(soup.select_one(selector="#name"))

# # print(soup.select_one(selector="p a"))

# # print(soup.select_one(selector=".heading"))

import requests

response=requests.get("https://news.ycombinator.com/")
response.raise_for_status()
soup=BeautifulSoup(response.text,"html.parser")
# print(soup)

x=soup.select(selector=".titleline a")
article_texts=[]
article_links=[]
for y in x:
    text=y.getText()
    article_texts.append(text)
    link=y.get("href")
    article_links.append(link)
    
article_upvotes=[int(x.getText().split()[0]) for x in soup.select(selector=".score")]

largest_number=max(article_upvotes)
largest_index=article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])


    
    