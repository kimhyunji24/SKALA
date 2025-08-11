from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyMuPDFLoader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import tiktoken
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 1. PDF 파일 로딩
loader = PyMuPDFLoader("/app/docs/AI용어정리.pdf") 
docs = loader.load()

# 2. 문서 분할
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splits = splitter.split_documents(docs)

# 3. 임베딩 및 벡터 DB 구성
db = FAISS.from_documents(splits, OpenAIEmbeddings())
retriever = db.as_retriever()

# 4. Retrieval QA 체인 생성
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-4o"),
    retriever=retriever
)

# 5. 질문 처리 함수
def run_qa(query: str) -> str:
    return qa.run(query)
