import re
import json
import os

def parse_poems(file_path):
    poems = []
    current_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Regex for date: Starts with year 20xx, followed by dot or space
    date_pattern = re.compile(r'^\s*20\d{2}[.\s].*$')

    for line in lines:
        # Check if line is a date line
        if date_pattern.match(line):
            date = line.strip()
            
            # Process the collected lines to find Title and Content
            # 1. Trim leading empty lines
            while current_lines and not current_lines[0].strip():
                current_lines.pop(0)
            
            if current_lines:
                # 2. First non-empty line is Title
                title = current_lines[0].strip()
                
                # 3. Rest is content
                # We want to preserve internal formatting, but maybe trim the *very* start/end of the content block?
                # Actually, if there are empty lines between Title and Content, they might be intentional or just separation.
                # Usually one empty line.
                raw_content_lines = current_lines[1:]
                
                # Let's remove *leading* empty lines from content (separation from title)
                # and *trailing* empty lines (separation from date)
                
                start_idx = 0
                while start_idx < len(raw_content_lines) and not raw_content_lines[start_idx].strip():
                    start_idx += 1
                
                end_idx = len(raw_content_lines)
                while end_idx > start_idx and not raw_content_lines[end_idx-1].strip():
                    end_idx -= 1
                
                content_lines = raw_content_lines[start_idx:end_idx]
                content = "".join(content_lines) # Join keeps the newlines from file
                
                poems.append({
                    "title": title,
                    "content": content,
                    "date": date
                })
            
            current_lines = []
        else:
            current_lines.append(line)

    return poems

if __name__ == "__main__":
    input_file = "whole-text"
    output_file = "_data/poems.json"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        exit(1)
        
    data = parse_poems(input_file)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully parsed {len(data)} poems to {output_file}.")
