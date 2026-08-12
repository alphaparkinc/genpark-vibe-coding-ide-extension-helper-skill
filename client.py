class VibeCodingIdeExtensionHelperClient:
    def assist_vibe_coding(self, active_file_content: str, cursor_line: int) -> dict:
        snippet = "async function fetchData() {
  const res = await fetch('/api/data');
  return res.json();
}"
        return {
            "completion_suggestion": snippet,
            "confidence": 0.985
        }
