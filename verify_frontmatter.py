import os
import yaml
import re

directory = r"c:\Users\Yadnyesh Kolte\problem-solving\_problems\dsa"

for filename in os.listdir(directory):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
    if frontmatter_match:
        try:
            data = yaml.safe_load(frontmatter_match.group(1))
            if data is None:
                data = {}
            if not data.get("category"):
                print(f"Missing category in {filename}")
            if not data.get("topics"):
                print(f"Missing topics in {filename}")
            if not data.get("date"):
                print(f"Missing date in {filename}")
        except Exception as e:
            print(f"Error parsing YAML in {filename}: {e}")
    else:
        print(f"No frontmatter in {filename}")
