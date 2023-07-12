import requests
from app.models import News

def get_data():
	res = requests.get("https://webapi.autodoc.ru/api/news/1/2")

	if res.status_code == 200:
		data = res.json()
		news = News.json_parse(data["news"][0])

		return news
	else:
		return None

