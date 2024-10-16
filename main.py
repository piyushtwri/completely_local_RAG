#%%

import os
import utils
file_name="docs/coffee_and_health.pdf"

#%%
model="smollm"
from langchain_ollama import OllamaLLM
model=OllamaLLM(model=model)

#%%
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(file_name)
pages=loader.load_and_split()

#%%
from langchain.prompts import PromptTemplate

template = """ Answer the question asked on the basis of the context provided.
If you can not find the answer then just say "answer is not available in the given text
context : {context}
Question : {question}
"""
prompt= PromptTemplate.from_template(template=template)
# print(prompt.format(context="Here is the context", question="Here is the question"))

# %%
# define method for generating embeddings
from langchain_ollama import OllamaEmbeddings
embeddings=OllamaEmbeddings(model="smollm")

# %%
# create a vector store and get a retriever
from langchain_community.vectorstores import DocArrayInMemorySearch
vector_store=DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)
retriever=vector_store.as_retriever()
# %%
# Create a chain pipeline that can take input questions and answer them based on the context provided
from operator import itemgetter

chain = ({  "context":itemgetter("question") | retriever,
            "question":itemgetter("question")}
            |prompt|model)

# %%
# Ask questions and print the answers untill stop is entered
question="What is the pdf about?"
while question !="":
    question = input("Enter your Question:...\n")
    print(f"Response: {chain.invoke({'question':question})}")
# %%
