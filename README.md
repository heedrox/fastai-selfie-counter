# People in selfie counter - made with fast.ai

Returns how many people are in a selfie: 0, 1, 2, 3, 4-more

A fast.ai model trained by Jordi Martí.

Thanks to fast.ai for its courses - https://course.fast.ai/

Really practical courses for developers and anxious people like me. Really, thanks!

# Starlette

With python3:

```
python3 -m venv venv
source venv/bin/activate

pip3 install fastai
pip3 install aiohttp
pip3 install starlette
pip3 install uvicorn
```

Run it with uvicorn:
```
uvicorn index:app
```

Usage: http://127.0.0.1:8000/classify-url?url=(encoded-url)

# Google Cloud Platform
