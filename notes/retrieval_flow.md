When a user asks a question, the retrieval process begins.

The system converts the user query into a meaningful representation and searches it against stored vectors in the vector store to identify the most relevant information.

Once relevant context is retrieved, the system constructs a prompt and constrains the LLM to generate an answer using only that retrieved information.

However, the system must also handle cases where the requested information is not found in the vector store or when the retrieved results are very weak.

In such scenarios, the system should fall back gracefully by responding with messages such as “I do not have enough information to answer this accurately” or by asking the user for clarification.

This fallback behavior is essential to prevent hallucination and confident guessing. Providing generic or ungrounded answers breaks user trust and defeats the core purpose of RAG, which is to generate reliable responses grounded in trusted data.
