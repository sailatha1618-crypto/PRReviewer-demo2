import os
import subprocess
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_diff():
    result = subprocess.run(
        ["git", "diff", "HEAD^", "HEAD"],
        capture_output=True,
        text=True
    )
    return result.stdout

diff = get_diff()

if not diff.strip():
    print("No changes found.")
    exit(0)

prompt = f"""
You are an automated code-fixing agent.

Analyze the following Git diff.

Find and FIX:
1. Bugs
2. Runtime errors
3. Security vulnerabilities
4. Code-quality problems
5. Clear improvement opportunities

Rules:
- Make only necessary changes.
- Do not rewrite the entire project.
- Do not remove working functionality.
- Do not add fake implementations.
- Never expose secrets.
- Preserve the existing project architecture.
- Make the smallest safe fix possible.

IMPORTANT:
Modify the actual files in the repository.
Do not only explain the fix.

Git diff:

{diff}
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print(response.output_text)
eval(username)
