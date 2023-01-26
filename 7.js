#!/usr/bin/env node

const { readFile } = require('fs/promises');

async function getText() {
    return await readFile('./7input', 'utf-8');
}

(async() => {
    const text = await getText();
    const textArray = text.split('\n');
    let counter = 0;
    let dataSize = 0;
    let totalSpace = 70000000;
    let usedSpace = 40528671;
    let segment, line;
    for (let i = 0; i < textArray.length; i++) {
        dataSize = 0;
        segment = textArray[i];
        if (!segment.includes('$ cd ..') && segment.includes('$ cd')) {
            counter = 1;
            for (let j = i + 1; j < textArray.length; j++) {
                line = textArray[j];
                if (counter > 0 && line.includes('$ cd ..')) {
                    counter--;
                } else if (counter > 0 && line.includes('$ cd')) {
                    counter++;
                } else if (counter > 0 && line.match(/^\d/)) {
                    dataSize += parseInt(line.match(/^\d+/), 10)
                }
            }
            if (totalSpace - usedSpace + dataSize >= 30000000) {
                console.log(dataSize, segment);
                // totalSize += dataSize;
            }
        }
    }
    // console.log(totalSize);
})();
