import os

files = ['jh-circle-visualizer.html', 'jh-math-models.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Scale down distances by a factor (e.g. 0.1) for display purposes
    # For jh-circle-visualizer.html
    if f == 'jh-circle-visualizer.html':
        content = content.replace("distEl.textContent = d.toFixed(1);", "distEl.textContent = (d/10).toFixed(1);")
        content = content.replace("distEl.textContent = r.toFixed(1);", "distEl.textContent = (r/10).toFixed(1);")
        content = content.replace("document.getElementById('t3-am').textContent = dx.toFixed(1);", "document.getElementById('t3-am').textContent = (dx/10).toFixed(1);")
        content = content.replace("document.getElementById('t3-mb').textContent = dx.toFixed(1);", "document.getElementById('t3-mb').textContent = (dx/10).toFixed(1);")
        content = content.replace("document.getElementById('t4-pa').textContent = tangentLen.toFixed(1);", "document.getElementById('t4-pa').textContent = (tangentLen/10).toFixed(1);")
        content = content.replace("document.getElementById('t4-pb').textContent = tangentLen.toFixed(1);", "document.getElementById('t4-pb').textContent = (tangentLen/10).toFixed(1);")
        content = content.replace('<span class="data-value">150</span>', '<span class="data-value">12.0</span>') # R=120, so 120/10 = 12.0
    
    # For jh-math-models.html
    if f == 'jh-math-models.html':
        content = content.replace("setText('m2-lenText', `BD = ${lenBD}   CE = ${lenBD}`);", "setText('m2-lenText', `BD = ${(dist(B.x, B.y, D.x, D.y)/10).toFixed(1)}   CE = ${(dist(B.x, B.y, D.x, D.y)/10).toFixed(1)}`);")
        content = content.replace("let sum = (d1 + d2).toFixed(1);", "let sum = ((d1 + d2)/10).toFixed(1);")
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Scale fix applied.")
