from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

while True:
    query = input("\nAsk a question (or type exit): ")

    if query.lower() == "exit":
        break

    docs = db.similarity_search(query, k=3)

    print("\nTop Results:\n")

    for i, doc in enumerate(docs, 1):
        print(f"Result {i}:")
        print(doc.page_content[:500])
        print("-" * 50)