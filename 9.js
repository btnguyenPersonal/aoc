const { readFile } = require('fs/promises');

async function getText() {
    return await readFile('./9input', 'utf-8');
}

const dir = {
    UP: 'U',
    DOWN: 'D',
    LEFT: 'L',
    RIGHT: 'R'
};

(async() => {
    const text = await getText();
    const textArray = text.split('\n');
    const directions = textArray.map(function (item) {
        return item.split(' ');
    })
    let pos = [
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000],
        [1000, 1000]
    ];
    let visited = [], temp = [];
    for (let i = 0; i < 2000; i++) {
        temp = [];
        for (let j = 0; j < 2000; j++) {
            temp.push(0);
        }
        visited.push(temp);
    }
    visited[pos[1][1]][pos[1][0]] = 1;
    await directions.forEach(direction => {
        for (let i = 0; i < parseInt(direction[1], 10); i++) {
            switch(direction[0]) {
                case dir.UP:
                    pos[0][1]--;
                    break;
                case dir.DOWN:
                    pos[0][1]++;
                    break;
                case dir.LEFT:
                    pos[0][0]--;
                    break;
                case dir.RIGHT:
                    pos[0][0]++;
                    break;
            }
            for (let person = 0; person < 9; person++) {
                distx = pos[person + 0][0] - pos[person + 1][0];
                disty = pos[person + 0][1] - pos[person + 1][1];
                if (distx > 1 || disty > 1 || distx < -1 || disty < -1) {
                    if (distx > 0) {
                        pos[person + 1][0] += 1;
                    }
                    if (distx < 0) {
                        pos[person + 1][0] -= 1;
                    }
                    if (disty > 0) {
                        pos[person + 1][1] += 1;
                    }
                    if (disty < 0) {
                        pos[person + 1][1] -= 1;
                    }
                }
            }
            visited[pos[9][1]][pos[9][0]] = 1;
        }
    });
    let sum = 0;
    for (let i = 0; i < 2000; i++) {
        for (let j = 0; j < 2000; j++) {
            sum += visited[i][j];
        }
    }
    console.log(sum);
    // let counter = 0;
    // visited.forEach(row => {
    //     process.stdout.write(counter.toString().padStart(4) + ' | ');
    //     counter++;
    //     row.forEach(cell => {
    //         process.stdout.write(cell.toString());
    //     })
    //     console.log();
    // });
})();
