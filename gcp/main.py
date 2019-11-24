from fastai.vision import *
from google.cloud import storage
from flask import Response
import aiohttp

storage_client = storage.Client()
bucket = storage_client.get_bucket("fastai-gcp-model")
blob = bucket.blob("export.pkl")
blob.download_to_filename("/tmp/export.pkl")

learner = load_learner("/tmp", "export.pkl")


async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


async def classify(request):
    url = request.args["url"]
    file_bytes = await get_bytes(url)
    img = open_image(BytesIO(file_bytes))
    _, _, losses = learner.predict(img)
    return Response(
        json.dumps({
            "predictions": sorted(
                zip(learner.data.classes, map(float, losses)),
                key=lambda p: p[1],
                reverse=True
            )
        }),
        mimetype="application/json"
    )
