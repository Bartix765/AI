import openai
import gradio
from dotenv import load_dotenv

TEMPERATURE = 0.5
MAX_TOKENS = 500
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0.6
MAX_CONTEXT_QUESTIONS = 10

openai.api_key = input("Enter api key: ")

messages = [{"role": "system"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.Image.create(
        prompt=user_input,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    ChatGPT_reply = image_url
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


if __name__ == '__main__':
    demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="AI IMAGE GENERATOR")
    demo.launch(share=True)