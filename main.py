# import json
import os
# from pathlib import Path

import uvicorn
from decouple import config
from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, UploadFile
from ocr import image_to_text
base_path = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

@app.post('/image_to_text')
def get_text_from_image(image):
    text = image_to_text(image)
    return{"response": text}


@app.post("/upload_image", status_code=200, tags=["Recipt Scanner"])
def upload_image(request: Request, file: UploadFile):
    return {"response": file.filename}



tags_metadata = [
    {
        "name": "Recipt Scanner",
        "description": "This End point used to extract the text information form Image",
    }
]

description = """
Recipts Scanning API 🚀
"""


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Recipts Scanning API",
        version="V-0.0.0",
        description=description,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    app.openapi_tags = tags_metadata
    return app.openapi_schema


app.openapi = custom_openapi


if __name__ == "__main__":
    # $ uvicorn main:app --reload
    port = config("FASTAPI_LOCAL_PORT", cast=int)
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload="True")