from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
y_combinator_webpage = response.text

soup = BeautifulSoup(y_combinator_webpage, "html.parser")
article_tags = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in article_tags:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_point_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_point_index])
print(article_links[max_point_index])


# Below is a practice code to learn scraping on a smaller html page
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# #Accessing the tile
# print(soup.title.string)
#
# # Accessing all the anchor tags
# anchor_tags = soup.find_all(name="a")
# for tags in anchor_tags:
#     print(tags.get("href"))
#     print(tags.getText())
#
# # Accessing through attributes
# heading = soup.find(name="h1", id="name")
# print(heading.getText())



