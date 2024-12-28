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

export { findJpgPath, findPngPath };
