import os
import json
import shutil
from parse_poems import parse_poems

def build_site():
    # 1. Prepare Output Directory
    # We use 'docs' for GitHub Pages compatibility
    output_dir = "docs"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # 2. Copy Assets
    shutil.copytree("assets", os.path.join(output_dir, "assets"))
    
    # 3. Get Data
    poems = parse_poems("whole-text")
    
    # 4. Generate Content
    # Cover
    html_content = []
    html_content.append('<section class="cover">')
    html_content.append('  <h1 class="site-title">减五度 诗</h1>')
    html_content.append('</section>')
    
    # TOC
    html_content.append('<nav class="toc" id="toc">')
    html_content.append('  <h2>目录</h2>')
    html_content.append('  <ul>')
    for i, poem in enumerate(poems):
        idx = i + 1
        html_content.append(f'    <li><a href="#poem-{idx}">{poem["title"]}</a></li>')
    html_content.append('  </ul>')
    html_content.append('</nav>')
    
    # Poems
    html_content.append('<main class="poems-container">')
    for i, poem in enumerate(poems):
        idx = i + 1
        html_content.append(f'    <article id="poem-{idx}" class="poem">')
        html_content.append('      <header class="poem-header">')
        html_content.append(f'        <h2 class="poem-title">{poem["title"]}</h2>')
        html_content.append('      </header>')
        html_content.append(f'      <div class="poem-content">{poem["content"]}</div>')
        html_content.append('      <footer class="poem-footer">')
        html_content.append(f'        <span class="poem-date">{poem["date"]}</span>')
        html_content.append('      </footer>')
        html_content.append('    </article>')
    html_content.append('</main>')

    # Back to TOC Button
    html_content.append('<a href="#toc" class="back-to-toc" title="回到目录">↑</a>')
    
    inner_content = "\n".join(html_content)
    
    # 5. Apply Layout
    with open("_layouts/default.html", "r", encoding="utf-8") as f:
        layout = f.read()
        
    # Simple template replacement
    # Remove Liquid tags if any remain (I used {{ content }} and {{ site.title }})
    # Note: relative_url filter in layout needs handling
    
    # Replace {{ site.title }}
    layout = layout.replace('{{ site.title }}', '减五度 诗')
    
    # Replace {{ "/assets/css/style.css" | relative_url }}
    # We assume root, so just assets/css/style.css
    layout = layout.replace('{{ "/assets/css/style.css" | relative_url }}', 'assets/css/style.css')
    
    # Replace {{ content }}
    final_html = layout.replace('{{ content }}', inner_content)
    
    # 6. Write Index
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Site built successfully in {output_dir}")

if __name__ == "__main__":
    build_site()
