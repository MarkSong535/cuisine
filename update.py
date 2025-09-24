import os
import glob

def update_index():
    with open('templates/index.md', 'r') as f:
        template_content = f.read()
    
    md_files = glob.glob('docs/*.md')
    
    md_files = [f.replace("docs/","/") for f in md_files if not f.endswith('index.md') and not f.endswith('tags.md')]
    
    links = []
    links_yml = []
    for md_file in sorted(md_files):
        filename = os.path.basename(md_file)
        title = filename.replace('.md', '').replace('_', ' ').replace('-', ' ').title()
        links.append(f"- [{title}]({filename})")
        links_yml.append(f"    - {title}: {filename}")
        
    links_section = "\n".join(links)
    final_content = template_content + "\n\n" + links_section
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.md', 'w') as f:
        f.write(final_content)
        
    with open('templates/mkdocs.yml', 'r') as f:
        mkdocs_content = f.read()
        
    key = "    - LOCATION"
    
    pre_key = mkdocs_content.split(key)[0]
    post_key = mkdocs_content.split(key)[1]
    
    new_content = pre_key + "\n".join(links_yml) + post_key    
    
    with open('mkdocs.yml', 'w') as f:
        f.write(new_content)
    
    print(f"Updated with {len(links)} links")

if __name__ == "__main__":
    update_index()