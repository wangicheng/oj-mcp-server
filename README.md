# Online Judge MCP Server

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
[![PyPI](https://img.shields.io/pypi/v/oj-mcp-server.svg)](https://pypi.org/project/oj-mcp-server/)
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

## Quickstart

### Using `uvx` (Recommended)
The easiest way to run this server is using [`uvx`](https://docs.astral.sh/uv/), which automatically downloads the correct Python version, creates an ephemeral environment, and runs the tool seamlessly:

```bash
set OJ_URL="http://localhost:8000" # Replace with actual OJ URL
set OJ_USERNAME="your-username"
set OJ_PASSWORD="your-password"

uvx oj-mcp-server
```

### Using `pip` or `pipx`
Alternatively, you can install the package directly into your Python environment:

```bash
pip install oj-mcp-server
oj-mcp-server
```

## Usage with MCP Clients

To use this server, add it to your MCP client's configuration (e.g., Claude Desktop, Cursor, Cline).

### Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "oj-mcp-server": {
      "command": "uvx",
      "args": ["oj-mcp-server"],
      "env": {
        "OJ_URL": "http://localhost:8000",
        "OJ_USERNAME": "your-username",
        "OJ_PASSWORD": "your-password"
      }
    }
  }
}
```
*Note: If you installed globally via `pip`, simply change `"command"` to `"oj-mcp-server"` and `"args"` to `[]`.*

### Cursor & Cline

In the MCP settings panel, add a new server:
- **Type**: command
- **Name**: `oj-mcp-server`
- **Command**: `uvx oj-mcp-server` *(or `oj-mcp-server` if installed via pip)*
- **Environment**: Set `OJ_URL`, `OJ_USERNAME`, and `OJ_PASSWORD`

### OpenCode

Add this configured server inside your `opencode.json` (under the `mcp` key):

```json
{
  "mcp": {
    "oj-mcp-server": {
      "type": "local",
      "command": ["uvx", "oj-mcp-server"],
      "environment": {
        "OJ_URL": "http://localhost:8000",
        "OJ_USERNAME": "your-username",
        "OJ_PASSWORD": "your-password"
      }
    }
  }
}
```
*Note: If using pip, change the command array to `["oj-mcp-server"]`.*
