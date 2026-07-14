from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

documents = []

pdf_folder = "../documents"

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(pdf_folder, file))
        documents.extend(loader.load())

print(f"Loaded {len(documents)} pages")

# Configuration A
splitter_a = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks_a = splitter_a.split_documents(documents)

print("\n=== Configuration A ===")
print(f"Chunk Size: 500")
print(f"Chunk Overlap: 50")
print(f"Total Chunks: {len(chunks_a)}")

# Configuration B
splitter_b = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks_b = splitter_b.split_documents(documents)

print("\n=== Configuration B ===")
print(f"Chunk Size: 1000")
print(f"Chunk Overlap: 100")
print(f"Total Chunks: {len(chunks_b)}")