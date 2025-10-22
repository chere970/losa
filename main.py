import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # load .env in project root

groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise RuntimeError("GROQ_API_KEY not set. Add it to .env or set the environment variable.")

os.environ["GROQ_API_KEY"] = groq_key  # ensure client lib can read it

llm = ChatGroq(model="llama3-70b-8192")  # Try a supported model. Alternatives: 'mixtral-8x7b-32768', 'gemma-7b-it'
response = llm.invoke("What is agentic AI?")
print(response)
