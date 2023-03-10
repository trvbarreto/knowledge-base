import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/front')

soupObject = BeautifulSoup(response.text, 'html.parser')
links = soupObject.select('.titleline')
subtext = soupObject.select('.subtext')


def create_custom_hackernews(links, subtext):
    hackernews = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = vote[0].getText().replace(
                ' points', '').replace(' point', '')
            if int(points) > 500:
                hackernews.append(
                    {
                        'title': title,
                        'link': href,
                        'votes': points
                    }
                )
    return hackernews


pprint.pprint(create_custom_hackernews(links, subtext))
