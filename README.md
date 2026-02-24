# Online Judge MCP Server

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
[![License](https://img.shields.io/github/license/wangicheng/oj-mcp-server.svg)](https://github.com/wangicheng/oj-mcp-server/blob/main/LICENSE)

<a href="https://glama.ai/mcp/servers/@wangicheng/oj-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@wangicheng/oj-mcp-server/badge" />
</a>

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
- `pip`

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

## Installation in MCP Clients

To use this server with an MCP-compatible client like Claude Desktop, Cursor, or Cline, you need to add it to your client's MCP configuration settings.

### Claude Desktop

Edit your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "oj-mcp-server": {
      "command": "C:/path/to/venv/Scripts/oj-mcp-server",
      "args": [],
      "env": {
        "OJ_URL": "http://localhost:8000",
        "OJ_USERNAME": "your-username",
        "OJ_PASSWORD": "your-password"
      }
    }
  }
}
```

### Cursor / Cline

In the MCP settings panel, add a new server:
- **Type**: command
- **Name**: `oj-mcp-server`
- **Command**: `C:/path/to/venv/Scripts/oj-mcp-server` (or `/path/to/venv/bin/oj-mcp-server` on macOS/Linux)
- **Environment**: Set `OJ_URL`, `OJ_USERNAME`, and `OJ_PASSWORD`

*(Make sure to adjust the directory path to wherever you cloned the repository)*

### OpenCode

To configure the MCP server in the OpenCode IDE, you can edit your `opencode.json` configuration file (located globally at `~/.config/opencode/opencode.json` or in your project directory). Add the server under the `mcp` key:

```json
{
  "mcp": {
    "oj-mcp-server": {
      "type": "local",
      "command": [
        "C:/path/to/venv/Scripts/oj-mcp-server"
      ],
      "environment": {
        "OJ_URL": "http://localhost:8000",
        "OJ_USERNAME": "your-username",
        "OJ_PASSWORD": "your-password"
      }
    }
  }
}
```
