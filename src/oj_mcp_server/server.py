import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from .oj_client import OJClient

# Load logic from .env
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("oj-mcp-server")

# Configuration
OJ_URL = os.environ.get("OJ_URL", "http://134.208.3.66")
OJ_USERNAME = os.environ.get("OJ_USERNAME", "")
OJ_PASSWORD = os.environ.get("OJ_PASSWORD", "")


client = OJClient(base_url=OJ_URL)
is_logged_in = False

def get_authenticated_client():
    global is_logged_in
    if not is_logged_in:
        if not OJ_USERNAME or not OJ_PASSWORD:
            raise ValueError("OJ_USERNAME and OJ_PASSWORD environment variables are required.")
        client.login(OJ_USERNAME, OJ_PASSWORD)
        is_logged_in = True
    return client

@mcp.tool()
def list_problems(offset: int = 0, limit: int = 50) -> str:
    """
    Fetch the list of problems from the Online Judge.
    Returns a JSON string containing total count and results.
    """
    c = get_authenticated_client()
    try:
        data = c.get_problems(offset=offset, limit=limit)
        return str(data)
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def list_my_submissions(offset: int = 0, limit: int = 20) -> str:
    """
    Fetch the list of latest submissions made by the authenticated user.
    Returns a JSON string containing the submission histories.
    """
    c = get_authenticated_client()
    try:
        data = c.get_submissions(offset=offset, limit=limit, myself=1)
        return str(data)
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def get_problem_details(problem_id: str) -> str:
    """
    Fetch the detailed information of a specific problem.
    problem_id: The external ID/display ID of the problem (e.g., "PR-114-1-31").
    """
    c = get_authenticated_client()
    try:
        data = c.get_problem(problem_id)
        return str(data)
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def submit_code(problem_id: int, code: str, language: str) -> str:
    """
    Submit code to the Online Judge for a specific problem.
    problem_id: the internal system ID of the problem.
    language: string such as "C", "C++", "Python3".
    code: the source code to submit.
    """
    c = get_authenticated_client()
    try:
        data = c.submit_code(code=code, language=language, problem_id=problem_id)
        return str(data)
    except Exception as e:
        return f"Error: {e}"

@mcp.tool()
def get_submission_status(submission_id: str) -> str:
    """
    Get the status and result of a previously submitted code.
    submission_id: The ID returned when submitting the code.
    """
    c = get_authenticated_client()
    try:
        data = c.get_submission(submission_id)
        return str(data)
    except Exception as e:
        return f"Error: {e}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()
