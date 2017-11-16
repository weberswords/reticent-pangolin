from bs4 import BeautifulSoup
from xml.sax.saxutils import escape
from email import utils
from dateutil import parser

import urllib
import datetime
import time


def get_posts(url):
	url = urllib.urlopen(url).read()
	soup = BeautifulSoup(url, "html.parser")
	body = soup.find_all('div', attrs={"class": "toc-body"})
	posts = soup.find_all('a', class_="cp-toc-item body-toc-item row-two-image row-three-image")
	return posts

def get_post_containers(post):
	return post.find_all("div", attrs={"class": "adjustment-container"})

def get_formatted_post_date(date):
	today = datetime.datetime.today()
	if "days" in date:
		days = int(filter(str.isdigit, str(date)))
		post_date = today - datetime.timedelta(days=days)
	else:
		post_date = parser.parse(date)

	post_tuple = post_date.timetuple()
	post_stamp = time.mktime(post_tuple)
	return utils.formatdate(post_stamp)

def get_post_link(post):
	base = "http://www.hoodlumcultured.com"
	link = post['href']
	return base + link

def get_post_data(post):
	containers = get_post_containers(post)
	date_category_list = containers[0].string.split("|")
	date = date_category_list[1].strip()
	date = get_formatted_post_date(date)
	link = get_post_link(post)
	category = date_category_list[0].strip()
	title = escape(containers[1].string)
	if len(containers) <= 2:
		description = ''
	else:
		description = containers[2].string

	new_post_object = {'title': title, 'date': date, 'category':category, 'description':description, 'link': link}
	return new_post_object

def add_posts_to_xml(posts):
	xml = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?><rss version=\"2.0\" xmlns:atom=\"http://www.w3.org/2005/Atom\"><channel><atom:link href=\"http://websonthewebs.com/hoodlums/rss.xml\" rel=\"self\" type=\"application/rss+xml\" /><title>UpdatED</title><link>http://www.hoodlumcultured.com</link><description>The latest from The Intelligent Hoodlums</description>"
	for post in posts:
		new_post_object = get_post_data(post)
		xml += "<item><guid>"+ new_post_object['link'] +"</guid><title>" + new_post_object['title'] + "</title><pubDate>" + new_post_object['date'] + "</pubDate><category>" + new_post_object['category']+"</category><link>" + new_post_object['link'] + "</link><description>" + new_post_object['description']+"</description></item>"

	xml += "</channel></rss>"
	return xml


with open('rss.xml', 'w+') as rss:
	posts = get_posts('http://www.hoodlumcultured.com')
	xml = add_posts_to_xml(posts)
	rss.write(xml.encode('utf8'))
	rss.close()
