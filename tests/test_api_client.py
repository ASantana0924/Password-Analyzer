import json
from src.utils import api_client

def main():
    print("Loading config...")
    with open("config/nameapi_config.json", "r") as f:
        config = json.load(f)
    print("✓ Config loaded successfully")
    
    print("\nTesting API call...")
    try:
        # Try a SIMPLE name request
        response = api_client.parse_name("John", "Smith")
        print("✓ API call succeeded")
        print("\nRaw API Response:")
        print(response)

    except Exception as e:
        print("✗ API call failed")
        print(str(e))

if __name__ == "__main__":
    main()
