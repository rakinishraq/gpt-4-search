import gpt_4_search as backend

try:
    output = backend.run("What is the latest GPT news?")
    if backend.references:
        print("\n**References:**")
    backend.show_references()
except Exception as e:
    print(f"`Error: {str(e)}`")