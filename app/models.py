from datetime import datetime

class News:
	def __init__(self, id, title):
		self.id = id
		self.title = title


	def json_parse(json):
		id = json["id"]
		title = json["title"]

		return News(id, title)

