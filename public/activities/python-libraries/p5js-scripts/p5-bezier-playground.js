new p5(p => {
    class Dot {
        constructor(x, y) {
            this.x = x;
            this.y = y;
        }

        show() {
            p.push();
            p.fill(0);
            p.noStroke();
            p.circle(this.x, this.y, 7);
            p.pop();
        }
    }

    let start;
    let stop;
    let cp1;
    let cp2;
    let dots = [];
    let activeDot;

    p.setup = function() {
        p.createCanvas(350, 350);
        start = new Dot(p.width * 0.6, p.height * 0.9);
        stop = new Dot(p.width * 0.4, p.height * 0.9);
        cp1 = new Dot(p.width * 0.1, p.height * 0.1);
        cp2 = new Dot(p.width * 0.9, p.height * 0.1);

        dots = [start, stop, cp1, cp2];
    }

    p.draw = function() {
        p.background(240);

        if (activeDot) {
            p.text(`x: ${activeDot.x.toFixed(0)}, y: ${activeDot.y.toFixed(0)}`, 10, 10);
        }

        p.push();
        p.fill(200, 255, 200); // light green
        p.stroke("red");
        p.strokeWeight(3);
        p.bezier(start.x, start.y, cp1.x, cp1.y, cp2.x, cp2.y, stop.x, stop.y);
        p.pop();

        for (let dot of dots) {
            dot.show();
        }
        p.line(start.x, start.y, cp1.x, cp1.y);
        p.line(stop.x, stop.y, cp2.x, cp2.y);
    }

    p.mousePressed = function() {
        for (let dot of dots) {
            if (p.dist(p.mouseX, p.mouseY, dot.x, dot.y) < 20) {
                activeDot = dot;
                break;
            }
        }
    }

    p.mouseReleased = function() {
        activeDot = null;
    }

    p.mouseDragged = function() {
        if (activeDot) {
            activeDot.x = p.mouseX;
            activeDot.y = p.mouseY;
        }
    }
}, "p5-bezier-playground")
