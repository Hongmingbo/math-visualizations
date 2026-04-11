import os
import re

def fix_linear():
    with open('linear-function-pro.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if we need to adjust scale for text displays
    # Currently linear-function-pro.html uses "mathX" and "mathY" which are already scaled by `scale = 40` (pixels per unit)
    # The displayed texts use (b), (xInt), (-b/k) etc., which are logical units.
    # We should make sure the hover "coords-display" also shows logical units.
    
    # Ensure coords display is correct
    if "const mathX = (pos.x - ox) / scale;" in content:
        # It already uses logical coordinates for the display
        pass

def fix_quadratic():
    with open('quadratic-visualizer.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Quadratic uses logical values a, b, c for its math.
    # The coordinate system maps 1 logical unit to `currentScale` pixels (default 40).
    # The info panel displays a, b, c, and vertex (-b/2a, (4ac-b^2)/4a). These are logical.
    # We need to make sure the tooltip / coords use logical units.
    pass

def fix_trig():
    with open('trigonometry-visualizer.html', 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Trig uses degrees (0-720) for X, and logical amplitude for Y.
    # `xScale = (w - 200) / 720`, `yScale = 60`.
    # Values displayed are logical (amplitude, degrees).
    pass

# We should also check jh-math-models.html again to make sure all lengths are scaled.
def fix_math_models():
    with open('jh-math-models.html', 'r', encoding='utf-8') as file:
        content = file.read()
        
    # K-type (Model 1): no length text displayed
    # Hand-in-hand (Model 2): already scaled in previous step
    # Half-angle (Model 3): EF = BE + DF
    content = content.replace("let EF = dist(E.x, E.y, F.x, F.y).toFixed(1);", "let EF = (dist(E.x, E.y, F.x, F.y)/10).toFixed(1);")
    content = content.replace("let BE = dist(B.x, B.y, E.x, E.y).toFixed(1);", "let BE = (dist(B.x, B.y, E.x, E.y)/10).toFixed(1);")
    content = content.replace("let DF = dist(D.x, D.y, F.x, F.y).toFixed(1);", "let DF = (dist(D.x, D.y, F.x, F.y)/10).toFixed(1);")
    
    # Let's apply it if they exist
    if "let EF =" not in content and "setAttr('m3-eq'" in content:
        # Need to insert the length calculation
        old_eq = "setAttr('m3-eq', {x: 720, y: 250});" # just an anchor
        # We'll just update the text content of m3-eq
        content = content.replace(
            "setAttr('m3-eq', {x: 720, y: 250});",
            "setAttr('m3-eq', {x: 720, y: 250});"
        )
        
        # Look for updateM3 to inject text update
        if "sliderE.value = xE;" in content:
            new_text = """            let EF = (dist(E.x, E.y, F.x, F.y)/10).toFixed(1);
            let BE = (dist(B.x, B.y, E.x, E.y)/10).toFixed(1);
            let DF = (dist(D.x, D.y, F.x, F.y)/10).toFixed(1);
            setText('m3-eq', `EF = ${EF} = BE(${BE}) + DF(${DF})`);
            sliderE.value = xE;"""
            content = content.replace("sliderE.value = xE;", new_text)

    with open('jh-math-models.html', 'w', encoding='utf-8') as file:
        file.write(content)


fix_math_models()
print("Math models scaled.")
