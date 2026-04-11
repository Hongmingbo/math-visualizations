import os

files = ['inverse-function.html', 'linear-function-pro.html', 'quadratic-visualizer.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_apply = """        function applyCustom() {
            const input = document.getElementById('custom-input').value;
            if (!input) { clearCustom(); return; }
            customFunc = parseFunction(input);
            draw();
        }"""
        
    new_apply = """        function applyCustom() {
            const input = document.getElementById('custom-input').value;
            if (!input) { clearCustom(); return; }
            const parsed = parseFunction(input);
            if (parsed) {
                customFunc = parsed;
                draw();
            } else {
                alert("函数解析失败，请检查语法！例如: 2*x + 1");
            }
        }"""
    
    content = content.replace(old_apply, new_apply)
    
    # Quadratic has a slightly different one
    old_apply2 = """        function applyCustom() {
            const input = document.getElementById('custom-input').value;
            if (!input) { clearCustom(); return; }
            customExpr = input;
            customFunc = parseFunction(input);
            draw();
        }"""
        
    new_apply2 = """        function applyCustom() {
            const input = document.getElementById('custom-input').value;
            if (!input) { clearCustom(); return; }
            customExpr = input;
            const parsed = parseFunction(input);
            if (parsed) {
                customFunc = parsed;
                draw();
            } else {
                alert("函数解析失败，请检查语法！例如: x**2 + 2*x");
            }
        }"""
        
    content = content.replace(old_apply2, new_apply2)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Alert fix applied.")
