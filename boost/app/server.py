from fastapi import FastAPI
from langserve import add_routes
from rag_chroma import chain as rag_chroma_chain

app = FastAPI()

add_routes(app, rag_chroma_chain, path="/rag-chroma")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
