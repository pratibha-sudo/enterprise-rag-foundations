"""
Daily task knowledge base for the fake RAG system.

This file contains structured representations of common
enterprise daily tasks. It is used during ingestion and
retrieval simulation.
"""
TASK_SOURCE = "DAILY_TASKS"
DAILY_TASKS = [
    {
        "task_name": "Load Daily Rates Manually",
        "modules": ["AP"],
        "purpose": "To update the application with daily exchange rates.",
        "steps": [
            "Login using the Accounts Payable responsibility.",
            "Navigate to the Submit Request form.",
            "Submit the concurrent program 'Import Daily Rates'."
        ],
        "validation_checks": "Verify the status of the submitted program and review the log output.",
        "warnings": "If 'Rates not found' appears in the log, contact the system administrator."
    }
]
