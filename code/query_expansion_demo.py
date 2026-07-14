queries = [
    "What is RAG?",
    "Explain Chain of Thought",
    "What is ReAct?"
]

expansions = {
    "What is RAG?":
        "What is Retrieval-Augmented Generation (RAG)?",
    "Explain Chain of Thought":
        "Explain Chain-of-Thought prompting and reasoning",
    "What is ReAct?":
        "What is ReAct prompting and acting-reasoning framework?"
}

print("=== Query Expansion Demo ===\n")

for query in queries:
    print(f"Original Query: {query}")
    print(f"Expanded Query: {expansions[query]}")
    print("-" * 60)