import time
import requests as rq
import bs4 as bs4
import re


def download_search_page(query, page):
    """Will return html code with many video links"""
    url = "https://www.youtube.com/results?search_query={query}&sp=CAI%253D&p={page}"
    urll = url.format(query=query, page=page)
    print(urll)
    response = rq.get(urll)

    return response.text


def download_video_page(link):
    """Will return html code from a specific video"""
    url = "https://www.youtube.com{link}"
    urll = url.format(link=link)
    response = rq.get(urll)

    link_name = re.search("v=(.*)", link).group(1)

    return response.text


def parse_search_page(page_html):
    """Apply BS4 on specific video page, extract some tags and return a video list with their attr"""
    parsed = bs4.BeautifulSoup(page_html)

    tags = parsed.findAll("a")

    video_list = []

    for e in tags:
        if e.has_attr("aria-describedby"):
            link = e['href']
            title = e['title']
            data = {"link": link, "title": title}
            video_list.append(data)
    return video_list

#TODO: Refactor parse_video_page function.
def parse_video_page(page_html):
    """Will return a dict with all info to be shown at main page"""
    parsed = bs4.BeautifulSoup(page_html, 'html.parser')

    class_watch = parsed.find_all(attrs={"class": re.compile(r"watch")})
    id_watch = parsed.find_all(attrs={"id": re.compile(r"watch")})
    channel = parsed.find_all("a", attrs={"href": re.compile(r"channel")})
    meta = parsed.find_all("meta")

    data = dict()

    for e in class_watch:
        colname = "_".join(e['class'])
        if "clearfix" in colname:
            continue
        data[colname] = e.text.strip()

    for e in id_watch:
        colname = e['id']
        # if colname in output:
        #    print(colname)
        data[colname] = e.text.strip()

    for e in meta:
        colname = e.get('property')
        if colname is not None:
            data[colname] = e['content']

    for link_num, e in enumerate(channel):
        data["channel_link_{}".format(link_num)] = e['href']

    return data
