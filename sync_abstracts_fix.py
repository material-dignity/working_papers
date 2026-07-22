import os
import re

papers = [
    ("wp1_stewardship_model/ssrn-5968756_Revised.tex", "wp1_stewardship_model/ssrn-5968756_Metadata.md"),
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
        
    # The abstract is between \begin{minipage}{0.95\textwidth} and \end{minipage} and after \noindent
    abstract_match = re.search(r'\\noindent\s*\n\n(.*?)\n\n\\end\{minipage\}', tex_content, re.DOTALL)
    
    if abstract_match:
        abstract_text = abstract_match.group(1).strip()
        # Remove line breaks from the abstract text for markdown (optional, but let's keep it as is or replace single newlines with spaces)
        abstract_text = abstract_text.replace('\n', ' ')
        # fix double spaces
        abstract_text = re.sub(r' +', ' ', abstract_text)
        
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

