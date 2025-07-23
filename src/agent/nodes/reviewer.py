# agent/nodes/reviewer.py
from langchain.chat_models import ChatOpenAI
from agent.config import OPENROUTER_API_KEY

def review_draft(state):
    prompt = f"""You are a strict compliance reviewer for a customer support team.

Check the following draft for:
- Overpromising (e.g., offering refunds directly)
- Disclosure of sensitive information (e.g., encryption methods, internal protocols)
- Advising on security or admin procedures
- Tone and clarity

If any violation exists, return: 'rejected' and explain why.
If it’s clear and safe, return: 'approved'

Support Draft:
\"\"\"{state['draft']}\"\"\"
"""
    

    llm = ChatOpenAI(openai_api_base="https://openrouter.ai/api/v1",
                     openai_api_key=OPENROUTER_API_KEY,
                     model_name="openai/gpt-3.5-turbo")
    feedback = llm.predict(prompt)
    print(feedback)
    result = "approved" if "approved" in feedback.lower() else "rejected"
    return {**state, "review_result": result, "review_feedback": feedback}