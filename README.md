# SL2 Indonesia AI Candidate Test_Duta Kukuh Pribadi

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

2. **Temperature**: his parameter controls the creativity and randomness of the generated text. A higher temperature value (close to 1) will result in more diverse and creative text, while a lower temperature value (close to 0) will result in more conservative and predictable text.

- Effect on generated text: The temperature parameter affects the level of randomness and creativity in the generated text. A higher temperature can result in more interesting and varied text, but it can also lead to less coherent or relevant text. A lower temperature can result in more predictable and coherent text, but it may lack creativity and diversity.

example using **low temperature**

The command :

```
curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"prompt":"Write about balarama dead","temperature":0.1,"max_tokens":250}'

```

The output :

```
"generated_text":"Balarama died of a snakebite."
```

if we are using **high temperature**

```
curl -X POST "http://127.0.0.1:8000/generate" -H "Content-Type: application/json" -d '{"prompt":"Write about balarama dead","temperature":0.9,"max_tokens":250}'
```

The output :

```
"generated_text":"Balarama is killed by a hunter while he is sleeping in the forest. The hunter mistakes Balarama for a deer and shoots him with an arrow. Balarama dies instantly.\n\nBalarama's death is a great tragedy for the Yadavas. He is a beloved brother to Krishna and a respected leader of the Yadava clan. His death is a sign that the end of the Yadavas is near.\n\nAfter Balarama's death, Krishna leads the Yadavas to Kurukshetra, where they fight a great battle against the Kauravas. In the end, the Yadavas are all killed, and Krishna is the only one left alive.

```
