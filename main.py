import json
import uvicorn

from external_api_handler import ExternalApiHandler
from fastapi import FastAPI
from requests_and_responses import *

app = FastAPI()
ExternalApiHandler = ExternalApiHandler()

@app.get("/home")
async def get_home():
    return "HI"

@app.post("/swe_sentiment/", response_model=SvSentimentResponse)
async def get_sv_sentiment(request_data: Request):
    result = await ExternalApiHandler.get_sv_sentiment(request_data)
    return result

@app.post("/en_sentiment/", response_model=EnSentimentResponse)
async def get_en_sentiment(request_data: Request):
    result = await ExternalApiHandler.get_en_sentiment(request_data)
    return result

@app.post("/topic/", response_model=TopicResponse)
async def get_en_sentiment(request_data: Request):
    result = await ExternalApiHandler.get_topic(request_data)
    return result

@app.post("/translation/", response_model=TranslationResponse)
async def get_translation(request_data: TranslationRequest):
    result = await ExternalApiHandler.get_translation(request_data)
    return result

@app.post("/summarize/", response_model=SummarizeResponse)
async def get_summarization(request_data: Request):
    result = await ExternalApiHandler.get_summarization(request_data)
    return result

def main():
    with open("Config/app_config.json") as f:
        config = json.load(f)

    HOST = config.get("HOST")
    PORT = config.get("PORT")

    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
