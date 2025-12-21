# RAG System Flow (Enterprise View)

## Offline Phase (Indexing)
- Collect internal documents, rules, or logs
- Clean and normalize text
- Chunk content by meaning
- Convert chunks into embeddings
- Store embeddings with metadata in a vector database

## Runtime Phase (Retrieval + Generation)
- User submits a question
- Question is converted into an embedding
- Vector store is searched for top relevant chunks
- Retrieved chunks are injected into the prompt
- LLM generates an answer using only provided context
- Output is validated and returned with sources
