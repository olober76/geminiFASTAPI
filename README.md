# SL2 Indonesia AI Candidate Test_Duta Kukuh Pribadi

## Getting Started

1. Generate API on Gemini AI first to get API KEY, Then insert it inside the code on **`gemAPIfast.py`**
2. Build the docker image : Run the following command in the directory containing your Dockerfile

```Powershell
    docker build -t [NAME IMAGE] .

```

3. Run the Docker Container : After the image is built, run the container using

```Powershell
    docker run -d -p 8000:80 fastapi-google-genai
```

4. if success, you can try to make text generation based on Gemini API, the only parameters used are

- **Prompt**: to make question
- **Temperature**: controls the creativity and randomness generated text (input from 0 to 1, must be float)
- **max_output_tokens** : controls the maximum number of tokens (input from 1 to 1000, must be int)
  the command that can use

```Powershell
curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt":"WRITE_PROMPT_HERE","temperature":INSERT_TEMP_HERE,"max_output_gitokens":INSERT_TOKENS_HERE}'

```

## Explanation

### Asynchronous API Calls

The benefits of using asynchronous calls in the code above are:

1. Concurrency: Asynchronous calls allow the program to perform multiple tasks concurrently. In this case, the `generate_text_async` function can handle multiple requests simultaneously.

2. Non-Blocking I/O: Asynchronous calls enable non-blocking I/O operations, which means that the program doesn't wait for the completion of an I/O operation (e.g., network request) before moving on to the next task.

3. Easier Error Handling: Asynchronous calls can make error handling easier, as errors can be propagated and handled more easily using try-except blocks and error handling mechanisms like HTTPException.

In the provided code, the benefits of asynchronous calls are evident in the following:

- The `generate_text_async` function uses `asyncio` and `aiohttp` to make asynchronous calls to the Google Generative AI API.
- The FastAPI endpoint uses async and await to handle incoming requests asynchronously.
- The tenacity library is used to implement retry logic with exponential backoff, which is particularly useful in asynchronous programming.
- By leveraging asynchronous calls, the code can handle multiple requests efficiently, provide faster response times, and improve the overall user experience.

### Parameter Tuning:

1. **Prompt**: This is the input text that the model uses as a starting point to generate new text.

- Effect on generated text: The prompt has a significant impact on the generated text. It sets the tone, style, and direction of the generated text.

2. **Temperature**: his parameter controls the creativity and randomness of the generated text (0 to 1).

- Effect on generated text: The temperature parameter affects the level of randomness and creativity in the generated text. A higher temperature can result in more interesting and varied text, but it can also lead to less coherent or relevant text. A lower temperature can result in more predictable and coherent text, but it may lack creativity and diversity.

example using **low temperature**

The command :

```powershell
curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt":"Write about balarama dead","temperature":0.1,"max_tokens":250}'

```

The output :

```powershell
"generated_text":"Balarama died of a snakebite."
```

if we are using **high temperature**

```powershell
curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt":"Write about balarama dead","temperature":0.9,"max_tokens":250}'
```

The output :

```powershell
"generated_text":"Balarama is killed by a hunter while he is sleeping in the forest. The hunter mistakes Balarama for a deer and shoots him with an arrow. Balarama dies instantly.\n\nBalarama's death is a great tragedy for the Yadavas. He is a beloved brother to Krishna and a respected leader of the Yadava clan. His death is a sign that the end of the Yadavas is near.\n\nAfter Balarama's death, Krishna leads the Yadavas to Kurukshetra, where they fight a great battle against the Kauravas. In the end, the Yadavas are all killed, and Krishna is the only one left alive.
```

3. **Max Output Tokens**: This parameter controls the maximum number of tokens (words or characters) in the generated text.

- Effect on generated text: The max output tokens parameter affects the length and complexity of the generated text. A higher value can result in more detailed and elaborate text, while a lower value can result in shorter and more concise text.

example using **low max_output_tokens**

The command :

```powershell
curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt":"Write about greece history","temperature":0.5,"max_tokens":100}'

```

The output :

```powershell
"generated_text":"Greece has a long and rich history dating back over 3,000 years. The first major civilization in Greece was the Minoan civilization, which flourished on the island of Crete from around 2700 to 1450 BC. The Minoans were a seafaring people who traded with other civilizations around the Mediterranean Sea. They built large palaces and had a sophisticated writing system.\n\nThe Minoan civilization was destroyed by a volcanic eruption around 1450"
```

example using **High max_output_tokens**

The command :

```powershell
curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"prompt":"Write about greece history","temperature":0.5,"max_tokens":950}'
```

The output :

```powershell
"generated_text":"Greece has a long and rich history dating back over 3,000 years. The first major civilization in Greece was the Minoan civilization, which flourished on the island of Crete from around 2700 to 1450 BC. The Minoans were a seafaring  ... every year."
```

(**Note** : The text was too long)

### Backend Integration

he code above integrates the `generate_text_async` function into a FastAPI app, creating a REST API endpoint to handle user requests. This function is then integrated into the FastAPI app by defining a POST endpoint `/generate` that accepts a JSON request with the input parameters prompt, temperature, and `max_output_tokens`. The endpoint uses the generate_text_async function to generate text based on the input parameters and returns the generated text, candidates, filters, and safety feedback in a JSON response.

The code too actualizes blunder dealing with and appropriate reaction designing. It employments try-except pieces to capture any special cases that will happen amid the execution of the 'generate_text_async' work or the handling of the client ask. In the event that an special case happens, it raises an HTTP exemption with a status code of 500 and a detail message that incorporates the mistake message. Also, the code performs essential approval on the input parameters, checking that the incite isn't purge, the 'temperature' is between and 1, and the 'max_output_tokens' is between 1 and 1000. In the event that any of these conditions are not met, it raises an HTTP exemption with a status code of 400 and a detail message that incorporates the mistake message. This guarantees that the API endpoint returns a well-formatted reaction with a clear blunder message in case of any mistakes or invalid input.

### Docker Integration

Utilizing Docker for arrangement of the FastAPI application gives a few benefits, counting steady and reproducible situations, segregation, and adaptability. Docker typifies the application and its conditions into a holder, guaranteeing that it runs reliably over distinctive situations, from improvement to generation, without issues related to contrasting framework arrangements or lost conditions. This confinement too improves security by keeping the application environment partitioned from the have framework. Besides, Docker disentangles scaling and overseeing different occasions of the application, making it less demanding to handle shifting loads and coordinated with coordination instruments like Kubernetes. Generally, Docker streamlines the arrangement prepare, decreases setup time, and upgrades the unwavering quality of the application.
