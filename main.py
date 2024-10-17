#%%
# Import necessary libraries
import os
import utils
file_name = "docs/coffee_and_health.pdf"  # Define the PDF file to process

#%%
## very Important : The ollama must be installed and running on your computer for local rag to work
# Initialize the model
ollama_model_name = "smollm" # ollama3
vector_store_name="InMemoryVectorStore"
from langchain_ollama import OllamaLLM
model = OllamaLLM(model=ollama_model_name)  # Load the specified model

#%%
# Load the PDF and split into pages
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(file_name)  # Load the PDF file using PyPDFLoader
pages = loader.load_and_split()  # Split PDF into individual pages

#%%
# Define the prompt template for generating responses based on context
from langchain.prompts import PromptTemplate

# Prompt template with instructions on how to answer based on provided context
template = """ Answer the question asked on the basis of the context provided.
If you cannot find the answer, then just say "answer is not available in the given text."
context : {context}
Question : {question}
"""
prompt = PromptTemplate.from_template(template=template)

# %%
# Define method for generating embeddings
from langchain_ollama import OllamaEmbeddings
embeddings = OllamaEmbeddings(model=ollama_model_name)  # Initialize embeddings with the specified model

# %%
# Create a vector store and set up a retriever for contextual search
if vector_store_name=="InMemoryVectorStore":
    from langchain_core.vectorstores import InMemoryVectorStore
    vector_store = InMemoryVectorStore.from_texts(pages, embedding=embeddings,)
else:
    from langchain_community.vectorstores import DocArrayInMemorySearch
    vector_store = DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)  # Create vector store from pages


retriever = vector_store.as_retriever()  # Set up retriever to search within vector store
# retrieved_documents = retriever.invoke("What is LangChain?")

# %%
# Create a chain pipeline that takes questions as input and provides context-based answers
from operator import itemgetter
chain = ({
    "context": itemgetter("question") | retriever,  # Retrieve context based on question
    "question": itemgetter("question")               # Pass question as input
} | prompt | model)  # Use the prompt and model for generating answers

# %%
# Ask questions until an empty string is entered, and print the response
question = "What is the pdf about?"  # Initial question to start with
while question != "":
    question = input("Enter your Question:...\n")  # Ask the user for a question
    print(f"Response: {chain.invoke({'question': question})}")  # Print the model's response
# %%
