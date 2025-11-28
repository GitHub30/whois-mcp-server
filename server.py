from fastmcp import FastMCP
from ipwhois import IPWhois
import subprocess
import shutil
import json

from typing import Any

# Initialize FastMCP server
mcp = FastMCP("whois-server")

@mcp.tool(annotations={"readOnlyHint": True})
def lookup_ip(ip_address: str) -> Any:
    """
    Perform a WHOIS lookup for an IP address.
    
    Args:
        ip_address: The IP address to lookup (e.g., "8.8.8.8").
        
    Returns:
        The WHOIS information as a dictionary.
    """
    try:
        return IPWhois(ip_address).lookup_rdap(depth=1)
    except Exception as e:
        return f"Error performing IP WHOIS lookup: {str(e)}"

@mcp.tool(annotations={"readOnlyHint": True})
def lookup_domain(domain: str) -> Any:
    """
    Perform a WHOIS lookup for a domain name.
    
    Args:
        domain: The domain name to lookup (e.g., "google.com").
        
    Returns:
        The WHOIS information as a dictionary.
    """
    try:
        # Ensure `whois` command is available on the system
        if shutil.which("whois") is None:
            return "Error: 'whois' command not found on system."

        # Run the system `whois` command and return its stdout
        result = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=15)
        if result.returncode != 0:
            stderr = result.stderr.strip()
            if stderr:
                return f"Error running whois command: {stderr}"
            return f"whois command failed with exit code {result.returncode}"

        return result.stdout
    except Exception as e:
        return f"Error performing Domain WHOIS lookup: {str(e)}"

if __name__ == "__main__":
    mcp.run()
