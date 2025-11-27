from fastmcp import FastMCP
from ipwhois import IPWhois
import whois
import json

# Initialize FastMCP server
mcp = FastMCP("whois-server")

def _lookup_ip(ip_address: str) -> str:
    try:
        obj = IPWhois(ip_address)
        results = obj.lookup_rdap(depth=1)
        return json.dumps(results, indent=2, default=str)
    except Exception as e:
        return f"Error performing IP WHOIS lookup: {str(e)}"

def _lookup_domain(domain: str) -> str:
    try:
        w = whois.whois(domain)
        # Convert the WhoisEntry object to a dictionary
        return json.dumps(w, indent=2, default=str)
    except Exception as e:
        return f"Error performing Domain WHOIS lookup: {str(e)}"

@mcp.tool()
def lookup_ip(ip_address: str) -> str:
    """
    Perform a WHOIS lookup for an IP address.
    
    Args:
        ip_address: The IP address to lookup (e.g., "8.8.8.8").
        
    Returns:
        A JSON string containing the WHOIS information.
    """
    return _lookup_ip(ip_address)

@mcp.tool()
def lookup_domain(domain: str) -> str:
    """
    Perform a WHOIS lookup for a domain name.
    
    Args:
        domain: The domain name to lookup (e.g., "google.com").
        
    Returns:
        A JSON string containing the WHOIS information.
    """
    return _lookup_domain(domain)

if __name__ == "__main__":
    mcp.run()
