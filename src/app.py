import instructor # type: ignore
from flask import Flask, request
from fastapi import FastAPI
import vertexai 
import asyncio
import uvicorn
from vertexai.generative_models import GenerativeModel  
from pydantic import BaseModel

vertexai.init(project="training-projects-430617", location="us-central1")

class UserData(BaseModel):
    query: str

class UserDetail(BaseModel):
    name: str
    age: int


client = instructor.from_vertexai(
    client=GenerativeModel("gemini-1.5-pro-preview-0409"),
    mode=instructor.Mode.VERTEXAI_TOOLS,
    _async=True,
)

# note that client.chat.completions.create will also work
# resp = client.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Extract Jason is 25 years old.",
#         }
#     ],
#     response_model=User,
# )

app = FastAPI()

@app.post('/predict', response_model=UserDetail)
async def endpoint_function(data: UserData) -> UserDetail:
    user_detail = await client.chat.completions.create(
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": f"Extract: `{data.query}`"},
        ],
    )
    return user_detail
    

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')











# import vertexai
# from vertexai.preview.generative_models import GenerativeModel
# from flask import Flask, request
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("API_KEY")

# vertexai.init(project="training-projects-430617", location="us-central1")

# parameters = {
#     "temperature": 0.6,
#     "max_output_tokens": 256,
#     "top_k": 3,
#     "top_p": 0.5
# }
# model = GenerativeModel("gemini-1.5-pro-002")

# app = Flask(__name__)

# @app.route('/predict', methods= ['POST'])
# def predict():
#     model_response = model.generate_content(contents=request.get_json()['prompt'])
#     return f"{model_response.candidates[0].content.parts[0].text} Dave"

# if __name__ == "__main__":
#     app.run(port=8080, host='0.0.0.0', debug=True)
