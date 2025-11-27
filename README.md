# whois-mcp-server
![Test](https://github.com/GitHub30/whois-mcp-server/actions/workflows/test.yml/badge.svg)

A Model Context Protocol (MCP) server that provides WHOIS lookup capabilities for IP addresses and domain names. Built with [FastMCP](https://github.com/jlowin/fastmcp), `ipwhois`, and `python-whois`.

## Features

- **IP Lookup**: Retrieve WHOIS information for IP addresses using `lookup_ip`.
- **Domain Lookup**: Retrieve WHOIS information for domain names using `lookup_domain`.

## Tools

### `lookup_ip`
Performs a WHOIS lookup for a given IP address (e.g., "8.8.8.8").

### `lookup_domain`
Performs a WHOIS lookup for a given domain name (e.g., "google.com").

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python server.py
   ```

## Development

Run tests:
```bash
python test.py
```