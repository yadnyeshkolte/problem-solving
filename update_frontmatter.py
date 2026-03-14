import os
import re
import yaml

directory = r"c:\Users\Yadnyesh Kolte\problem-solving\_problems\dsa"

# Regular expressions for matching URLs
neetcode_re = re.compile(r'https://neetcode\.io/\S+')
leetcode_re = re.compile(r'https://leetcode\.com/\S+')

for filename in os.listdir(directory):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content to separate frontmatter from the rest of the file
    frontmatter_match = re.match(r"---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    
    if frontmatter_match:
        frontmatter_str = frontmatter_match.group(1)
        rest_of_file = frontmatter_match.group(2)
        
        try:
            # Load yaml
            data = yaml.safe_load(frontmatter_str)
            if data is None:
                data = {}
        except Exception as e:
            print(f"Error parsing YAML in {filename}: {e}")
            continue

        # Extract URLs from the rest of the file if they appear at the top
        # Check first 15 lines of rest_of_file for bare links
        lines = rest_of_file.split('\n')
        top_lines = lines[:15]
        
        neetcode_url = None
        leetcode_url = None
        
        for line in top_lines:
            n_match = neetcode_re.search(line)
            l_match = leetcode_re.search(line)
            if n_match and not neetcode_url:
                 neetcode_url = n_match.group(0)
            if l_match and not leetcode_url:
                 leetcode_url = l_match.group(0)
                 
        # Prioritize existing frontmatter URLs if they exist
        existing_leetcode = data.get('leetcode_url')
        existing_neetcode = data.get('neetcode_url')
        
        if existing_leetcode and 'leetcode.com' in existing_leetcode:
             leetcode_url = existing_leetcode
        elif existing_leetcode and 'neetcode.io' in existing_leetcode:
             neetcode_url = existing_leetcode # fix for some incorrectly labeled URLs
        
        if existing_neetcode:
             neetcode_url = existing_neetcode

        if neetcode_url:
             data['neetcode_url'] = neetcode_url
        if leetcode_url:
             data['leetcode_url'] = leetcode_url
             
        # Update category
        category = data.get('category')
        categories = set()
        if isinstance(category, list):
             categories.update(category)
        elif isinstance(category, str):
             if category: categories.add(category)
             
        if leetcode_url:
             categories.add("LeetCode")
        if neetcode_url:
             categories.add("NeetCode")
        
        if "DSA" not in categories:
             categories.add("DSA")
             
        # Convert back to list and sort for consistency
        data['category'] = sorted(list(categories))
        
        # Clean up the top of the file by removing bare links
        new_lines = []
        for line in lines:
            if neetcode_re.search(line) and not 'neetcode_url' in line:
                 continue
            if leetcode_re.search(line) and not 'leetcode_url' in line:
                 continue
            new_lines.append(line)
            
        # Remove consecutive blank lines at the top
        while new_lines and new_lines[0].strip() == '':
             new_lines.pop(0)

        new_rest = '\n'.join(new_lines)
        
        # Dump yaml
        class NoAliasDumper(yaml.SafeDumper):
            def ignore_aliases(self, data):
                return True

        new_frontmatter = yaml.dump(data, sort_keys=False, default_flow_style=False, allow_unicode=True, Dumper=NoAliasDumper)
        
        new_content = f"---\n{new_frontmatter}---\n\n{new_rest}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
             f.write(new_content)
        print(f"Updated {filename}")
        
    else:
         # File doesn't have frontmatter, we need to create it
         print(f"Adding new frontmatter to {filename}")
         lines = content.split('\n')
         
         neetcode_url = None
         leetcode_url = None
         
         # search first 20 lines
         search_lines = lines[:20]
         for line in search_lines:
             n_match = neetcode_re.search(line)
             l_match = leetcode_re.search(line)
             if n_match and not neetcode_url:
                  neetcode_url = n_match.group(0)
             if l_match and not leetcode_url:
                  leetcode_url = l_match.group(0)
                  
         data = {
             'title': filename.replace('.md', '').replace('-', ' ').title(),
             'category': ['DSA']
         }
         
         if leetcode_url:
              data['leetcode_url'] = leetcode_url
              data['category'].append('LeetCode')
         if neetcode_url:
              data['neetcode_url'] = neetcode_url
              data['category'].append('NeetCode')
              
         # Clean up lines
         new_lines = []
         for line in lines:
             if neetcode_re.search(line):
                  continue
             if leetcode_re.search(line):
                  continue
             new_lines.append(line)
             
         while new_lines and new_lines[0].strip() == '':
             new_lines.pop(0)
             
         new_rest = '\n'.join(new_lines)
         
         new_frontmatter = yaml.dump(data, sort_keys=False, default_flow_style=False, allow_unicode=True)
         
         new_content = f"---\n{new_frontmatter}---\n\n{new_rest}"
         
         with open(filepath, 'w', encoding='utf-8') as f:
              f.write(new_content)
         print(f"Created new frontmatter for {filename}")

print("Done.")
