from fastmcp import FastMCP
from ipwhois import IPWhois
import whois
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
        return whois.whois(domain)
    except Exception as e:
        return f"Error performing Domain WHOIS lookup: {str(e)}"

if __name__ == "__main__":
    mcp.run()
