import io
from fastapi import FastAPI, Request
from image_handler import NodeMcuAIImageHandler
from ai import Resnet50, Resnet152
from PIL import Image

app = FastAPI()


@app.post('/upload')
async def process_image(request: Request):
    # Get the raw data from the request
    raw_bytes = await request.body()
    image_handler = NodeMcuAIImageHandler(Image.open(io.BytesIO(raw_bytes)), Resnet152())
    response = {'message': {'isWasteBiodegradable': image_handler.get_type_of_waste().value == 'Biodegradable'}}
    print(response)
    return response
