import json
import uvicorn

from external_api_handler import ExternalApiHandler
from fastapi import FastAPI
from requests_and_responses import *

app = FastAPI()
ExternalApiHandler = ExternalApiHandler()

#Some comment

@app.get("/home")
async def get_home():
    return "API Switch"

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
#
#def main():
#    with open("app/Config/app_config.json") as f:
#        config = json.load(f)
#
#    host = config.get("HOST")
#    port = config.get("PORT")
#
#    uvicorn.run(app, host=host, port=port)
#

#if __name__ == "__main__":
#    main()
