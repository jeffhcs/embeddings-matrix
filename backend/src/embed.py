import cohere
import os
from dotenv import find_dotenv, load_dotenv
import openai

load_dotenv(find_dotenv())

co = cohere.Client(os.environ['COHERE_API_KEY'])
openAi = openai.OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
  
)

def embed_single(text):
    print('Embedding text...')
    response = co.embed(
        texts=[text],
        model='embed-english-v3.0',
        input_type='search_query'
    )
    return response.embeddings[0]

def embed(texts, model):
    assert model in ['cohere', 'openai'], 'Invalid model'
    if model == 'cohere':
        response = co.embed(
            texts=texts,
            model='embed-english-v3.0',
            input_type='classification'
        )
        return response.embeddings
    else:
        response = openAi.embeddings.create(
            input=texts,
            model='text-embedding-ada-002',
        )
        return [i.embedding for i in response.data]