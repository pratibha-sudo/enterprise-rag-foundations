# Indexing vs Retrieval in RAG

## Indexing (Offline Phase)
- Documents are cleaned and normalized
- Content is chunked by meaning
- Chunks are converted into embeddings
- Embeddings are stored in a vector database

Purpose: Prepare knowledge for efficient search.

## Retrieval (Runtime Phase)
- User question is converted into an embedding
- Vector store is searched using semantic similarity
- Top relevant chunks are fetched for the query

Purpose: Fetch the most relevant information for a specific question.
