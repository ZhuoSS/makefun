import os

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(out_dir, exist_ok=True)

file_path = os.path.join(out_dir, 'entry.txt')
content = "I asked my agent to think outside the box. It spent four hours building a box, then asked me to think inside it."

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)