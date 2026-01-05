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
    Model: qwen/qwen3-coder-480b-a35b:free - Best for agentic coding & data analysis
    """
    openai_model_client = OpenAIChatCompletionClient(
        model="qwen/qwen3-coder-480b-a35b:free",
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
            "family": "qwen"
        }
    )
    return openai_model_client