import openai
from config import openaitoken
openai.api_key = openaitoken

def chat_request(request):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a chatbot"},
                    {"role": "user", "content": request},
                ]
        )
        return ''.join([choice.text for choice in response.choices])
    except Exception as e:
        print(f'Error: {str(e)}')
        return 'что то сломалось, хз что вообще'