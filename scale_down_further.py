import os

files = ['jh-circle-visualizer.html', 'jh-math-models.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace /10 or / 10 with /40
    content = content.replace("/10).toFixed", "/40).toFixed")
    content = content.replace("/ 10).toFixed", "/ 40).toFixed")
    
    # Also fix the hardcoded "12.0" to "3.0" since R=120, 120/40 = 3.0
    content = content.replace('<span class="data-value">12.0</span>', '<span class="data-value">3.0</span>')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Scale updated to /40.")
