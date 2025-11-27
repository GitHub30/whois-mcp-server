import sys
import json
from server import lookup_ip, lookup_domain

def test_lookup_ip():
    print("Testing lookup_ip with 8.8.8.8...")
    result = lookup_ip.fn("8.8.8.8")
    try:
        # result is already a dict (or string on error)
        if isinstance(result, dict):
            print("Success! Result snippet:")
            print(json.dumps(result, indent=2, default=str)[:200] + "...")
        else:
            print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 20)

def test_lookup_domain():
    print("Testing lookup_domain with google.com...")
    result = lookup_domain.fn("google.com")
    try:
        # result is already a dict (or string on error)
        if isinstance(result, dict):
            print("Success! Result snippet:")
            print(json.dumps(result, indent=2, default=str)[:200] + "...")
        else:
            print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 20)

if __name__ == "__main__":
    test_lookup_ip()
    test_lookup_domain()
