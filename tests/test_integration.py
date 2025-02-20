import requests
import asyncio
import pytest

pytest_plugins = ('pytest_asyncio',)

@pytest.mark.asyncio
async def test_integration_model_returns_correct_information():
    url = 'https://cicd-example-456176258602.us-central1.run.app/predict'
    data = '''{"query":"This has nothing to do with anything, but there is a man named Harvey, and he just turned 40."}'''
    response = requests.post(url, data=data)
    assert response.json()["name"] == "Harvey"
    assert response.json()["age"] == 40