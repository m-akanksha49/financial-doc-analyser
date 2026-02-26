# task.py
from crewai import Task
from agents import financial_analyst

analyze_financial_document = Task(
    description="""
You are given a financial document file located at: {file_path}

User Query:
{query}

Carefully analyze the financial document and provide:

1. Financial summary
2. Key performance indicators
3. Risk factors
4. Investment insights
5. Final recommendation (Buy / Hold / Sell with reason)

Do not assume tools are available.
Provide clear structured output.
""",
    expected_output="Detailed financial analysis report with insights and recommendation.",
    agent=financial_analyst
)