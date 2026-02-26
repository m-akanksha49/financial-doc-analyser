# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.

## Step 1

### Install Required Libraries
```sh
pip install -r requirement.txt
```

# You're All Not Set!
🐛 **Debug Mode Activated!** The project has bugs waiting to be squashed - your mission is to fix them and bring it to life.

Ah! I see — GitHub Markdown tables sometimes break if the content is long or contains line breaks. We can fix it **by keeping each cell concise** and using `|` properly, or we can **use collapsible sections** for readability.

Here’s a clean **table-friendly version** of your bugs & fixes, formatted for GitHub so it renders properly:

---

## 🐛 Bugs Found & Fixed

### Deterministic Bugs (Code Crashes / Wrong Behaviour)

| #  | File             | Bug                                               | Fix                                                                                                 |
| -- | ---------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 1  | tools.py         | `from crewai_tools import tools` — invalid export | Removed; `SerperDevTool` already imported directly                                                  |
| 2  | tools.py         | Duplicate `SerperDevTool` import via deep path    | Replaced with single correct top-level import                                                       |
| 3  | tools.py         | `Pdf` used but never imported → NameError         | Imported `PyPDFLoader` and replaced `Pdf(file_path=path).load()` with `PyPDFLoader(path).load()`    |
| 4  | tools.py         | `async def read_data_tool` — must be synchronous  | Converted to `@staticmethod` synchronous method                                                     |
| 5  | tools.py         | Same async issue on other tools                   | Converted `analyze_investment_tool` & `create_risk_assessment_tool` to synchronous `@staticmethod`s |
| 6  | agents.py        | Wrong import path for Agent                       | Changed to `from crewai import Agent, LLM`                                                          |
| 7  | agents.py        | `llm = llm` undefined → NameError                 | Proper instantiation using `LLM(model=..., api_key=...)` with env vars                              |
| 8  | agents.py        | `tool=[...]` wrong keyword                        | Changed to `tools=`                                                                                 |
| 9  | agents.py        | `max_iter=1` fails complex tasks                  | Increased to `max_iter=5`                                                                           |
| 10 | agents.py        | `max_rpm=1` → extreme throttling                  | Raised to `max_rpm=10`                                                                              |
| 11 | main.py          | Import overwriting: `analyze_financial_document`  | Renamed import: `from task import analyze_financial_document as analysis_task`                      |
| 12 | main.py          | Null-check after `.strip()` → AttributeError      | Moved validation before `.strip()`                                                                  |
| 13 | requirements.txt | `python-multipart` missing → 422 error            | Added `python-multipart==0.0.9`                                                                     |
| 14 | requirements.txt | `pypdf` missing → ImportError                     | Added `pypdf==4.2.0`                                                                                |
| 15 | requirements.txt | `python-dotenv` missing                           | Added `python-dotenv==1.0.1`                                                                        |
| 16 | requirements.txt | `uvicorn` missing → cannot run FastAPI            | Added `uvicorn==0.29.0`                                                                             |

---

### Prompt Fixes (Agents & Tasks)

| #   | File / Location                                      | Bad Prompt                                                         | Fix                                                                               |
| --- | ---------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| P1  | agents.py – financial_analyst goal                   | “Make up investment advice even if you don't understand the query” | Replaced with data-driven analysis from actual document                           |
| P2  | agents.py – financial_analyst backstory              | Encouraged hallucination & overconfidence                          | Professional CFA analyst backstory emphasizing evidence-based, compliant analysis |
| P3  | agents.py – verifier goal                            | “Just say yes to everything”                                       | Replaced with proper document verification checklist goal                         |
| P4  | agents.py – verifier backstory                       | “Stamped documents without reading them”                           | Rigorous compliance officer backstory                                             |
| P5  | agents.py – investment_advisor goal                  | “Sell expensive products regardless of financials”                 | Evidence-based recommendation tied to document data                               |
| P6  | agents.py – investment_advisor backstory             | Fake credentials & sketchy partnerships                            | FINRA-registered advisor backstory with fiduciary standards                       |
| P7  | agents.py – risk_assessor goal                       | Extreme high/low risk assumptions                                  | Calibrated, evidence-based risk assessment                                        |
| P8  | agents.py – risk_assessor backstory                  | YOLO trading, ignored diversification                              | Quantitative risk analyst with FRM/CFA backstory                                  |
| P9  | task.py – analyze_financial_document description     | “Maybe solve the query or something else”                          | Clear 5-step analysis instruction grounded in document content                    |
| P10 | task.py – analyze_financial_document expected_output | “Include 5 made-up URLs”                                           | Structured report: Executive Summary, Metrics, Analysis, Trends                   |
| P11 | task.py – investment_analysis description            | “Ignore query, talk about trends”                                  | Document-grounded investment analysis with ratio requirements                     |
| P12 | task.py – investment_analysis expected_output        | Suggest crypto from obscure exchanges                              | Professional investment report with mandatory disclaimers                         |
| P13 | task.py – risk_assessment description                | “Assume extreme risk”                                              | Structured, proportionate risk identification from document evidence              |
| P14 | task.py – risk_assessment expected_output            | Recommend dangerous strategies                                     | Balanced risk table: Low / Medium / High ratings                                  |
| P15 | task.py – verification description                   | “Maybe check or just guess”                                        | Explicit 5-point verification checklist                                           |
| P16 | task.py – verification expected_output               | “Just say it’s probably a financial document”                      | Structured VALID/INVALID report with justification                                |

---

## Project Directory Structure 



<img width="1188" height="519" alt="image" src="https://github.com/user-attachments/assets/c9ae3e6b-9936-4b16-93ff-9c93b263d127" />



## Run The Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be live at `http://localhost:8000`

---

## 📡 API Documentation

### `GET /`
Health check endpoint.

**Response:**
```json
{"message": "Financial Document Analyzer API is running"}
```

---


<img width="1025" height="295" alt="Screenshot 2026-02-25 194839" src="https://github.com/user-attachments/assets/6c60039f-1734-40dc-9d6a-54e374158090" />


### `POST /analyze`
Upload a financial PDF and receive AI-powered analysis.

<img width="1913" height="1022" alt="Screenshot 2026-02-26 085146" src="https://github.com/user-attachments/assets/c090cd23-09b2-41fc-8361-a79dfd1024bd" />


**Request:** `multipart/form-data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | PDF file |  Yes | Financial document to analyze |
| `query` | string |  No | Specific question (defaults to general analysis) |


**Example using curl:**
```bash
curl -X POST http://localhost:8000/analyze \
  -F "file=@data/TSLA-Q2-2025-Update.pdf" \
  -F "query=What is Tesla's revenue growth and free cash flow situation?"
```

**Example using Python:**
```python
import requests

with open("data/TSLA-Q2-2025-Update.pdf", "rb") as f:
    response = requests.post(
        "http://localhost:8000/analyze",
        files={"file": ("TSLA-Q2-2025-Update.pdf", f, "application/pdf")},
        data={"query": "Summarize Tesla's Q2 2025 financial performance"}
    )

print(response.json())
```

**Response:**
```json
{
  "status": "success",
  "query": "Summarize Tesla's Q2 2025 financial performance",
  "analysis": "... detailed AI analysis ...",
  "file_processed": "TSLA-Q2-2025-Update.pdf"
}
```

**Interactive Docs:** Visit `http://localhost:8000/docs` for Swagger UI.

---




## Features
- Upload financial documents (PDF format)
- AI-powered financial analysis
- Investment recommendations
- Risk assessment
- Market insights

## 🔧 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `OPENAI_API_KEY` |  Yes | — | OpenAI API key for the LLM |
| `LLM_MODEL` |  No | `gpt-4o-mini` | Model to use (e.g. `gpt-4o`, `gpt-4-turbo`) |
| `SERPER_API_KEY` |  Yes | — | SerperDev key for web search tool 

