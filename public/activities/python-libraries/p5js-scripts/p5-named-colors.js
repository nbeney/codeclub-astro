const colorNames = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet",
    "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue",
    "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
    "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet",
    "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro",
    "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew", "hotpink", "indianred", "indigo", "ivory",
    "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow",
    "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey",
    "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid",
    "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream",
    "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod",
    "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown",
    "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray",
    "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow",
    "yellowgreen",
]

function getRGB(color) {
    // Create a temporary element to apply the color
    const tempElement = document.createElement('div');
    tempElement.style.color = color;
    tempElement.style.visibility = 'hidden';
    document.body.appendChild(tempElement);

    // Get the computed color style
    const rgbColor = window.getComputedStyle(tempElement).color;

    // Remove the temporary element
    document.body.removeChild(tempElement);

    // Extract RGB values
    const match = rgbColor.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    if (match) {
        return [parseInt(match[1]), parseInt(match[2]), parseInt(match[3])];
    } else {
        return null;
    }
}

function getContrastColor(color) {
    const rgb = getRGB(color);
    if (!rgb) return null;

    // Calculate relative luminance
    const luminance = (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]) / 255;

    // Check if luminance is above a certain threshold
    return luminance > 0.5 ? 'black' : 'white';
}

function generateNamedColorsTable(containerId) {
    const colorList = document.getElementById(containerId);

    const container = document.createElement("div");
    container.classList.add("container");
    colorList.appendChild(container);

    const row = document.createElement("div");
    row.classList.add("row", "row-cols-2", "row-cols-sm-3", "row-cols-md-4", "row-cols-lg-5", "row-cols-xl-6", "g-1");
    container.appendChild(row);

    for (const colorName of colorNames) {
        const col = document.createElement("div");
        col.classList.add("col");
        const colorBox = document.createElement("div");
        colorBox.classList.add("color-box");
        colorBox.style.backgroundColor = colorName;
        colorBox.style.color = getContrastColor(colorName);
        colorBox.style.border = "solid black 1px";
        colorBox.style.textAlign = "center";
        colorBox.textContent = colorName;
        col.appendChild(colorBox);
        row.appendChild(col);
    }
}