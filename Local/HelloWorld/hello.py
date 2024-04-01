from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
import os


# Load environment variables from the .env file
load_dotenv()

# Get the model and URL value from the .env file
model = os.getenv("OLLAMA_MODEL")
base_url = os.getenv("BASE_URL")
print("Ollama Model: " + model)
print("Ollama URL: " + base_url)

llm = ChatOllama(model=model, base_url=base_url, format="json", temperature=0)

from langchain_core.messages import HumanMessage

messages = [
    HumanMessage(
        content="What color is the sky at different times of the day? Respond using JSON"
    )
]

chat_model_response = llm.invoke(messages)
print(chat_model_response)