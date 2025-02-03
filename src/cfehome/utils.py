from openai import OpenAI
from django.conf import settings
import openai

OPENAI_KEY=getattr(settings,'OPENAI_SECRET_KEY')
client=OpenAI(api_key=OPENAI_KEY)
def get_response(prompt):
 try:
    response=client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'developer','content':'You are a helpful assistant'},
            {'role':'user','content':prompt}
        ],
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        

    )
    
    return response

      
 except openai.OpenAIError as e:
            print(f" Error - {e}")
            return {"error": "API request failed after multiple attempts"}
