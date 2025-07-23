# agent/nodes/escalation.py
import csv
from pathlib import Path

ESCALATION_FILE = Path("data/escalation_log.csv")

ESCALATION_FILE.parent.mkdir(parents=True, exist_ok=True)
if not ESCALATION_FILE.exists():
    with open(ESCALATION_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Subject", "Description", "Draft", "Feedback"])

def log_escalation(state):
    with open(ESCALATION_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            state['subject'],
            state['description'],
            state.get('draft', 'N/A'),
            state.get('review_feedback', 'N/A')
        ])
    return {**state, "final_response": "Ticket requires human review. Escalated."}
