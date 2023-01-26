#!/usr/bin/env node

const { readFile } = require('fs/promises');

async function getText() {
    return await readFile('./8input', 'utf-8');
}

(async() => {
    const text = await getText();
    const textArray = text.split('\n');
    const trees = textArray.map(function (item) {
        return item.split('').map(Number);
    })
    let canSee = false, temp = true;
    let numVisibleTrees = 0;
    let scenicView = 0;
    for (let i = 1; i < trees.length - 1; i++) {
        for (let j = 1; j < trees[i].length - 1; j++) {
            canSee = false;
            const directions = [
                [0, 1],
                [1, 0],
                [0, -1],
                [-1, 0],
            ]
            // process.stdout.write(trees[i][j].toString() + ' | ');
            process.stdout.write('expr ');
            directions.forEach(dir => {
                scenicView = 0;
                let k = 1;
                temp = true;
                while (i + dir[0] * k < trees.length
                    && i + dir[0] * k >= 0
                    && j + dir[1] * k < trees.length
                    && j + dir[1] * k >= 0) {
                    if (trees[i + dir[0] * k][j + dir[1] * k] >= trees[i][j]) {
                        scenicView++;
                        temp = false;
                        break;
                    } else {
                        scenicView++;
                    }
                    k++;
                }
                process.stdout.write(scenicView.toString() + ' \\\* ');
                if (temp) {
                    canSee = true;
                }
            });
            process.stdout.write('1');
            console.log();
            // console.log(trees[i][j], canSee);
            canSee && numVisibleTrees++;
        }
    }
    console.log(numVisibleTrees + 2 * trees.length + 2 * trees[0].length - 4);
})();

// run with node 8.js | sh | sort -n
