from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import uvicorn

# Import the APIs
from apis.doc_processor_api import analyze_document
from apis.fin_api_m2 import UserProfile, AllocationAdvice, get_percentage_prediction_and_normalize
from apis.rag_api import FinancialAdvisor, KnowledgeBaseLoader, Config

app = FastAPI(
    title="FinSightAI Unified API",
    description="Combined API for document processing, financial advice, and RAG-based assistance",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modify this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Document Processor API routes
app.post("/docs/analyze/")(analyze_document)

# Financial Advisor API routes
@app.post("/finance/allocate/", response_model=AllocationAdvice)
async def get_allocation_advice(profile: UserProfile):
    return await get_percentage_prediction_and_normalize(profile)

# RAG API routes
@app.post("/rag/query/")
async def query_rag(question: str):
    try:
        config = Config()
        kb_loader = KnowledgeBaseLoader(config)
        vector_db = kb_loader.load()
        advisor = FinancialAdvisor(config, vector_db)
        response = await advisor.get_response(question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main_api:app", host="0.0.0.0", port=8000, reload=True)