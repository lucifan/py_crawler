import requests
import time
from bs4 import BeautifulSoup

# req = requests.get('http://baozoumanhua.com/qutu?page=1')
# soup = BeautifulSoup(req.text, 'lxml')

starttime = time.time()

for i in range(100):
	pertime = time.time()
	print('=====================page{}=====================').format(i+1)
	url = 'http://baozoumanhua.com/qutu?page={}'.format(i+1)
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'lxml')
	for content in soup.find_all(attrs={"class": "article-content"}):
		if content.find(attrs={"class": "multiple-article-wrapper"}):
			continue
		if content.find('img'):
			print(content.find('img').get('data-original-image-url'))
	print(time.time()-pertime)

print('total time cost: ', time.time()-starttime)