# =============================================================================
# Student Name: Michael Johnson
# Lab Title: Lab 5
# Date:
# =============================================================================


# 1.1 Import Path from pathlib and import json
from pathlib import Path
import json


# 1.2 Create a function to save the task list
def store_task_list(task_list):
    """Save task list to a file."""
    file = Path("task_list.json")

    # 1.3 Create a json string of the list using dumps() and write it to the file
    file.write_text(json.dumps(task_list))

    # 1.4 Display that the file was saved
    print("Task list saved.")


# 2.1 Create a function to load the task list
def load_task_list():
    """Load task list from a file."""

    # 2.2 Create a Path object for task_list.json
    file = Path("task_list.json")

    # 2.3 Check if the file exists
    if file.exists():
        # Read the contents and then return the list
        return json.loads(file.read_text())
        # Return an empty list if the path does not exist
    return []