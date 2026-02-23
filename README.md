# Online Judge MCP Server

This is a Model Context Protocol (MCP) server that provides AI agents with tools to interact with an Online Judge API.

## Features

Provides the following tools:
- `list_problems(offset, limit)`: List available problems on the OJ.
- `list_my_submissions(offset, limit)`: List recent submissions made by the authenticated user.
- `get_problem_details(problem_id)`: Fetch detailed descriptions, samples, limits, and rules of a problem.
- `submit_code(problem_id, code, language)`: Submit source code to a specific problem.
- `get_submission_status(submission_id)`: Check the polling status of a code submission.

## Requirements

- Python 3.10 or higher
- `uv` (recommended) or `pip`

## Setup & Running

1. **Install dependencies**:
   ```bash
   pip install -e .
   ```

2. **Run the MCP server locally**:
   Set the following environment variables before running:
   ```bash
   set OJ_URL="http://localhost:8000" # Replace with actual OJ URL
   set OJ_USERNAME="your-username"
   set OJ_PASSWORD="your-password"
   
   oj-mcp-server
   ```
