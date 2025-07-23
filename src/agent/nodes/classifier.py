# agent/nodes/classifier.py
from langchain.chat_models import ChatOpenAI
from agent.config import OPENROUTER_API_KEY

def classify_ticket(state):
    prompt = f"""Classify the following support ticket into one of the categories:
Billing, Technical, Security, General.

Subject: {state['subject']}
Description: {state['description']}
"""
    llm = ChatOpenAI(openai_api_base="https://openrouter.ai/api/v1",
                     openai_api_key=OPENROUTER_API_KEY,
                     model_name="openai/gpt-3.5-turbo")
    response = llm.predict(prompt)
    category = response.lower().strip()
    return {**state, "category": category, "attempt": 1}