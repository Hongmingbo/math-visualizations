import os

def fix_inverse():
    with open('inverse-function.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Safe parseFunction
    old_parse = """        function parseFunction(expr) {
            expr = expr.replace(/\s/g, '').replace(/\^/g, '**');
            return (x) => {
                try {
                    const keys = Object.getOwnPropertyNames(Math);
                    const values = keys.map(k => Math[k]);
                    const f = new Function(...keys, 'x', `return ${expr};`);
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
                f(...values, 1); // test
                return (x) => {
                    try { return f(...values, x); }
                    catch(e) { return NaN; }
                };
            } catch(e) {
                return null;
            }
        }"""
    
    content = content.replace(old_parse, new_parse)

    # Stop animation on interaction
    content = content.replace("document.getElementById('k').addEventListener('input', draw);", "document.getElementById('k').addEventListener('input', () => { if(isAnimating) toggleAnimation(); draw(); });")
    content = content.replace("function setK(val) {\n            document.getElementById('k').value = val;\n            draw();\n        }", "function setK(val) {\n            if(isAnimating) toggleAnimation();\n            document.getElementById('k').value = val;\n            draw();\n        }")
    content = content.replace("function randomK() {\n            let val = (Math.random() * 10 - 5).toFixed(1);\n            if (Math.abs(val) < 0.1) val = 1.0;\n            document.getElementById('k').value = val;\n            draw();\n        }", "function randomK() {\n            if(isAnimating) toggleAnimation();\n            let val = (Math.random() * 10 - 5).toFixed(1);\n            if (Math.abs(val) < 0.1) val = 1.0;\n            document.getElementById('k').value = val;\n            draw();\n        }")
    content = content.replace("isDragging = true;", "isDragging = true;\n            if(isAnimating) toggleAnimation();")

    with open('inverse-function.html', 'w', encoding='utf-8') as f:
        f.write(content)

def fix_linear():
    with open('linear-function-pro.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Safe parseFunction
    old_parse = """        function parseFunction(expr) {
            expr = expr.replace(/\s/g, '').replace(/\^/g, '**');
            return (x) => {
                try {
                    const keys = Object.getOwnPropertyNames(Math);
                    const values = keys.map(k => Math[k]);
                    const f = new Function(...keys, 'x', `return ${expr};`);
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

    with open('linear-function-pro.html', 'w', encoding='utf-8') as f:
        f.write(content)

fix_inverse()
fix_linear()
print("Fixed inverse and linear.")
