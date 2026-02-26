# agents.py
from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# Financial Analyst
financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial documents and provide insights.",
    backstory="Expert financial analyst skilled in modeling and risk evaluation.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[]  # ✅ Required
)

# Financial Document Verifier
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify whether the uploaded file is a valid financial document.",
    backstory="Specialist in compliance and document validation.",
    verbose=True,
    memory=True,
    llm=llm,
    max_iter=2,
    allow_delegation=False,
    tools=[]  # ✅ Required
)

# Investment Advisor
investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide responsible and data-driven investment recommendations.",
    backstory="Certified financial advisor focused on ethical investing.",
    verbose=True,
    llm=llm,
    max_iter=3,
    allow_delegation=False,
    tools=[]  # ✅ Required
)

# Risk Assessor
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Assess financial risks using realistic financial metrics.",
    backstory="Experienced institutional finance risk manager.",
    verbose=True,
    llm=llm,
    max_iter=3,
    allow_delegation=False,
    tools=[]  # ✅ Required
)