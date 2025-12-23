"""
Simple retriever for the fake RAG system.

This module reads structured daily task data and determines
which task and which fields are relevant for a given user query.
"""

from src.ingest.daily_tasks_data import DAILY_TASKS

def detect_intent(user_question):
    """
    Detects the intent of the user question.
    Returns one of: 'HOW', 'WHY', 'OTHER'
    """
    question = user_question.lower()

    if "how" in question or "steps" in question or "process" in question:
        return "HOW"

    if (
        "why" in question
        or "fail" in question
        or "failed" in question
        or "not working" in question
        or "error" in question
    ):
        return "WHY"

    return "OTHER"


def match_task(user_question, tasks):
    """
    Finds the most relevant task based on simple keyword matching.
    Returns the matched task dictionary or None.
    """
    question = user_question.lower()

    for task in tasks:
        task_name = task["task_name"].lower()

        # simple keyword check
        if "daily rates" in question and "daily rates" in task_name:
            return task

    return None
def select_response_fields(task, intent):
    """
    Selects relevant fields from a task based on user intent.
    """
    response = {
        "task_name": task["task_name"],
        "modules": task["modules"]
    }

    if intent == "HOW":
        response["steps"] = task["steps"]

        if "validation_checks" in task:
            response["validation_checks"] = task["validation_checks"]

        if "warnings" in task:
            response["warnings"] = task["warnings"]

    elif intent == "WHY":
        response["validation_checks"] = task["validation_checks"]
        response["warnings"] = task["warnings"]

        if "steps" in task:
            response["steps"] = task["steps"]

    else:
        return None

    return response
def retrieve_answer(user_question):
    """
    Main retrieval flow for the fake RAG system.
    """
    intent = detect_intent(user_question)
    task = match_task(user_question, DAILY_TASKS)

    if not task:
        return {
            "message": "I do not have enough information to answer this query."
        }

    response = select_response_fields(task, intent)

    if not response:
        return {
            "message": "I am unable to determine how to answer this query."
        }

    return response
