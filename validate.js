const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
for (const file of files) {
    const content = fs.readFileSync(file, 'utf-8');
    
    // Check for common issues
    if (!content.includes('<meta charset="UTF-8"')) {
        console.error(`${file}: Missing meta charset`);
    }
    if (content.includes('eval(')) {
        console.error(`${file}: Contains eval()`);
    }
    if (content.includes('event.target') && !content.includes('function') && !content.match(/\([^)]*e[^)]*\)/) && !content.match(/\([^)]*event[^)]*\)/)) {
        console.error(`${file}: Unsafe event.target`);
    }
    if (content.split('<style>').length !== content.split('</style>').length) {
        console.error(`${file}: Unbalanced style tags`);
    }
    if (content.split('<script>').length !== content.split('</script>').length) {
        console.error(`${file}: Unbalanced script tags`);
    }
}
console.log('Validation complete.');
