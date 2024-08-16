import google.generativeai as genai
import asyncio
import tenacity
import os

from fastapi import FastAPI, Request, HTTPException
from aiohttp import ClientSession
from aiocache import cached, Cache
from joblib import Parallel, delayed


# Setting up in-memory caching for API responses
cache = Cache(Cache.MEMORY)

app = FastAPI()


# Configure the Google Generative AI API with API key
genai.configure(api_key="YOUR_API_KEY")

# Define an asynchronous function for generating text with retry logic and caching
@cached(ttl=3600)
@tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4, max=10), stop=tenacity.stop_after_attempt(3))
async def generate_text_async(prompt: str, temperature: float, max_output_tokens: float):
    async with ClientSession() as session:
        try:
            # Asynchronously generate text using the Google Generative AI library
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None,
                lambda: genai.generate_text(
                    prompt=prompt,
                    temperature=temperature,
                    max_output_tokens=max_output_tokens
                )
            )
            return response # Return the API response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) # Handle errors by raising an HTTP exception

# Function to process incoming requests     
def process_request(request):
    prompt = request["prompt"]
    temperature = request["temperature"]
    max_output_tokens = request["max_output_tokens"]
    return generate_text(prompt, temperature, max_output_tokens)

# Define the FastAPI endpoint for text generation
@app.post("/generate")
async def generate_text(request: Request):
    try:
        data = await request.json() # Parse the incoming JSON request

        # Extract and validate input parameters
        prompt = data.get("prompt")
        temperature = data.get("temperature") # Set the parameter for temperature
        max_output_tokens = data.get("max_output_tokens") # Set parameter for max_output_tokens

        # Basic validation
        if not prompt:
            raise HTTPException(status_code=400, detail="Prompt is required.")
        
        if not (0 <= temperature <= 1):
            raise HTTPException(status_code=400, detail="Temperature must be between 0 and 1.")
        
        if not (1 <= max_output_tokens <= 1000):
                raise HTTPException(status_code=400, detail="max_output_tokens must be between 1 and 1000.")

        
        
        # Generate text using the async function
        response = await generate_text_async(prompt, temperature, max_output_tokens)
        
        # Access the output from the response object
        generated_text = response.result
        candidates = response.candidates
        filters = response.filters
        safety_feedback = response.safety_feedback
        
        return {
            "generated_text": generated_text,
            "candidates": candidates,
            "filters": filters,
            "safety_feedback": safety_feedback
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) # # Handle errors and return an HTTP 500 response