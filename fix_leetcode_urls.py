import os
import yaml
import re

directory = r"c:\Users\Yadnyesh Kolte\problem-solving\_problems\dsa"

class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

count_fixed = 0

for filename in os.listdir(directory):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_match = re.match(r"---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if frontmatter_match:
        frontmatter_str = frontmatter_match.group(1)
        rest_of_file = frontmatter_match.group(2)
        
        try:
            data = yaml.safe_load(frontmatter_str)
            if data is None:
                continue
                
            needs_update = False
            
            # Check if leetcode_url is populated with neetcode link
            if data.get('leetcode_url') and 'neetcode.io' in data['leetcode_url']:
                print(f"[{filename}] Found neetcode link in leetcode_url: {data['leetcode_url']}")
                # We already know neetcode_url captured it in previous steps, so we just delete it from leetcode_url
                del data['leetcode_url']
                
                # We should also remove 'LeetCode' from category list if it has no legitimate leetcode URL
                if 'category' in data and 'LeetCode' in data['category']:
                    data['category'].remove('LeetCode')
                    
                needs_update = True
                count_fixed += 1
                
            if needs_update:
                new_frontmatter = yaml.dump(data, sort_keys=False, default_flow_style=False, allow_unicode=True, Dumper=NoAliasDumper)
                new_content = f"---\n{new_frontmatter}---\n{rest_of_file}"
                with open(filepath, 'w', encoding='utf-8') as f:
                     f.write(new_content)
                print(f" -> Fixed & saved {filename}")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"Total files fixed: {count_fixed}")
