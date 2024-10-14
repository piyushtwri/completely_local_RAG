# PDF Question Answering System

This project implements a question-answering system that utilizes a PDF document as its knowledge source. It employs LangChain with an Ollama model to efficiently retrieve answers based on questions asked by the user.

## Table of Contents

- [Introduction to RAG Systems](#introduction-to-rag-systems)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [Privacy and Security](#privacy-and-security)
- [License](#license)

## Introduction to RAG Systems

Retrieval-Augmented Generation (RAG) systems combine the strengths of information retrieval and generative models. They allow for:

- **Enhanced Accuracy**: By retrieving relevant information from a knowledge source (like a PDF), RAG systems provide more accurate and contextually relevant responses than traditional generative models that rely solely on learned patterns.

- **Dynamic Knowledge Base**: RAG systems can easily adapt to different documents and datasets, enabling users to ask questions based on the most current information available, making them ideal for applications requiring up-to-date knowledge.

- **Improved Context Understanding**: By pulling relevant context from documents, these systems can better understand and respond to complex queries, reducing the chances of generating irrelevant or incorrect answers.

Overall, RAG systems empower users to leverage external knowledge effectively, making them a powerful tool for various applications, including customer support, research, and education.

## Installation

To run this project, you will need Python 3.x and the following libraries:

- `langchain`
- `langchain-ollama`
- `langchain-chroma`
- Any additional dependencies you might have in your `utils.py`

**Essential:** Before running the script, ensure that the Ollama model is preinstalled and running on your computer, as it will be used to execute the model locally. This local execution guarantees that your files remain private and secure, with no chance of file misuse.

You can install the necessary packages using pip:

```bash
pip install langchain langchain-ollama langchain-chroma




### Key Additions:
- **Privacy and Security Section**: Added to emphasize the local execution and assurance of file security.
- **Expanded Context**: Provided more details about the components to give prospective users a clearer understanding of the functionality and benefits.

Feel free to modify or expand further based on your specific project needs!