import os
import re

tex_path = "/home/user0/git/working_papers/wp3_los_angeles_pipeline/ssrn-6579600_Revised.tex"
md_path = "/home/user0/git/working_papers/wp3_los_angeles_pipeline/ssrn-6579600_Metadata.md"

with open(tex_path, 'r') as f:
    tex_content = f.read()

match = re.search(r'\\noindent\s*\n(.*?)\\end\{minipage\}', tex_content, re.DOTALL)
if match:
    abstract_text = match.group(1).strip()
    abstract_text = abstract_text.replace('\n', ' ')
    abstract_text = re.sub(r' +', ' ', abstract_text)
    
    with open(md_path, 'r') as f:
        md_content = f.read()
        
    def replacer(m):
        return m.group(1) + abstract_text + '\n\n'
        
    new_md_content = re.sub(r'(## Abstract\s*\n).*?(?=\n## |\Z)', replacer, md_content, flags=re.DOTALL)
    
    with open(md_path, 'w') as f:
        f.write(new_md_content)
    print("Updated WP3 Metadata")
else:
    print("Could not match WP3")
