import sys
import json
from server import lookup_ip, lookup_domain

def test_lookup_ip():
    print("Testing lookup_ip with 8.8.8.8...")
    result = lookup_ip.fn("8.8.8.8")
    try:
        data = json.loads(result)
        print("Success! Result snippet:")
        print(json.dumps(data, indent=2)[:200] + "...")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON. Raw output: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 20)

def test_lookup_domain():
    print("Testing lookup_domain with google.com...")
    result = lookup_domain.fn("google.com")
    try:
        data = json.loads(result)
        print("Success! Result snippet:")
        print(json.dumps(data, indent=2)[:200] + "...")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON. Raw output: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("-" * 20)

if __name__ == "__main__":
    test_lookup_ip()
    test_lookup_domain()
