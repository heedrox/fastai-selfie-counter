from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from fastai.vision import *
import aiohttp

path = Path('./work-folder')
learner = load_learner(path)


async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def classify_url(request):
    url = request.query_params["url"]
    file_bytes = await get_bytes(url)
    img = open_image(BytesIO(file_bytes))
    _,_,losses = learner.predict(img)
    return JSONResponse({
        "predictions": sorted(
            zip(learner.data.classes, map(float, losses)),
            key=lambda p : p[1],
            reverse=True
        )
    })


app = Starlette(debug=True, routes=[
    Route('/classify-url', classify_url, methods=['GET']),
])