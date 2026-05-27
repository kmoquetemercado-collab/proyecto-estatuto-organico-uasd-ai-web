from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import os
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_pinecone import Pinecone
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_openai.chat_models import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware

# Class
class ChatModel(BaseModel):
    query: str

load_dotenv()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Model
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4o")

# Vector store
index_name = "events-qa-index"

vectorstore = Pinecone(
    index_name=index_name,
    embedding=OpenAIEmbeddings(),
)

# Prompt Template
template = """
You know everything about Harley-Davidson events.
Answer the question based on the context below. The context have information about thousands of events in different countries.
The countries are written in Alpha-2, so match the country in the question with the Alpha-2 code.
If something about checkins is asked, look in the context "Checkin Count".
If something about bookmarks is asked, look in the context "Bookmark Count".

If you can't find the answer in the context then answer accordingly. Be friendly.


Context: {context}

Question: {question}
"""
# Chain
parser = StrOutputParser()
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": vectorstore.as_retriever(), "question": RunnablePassthrough()}
    | prompt
    | model
    | parser
)

# API
@app.post("/chat/")
def read_item(query: ChatModel):
    print(f"Query received: {query}")
    return chain.invoke(query.query)