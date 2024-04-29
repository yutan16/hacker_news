import requests
from bs4 import BeautifulSoup
import pprint

res1 = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res)
# print(res.text)

soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup)
# print(soup.title)
# print(soup.body)
# print(soup.a)
# print(soup.find(id='score_37006082'))
# print(soup.select('.score'))  # '.' is for class
# print(soup.select('#score_37006082'))  # '#' is for specific ids

links1 = soup1.select('.titleline')
subtext1 = soup1.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')

mega_links = links1 + links2
mega_subtext = subtext1 + subtext2

# print(links[0], votes[0])
# print(links[0].get('href', None))


def sort_by_points(hnlist):
    sorted_hn = sorted(hnlist, key=lambda k: k['points'], reverse=True)
    return sorted_hn


def hn_lists(links, subtext):
    hn = []
    for index, link in enumerate(links):
        title = links[index].getText()
        href = links[index].a.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
        if points > 99:
            hn.append({'title': title, 'link': href, 'points': points})
    return sort_by_points(hn)


pprint.pprint(hn_lists(mega_links, mega_subtext))
