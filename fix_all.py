import os
import re

def fix_quadratic():
    with open('quadratic-visualizer.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add stop animation call
    content = content.replace("function setExample(a, b, c) {", "function setExample(a, b, c) {\n            if (animReq) toggleAnimation();")
    content = content.replace("document.getElementById('c').addEventListener('input', draw);", "document.getElementById('c').addEventListener('input', () => { if(animReq) toggleAnimation(); draw(); });")
    content = content.replace("document.getElementById('a').addEventListener('input', draw);", "document.getElementById('a').addEventListener('input', () => { if(animReq) toggleAnimation(); draw(); });")
    content = content.replace("document.getElementById('b').addEventListener('input', draw);", "document.getElementById('b').addEventListener('input', () => { if(animReq) toggleAnimation(); draw(); });")
    content = content.replace("if (dist < 20) {", "if (dist < 20) {\n                if(animReq) toggleAnimation();")

    with open('quadratic-visualizer.html', 'w', encoding='utf-8') as f:
        f.write(content)

def fix_trig():
    with open('trigonometry-visualizer.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix parseFunction
    old_parse = """        function parseFunction(expr) {
            const cleanExpr = expr.replace(/\s/g, '').replace(/\^/g, '**');
            return (x) => {
                try {
                    const keys = Object.getOwnPropertyNames(Math);
                    const values = keys.map(k => Math[k]);
                    const f = new Function(...keys, 'x', `return ${cleanExpr};`);
                    return f(...values, x);
                } catch(e) { return NaN; }
            };
        }"""
    
    new_parse = """        function parseFunction(expr) {
            const cleanExpr = expr.replace(/\s/g, '').replace(/\^/g, '**');
            try {
                const keys = Object.getOwnPropertyNames(Math);
                const values = keys.map(k => Math[k]);
                const f = new Function(...keys, 'x', `return ${cleanExpr};`);
                f(...values, 0); // test
                return (x) => {
                    try { return f(...values, x); }
                    catch(e) { return NaN; }
                };
            } catch(e) {
                return null;
            }
        }"""
    
    content = content.replace(old_parse, new_parse)

    # Apply custom alert
    old_apply = """        function applyCustom() {
            const input = document.getElementById('custom-input').value;
            if (!input) { clearCustom(); return; }
            customExpr = input;
            customFunc = parseFunction(input);
            draw();
        }"""
    
    new_apply = """        function applyCustom() {
            const input = document.getElementById('custom-input').value;
            if (!input) { clearCustom(); return; }
            customExpr = input;
            const parsed = parseFunction(input);
            if (parsed) {
                customFunc = parsed;
                draw();
            } else {
                alert("函数解析失败，请检查语法！");
            }
        }"""
    content = content.replace(old_apply, new_apply)

    # Stop animation on drag
    content = content.replace("isDraggingAngle = true;", "isDraggingAngle = true;\n                if(animReq) toggleAnimation();")
    content = content.replace("isDraggingGraphPoint = true;", "isDraggingGraphPoint = true;\n                if(animReq) toggleAnimation();")
    content = content.replace("document.getElementById('angle').addEventListener('input', draw);", "document.getElementById('angle').addEventListener('input', () => { if(animReq) toggleAnimation(); draw(); });")

    with open('trigonometry-visualizer.html', 'w', encoding='utf-8') as f:
        f.write(content)

fix_quadratic()
fix_trig()
print("Fixed quadratic and trig.")
