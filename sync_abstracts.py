import os
import re

papers = [
    ("wp1_infrastructure/ssrn-6110252_Revised.tex", "wp1_infrastructure/ssrn-6110252_Metadata.md"),
    ("wp2_surplus_capacity/ssrn-6211658_Revised.tex", "wp2_surplus_capacity/ssrn-6211658_Metadata.md"),
    ("wp3_los_angeles_pipeline/ssrn-6579600_Revised.tex", "wp3_los_angeles_pipeline/ssrn-6579600_Metadata.md")
]

base_dir = "/home/user0/git/working_papers"

for tex_file, md_file in papers:
    tex_path = os.path.join(base_dir, tex_file)
    md_path = os.path.join(base_dir, md_file)
    
    if not os.path.exists(tex_path) or not os.path.exists(md_path):
        print(f"Skipping {tex_file} - not found.")
        continue
        
    with open(tex_path, 'r') as f:
        tex_content = f.read()
        
    abstract_match = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', tex_content, re.DOTALL)
    if abstract_match:
        abstract_text = abstract_match.group(1).strip()
        
        with open(md_path, 'r') as f:
            md_content = f.read()
            
        # Replace the content under ## Abstract until the next ## or end of file
        new_md_content = re.sub(r'(## Abstract\s*\n).*?(?=\n## |\Z)', r'\1' + abstract_text + '\n\n', md_content, flags=re.DOTALL)
        
        if new_md_content != md_content:
            with open(md_path, 'w') as f:
                f.write(new_md_content)
            print(f"Updated {md_file}")
        else:
            print(f"{md_file} is already perfectly synced.")
    else:
        print(f"Could not find abstract in {tex_file}")

