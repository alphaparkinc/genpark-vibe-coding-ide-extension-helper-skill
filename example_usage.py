from client import VibeCodingIdeExtensionHelperClient

def main():
    client = VibeCodingIdeExtensionHelperClient()
    res = client.assist_vibe_coding("function main() {", 1)
    print(f"Confidence: {res['confidence']}")
    print("Suggested Code:")
    print(res["completion_suggestion"])

if __name__ == "__main__":
    main()
