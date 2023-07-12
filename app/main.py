from fastapi import FastAPI
from . import crud

app = FastAPI()

@app.get("/")
def read_news():
	data = crud.get_data()
	return data

