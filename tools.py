# ==========================================
# tools.py - Financial Document Tools
# ==========================================

import os
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Correct environment variable names
openai_key = os.getenv("OPENAI_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

# ⚠ Optional: Raise error if SERPER key missing
if not serper_key:
    print("WARNING: SERPER_API_KEY not found in .env file")

# ✅ Updated LangChain import
from langchain_community.document_loaders import PyPDFLoader

# ✅ Correct Serper import (compatible with crewai-tools 0.1.6)
from crewai_tools import SerperDevTool


# ==========================================================
# 🔎 Search Tool (Optional Web Search)
# ==========================================================

# This will automatically read SERPER_API_KEY from environment
search_tool = SerperDevTool()


# ==========================================================
# 📄 Financial Document PDF Reader Tool
# ==========================================================

class FinancialDocumentTool:
    """
    Tool for reading and cleaning financial PDF documents.
    """

    @staticmethod
    async def read_data_tool(path: str = "data/sample.pdf") -> str:
        """
        Reads financial PDF and returns cleaned text.
        """

        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found at path: {path}")

        try:
            loader = PyPDFLoader(path)
            docs = loader.load()

            full_report = ""

            for page in docs:
                content = page.page_content.strip()

                # Remove empty lines
                content = "\n".join(
                    line.strip()
                    for line in content.splitlines()
                    if line.strip()
                )

                full_report += content + "\n\n"

            if not full_report.strip():
                raise ValueError("PDF file appears empty or unreadable.")

            return full_report

        except Exception as e:
            raise RuntimeError(f"Error reading PDF file: {str(e)}")


# ==========================================================
# 📊 Investment Analysis Tool
# ==========================================================

class InvestmentTool:
    """
    Tool to perform structured financial analysis.
    """

    @staticmethod
    async def analyze_investment_tool(financial_document_data: str) -> str:

        if not financial_document_data:
            return "No financial data provided for investment analysis."

        cleaned_data = " ".join(financial_document_data.split()).lower()

        insights = []

        if "revenue" in cleaned_data:
            insights.append("Revenue information detected.")

        if "profit" in cleaned_data:
            insights.append("Profit metrics identified.")

        if "debt" in cleaned_data:
            insights.append("Debt-related information found.")

        if not insights:
            insights.append("Limited financial metrics detected in document.")

        return (
            "Investment Analysis Summary:\n"
            + "\n".join(f"- {point}" for point in insights)
        )


# ==========================================================
# ⚠ Risk Assessment Tool
# ==========================================================

class RiskTool:
    """
    Tool to generate risk assessment from document data.
    """

    @staticmethod
    async def create_risk_assessment_tool(financial_document_data: str) -> str:

        if not financial_document_data:
            return "No financial data available for risk assessment."

        text = financial_document_data.lower()
        risks = []

        if "loss" in text:
            risks.append("Potential profitability risk detected.")

        if "debt" in text:
            risks.append("Debt exposure risk identified.")

        if "decline" in text:
            risks.append("Revenue decline risk noted.")

        if "litigation" in text:
            risks.append("Legal risk exposure found.")

        if not risks:
            risks.append("No major financial risks explicitly identified.")

        return (
            "Risk Assessment Summary:\n"
            + "\n".join(f"- {risk}" for risk in risks)
        )