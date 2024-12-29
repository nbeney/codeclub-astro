function findJpgPath(pattern) {
    const paths = import.meta.glob('/src/assets/images/**/*.jpg');
    const key = Object.keys(paths).find((key) => key.includes(pattern));
    if (!key) throw new Error(`"${pattern}" does not exist in glob: "/src/pages/**/*.jpg"`);
    return paths[key]();
}

function findPngPath(pattern) {
    const paths = import.meta.glob('/src/assets/images/**/*.png');
    const key = Object.keys(paths).find((key) => key.includes(pattern));
    if (!key) throw new Error(`"${pattern}" does not exist in glob: "/src/pages/**/*.png"`);
    return paths[key]();
}

function nextId(seqName) {
    if (!nextId.map) nextId.map = new Map();
    if (!nextId.map.has(seqName)) nextId.map.set(seqName, 0);
    nextId.map.set(seqName, nextId.map.get(seqName) + 1);
    return nextId.map.get(seqName);
}

export { findJpgPath, findPngPath, nextId };
