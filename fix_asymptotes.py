import os

files = ['inverse-function.html', 'linear-function-pro.html', 'quadratic-visualizer.html', 'trigonometry-visualizer.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We look for the custom function drawing loop
    # Typical pattern:
    # let first = true;
    # for (let x = -range; x <= range; x += 0.01) {
    #     const y = customFunc(x);
    
    # We'll use a safer regex or string replacement
    
    if "let lastY = null;" not in content and "customFunc(x)" in content:
        # Inverse-function.html specific
        content = content.replace(
"""                let first = true;
                for (let x = -range; x <= range; x += 0.01) {
                    const y = customFunc(x);
                    if (!isNaN(y) && Math.abs(y) <= range) {
                        const px = ox + x * scale;
                        const py = oy - y * scale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                    } else {
                        first = true;
                    }
                }""",
"""                let first = true;
                let lastY = null;
                for (let x = -range; x <= range; x += 0.01) {
                    const y = customFunc(x);
                    if (!isNaN(y) && Math.abs(y) <= range) {
                        if (lastY !== null && Math.abs(y - lastY) > range) first = true;
                        const px = ox + x * scale;
                        const py = oy - y * scale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                        lastY = y;
                    } else {
                        first = true;
                        lastY = null;
                    }
                }""")
        
        # Linear-function-pro.html specific
        content = content.replace(
"""                let first = true;
                for (let x = -10; x <= 10; x += 0.01) {
                    const y = customFunc(x);
                    if (!isNaN(y)) {
                        const px = ox + x * scale;
                        const py = oy - y * scale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                    } else {
                        first = true;
                    }
                }""",
"""                let first = true;
                let lastY = null;
                for (let x = -10; x <= 10; x += 0.01) {
                    const y = customFunc(x);
                    if (!isNaN(y)) {
                        if (lastY !== null && Math.abs(y - lastY) > 10) first = true;
                        const px = ox + x * scale;
                        const py = oy - y * scale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                        lastY = y;
                    } else {
                        first = true;
                        lastY = null;
                    }
                }""")

        # Quadratic-visualizer.html specific
        content = content.replace(
"""                let first = true;
                for (let x = -10; x <= 10; x += 0.05) {
                    const y = customFunc(x);
                    if (!isNaN(y)) {
                        const px = ox + x * currentScale;
                        const py = oy - y * currentScale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                    } else {
                        first = true;
                    }
                }""",
"""                let first = true;
                let lastY = null;
                for (let x = -10; x <= 10; x += 0.05) {
                    const y = customFunc(x);
                    if (!isNaN(y)) {
                        if (lastY !== null && Math.abs(y - lastY) > 10) first = true;
                        const px = ox + x * currentScale;
                        const py = oy - y * currentScale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                        lastY = y;
                    } else {
                        first = true;
                        lastY = null;
                    }
                }""")

        # Trigonometry-visualizer.html specific
        content = content.replace(
"""            if (customFunc) {
                ctx.beginPath();
                ctx.strokeStyle = '#e74c3c';
                ctx.lineWidth = 2;
                let first = true;
                for (let x = 0; x <= 720; x += 2) {
                    const rad = x * Math.PI / 180;
                    const y = customFunc(rad);
                    if (!isNaN(y) && isFinite(y)) {
                        const px = ox + x * xScale;
                        const py = oy - y * yScale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                    } else {
                        first = true;
                    }
                }
                ctx.stroke();
            }""",
"""            if (customFunc) {
                ctx.beginPath();
                ctx.strokeStyle = '#e74c3c';
                ctx.lineWidth = 2;
                let first = true;
                let lastY = null;
                for (let x = 0; x <= 720; x += 2) {
                    const rad = x * Math.PI / 180;
                    const y = customFunc(rad);
                    if (!isNaN(y) && isFinite(y)) {
                        if (lastY !== null && Math.abs(y - lastY) > 10) first = true;
                        const px = ox + x * xScale;
                        const py = oy - y * yScale;
                        if (first) { ctx.moveTo(px, py); first = false; }
                        else { ctx.lineTo(px, py); }
                        lastY = y;
                    } else {
                        first = true;
                        lastY = null;
                    }
                }
                ctx.stroke();
            }""")

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Asymptote fix applied.")
