# agent/nodes/drafter.py
from langchain.chat_models import ChatOpenAI
from agent.config import OPENROUTER_API_KEY

def generate_draft(state):
    prompt = f"""Given this context: {state['context']}\n\nAnd ticket:\nSubject: {state['subject']}\nDescription: {state['description']}\n\nWrite a helpful, clear support reply."""
    llm = ChatOpenAI(openai_api_base="https://openrouter.ai/api/v1",
                     openai_api_key=OPENROUTER_API_KEY,
                     model_name="openai/gpt-3.5-turbo")
    draft = llm.predict(prompt)
    return {**state, "draft": draft}