# main.py
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio

# CrewAI imports
from crewai import Crew, Process

# Import your agents and task
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from task import analyze_financial_document as analyze_task

# Initialize FastAPI
app = FastAPI(title="Financial Document Analyzer API")

# Function to run Crew workflow
def run_crew(query: str, file_path: str):
    # Initialize Crew with all agents and the analyze task
    financial_crew = Crew(
        agents=[financial_analyst, verifier, investment_advisor, risk_assessor],
        tasks=[analyze_task],
        process=Process.sequential
    )

    # Run workflow
    result = financial_crew.kickoff({
        "query": query,
        "file_path": file_path
    })

    return result

# Health check
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}

# Analyze PDF endpoint
@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    # Validate file
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", f"financial_document_{file_id}.pdf")

    try:
        # Save uploaded PDF
        contents = await file.read()
        if not contents:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")
        with open(file_path, "wb") as f:
            f.write(contents)

        # Clean query
        query = query.strip() if query else "Analyze this financial document"

        # Run Crew workflow in a thread to avoid blocking
        response = await asyncio.to_thread(run_crew, query, file_path)

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except HTTPException:
        raise  # Re-raise FastAPI exceptions

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing financial document: {str(e)}"
        )

    finally:
        # Safe cleanup of uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass

# Run server directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)