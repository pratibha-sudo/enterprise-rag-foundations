So when a user asks a question to the system, the retrieval process begins.

The system converts the user query into a meaningful representation.
This meaning is searched against stored vectors in the vector store to find the most relevant information.

Once the related information is retrieved, the system constructs a prompt
and constrains the LLM to explain only that retrieved context to the user.
