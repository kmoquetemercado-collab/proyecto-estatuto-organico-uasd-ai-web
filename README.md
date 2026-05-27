# RAG Chatbot Project

This project is a Retrieval-Augmented Generation (RAG) Chatbot built using Pinecone, OpenAI, FastAPI, and Next.js. The chatbot leverages the power of Pinecone for efficient vector search and OpenAI's language model to generate responses based on retrieved documents. The frontend is developed with Next.js to provide a seamless user experience, while FastAPI is used to create the backend API for handling requests and integrating with Pinecone and OpenAI.

## Technologies Used

- **Pinecone**: For efficient vector search and document retrieval.
- **OpenAI**: To generate high-quality responses based on the retrieved documents.
- **FastAPI**: To create the backend API for handling requests and integrating with Pinecone and OpenAI.
- **Next.js**: To develop the frontend for a seamless user interface.

## Environment Variables

To run this project, you need to create a `.env` file in the root directory with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
```