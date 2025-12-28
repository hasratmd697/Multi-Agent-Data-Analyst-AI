from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os

load_dotenv()
# OpenRouter API key
api_key = os.getenv('OPENROUTER_API_KEY')

def get_model_client():
    """
    Configure OpenAI-compatible client for OpenRouter API
    Base URL: https://openrouter.ai/api/v1
    Model: google/gemini-2.0-flash-001 (or any other OpenRouter model)
    """
    openai_model_client = OpenAIChatCompletionClient(
        model="google/gemini-2.0-flash-001",
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        max_retries=5,  # Retry on transient 500 errors
        timeout=120,    # Increase timeout for longer operations
        extra_kwargs={
            "extra_headers": {
                "HTTP-Referer": "http://localhost:8501",  # Update to your actual repo URL
                "X-Title": "Multi-Agent Data Analyst AI",
            }
        },
        model_info={
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,
            "family": "gemini"
        }
    )
    return openai_model_client