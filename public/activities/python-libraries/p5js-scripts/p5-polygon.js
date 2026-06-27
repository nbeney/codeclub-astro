new p5(p => {
    let sliderNPoints, labelNPoints;
    let sliderRadius, labelRadius;

    p.setup = function() {
        p.createCanvas(300, 300);

        let divContainer = p.createDiv();

        let divNPoints = p.createDiv().parent(divContainer);
        p.createSpan("Points: ").parent(divNPoints);
        sliderNPoints = p.createSlider(3, 12, 5, 1).parent(divNPoints);
        p.createSpan("   "); // spacer
        labelNPoints = p.createSpan("???").parent(divNPoints);

        let divRadius = p.createDiv().parent(divContainer);
        p.createSpan("Radius: ").parent(divRadius);
        sliderRadius = p.createSlider(10, p.height/2 * 0.8, 120, 5).parent(divRadius);
        p.createSpan("   "); // spacer
        labelRadius = p.createSpan("???").parent(divRadius);
    }

    p.draw = function() {
        const npoints = sliderNPoints.value();
        const radius = sliderRadius.value();

        labelNPoints.html(npoints);
        labelRadius.html(radius);

        p.background(240);

        p.translate(p.width/2, p.height/2);
        p.fill(200, 255, 200);
        p.strokeWeight(3);
        p.beginShape();
        for (let i = 0; i < npoints; i++) {
            let x = radius * p.cos(p.radians(i * 360 / npoints));
            let y = radius * p.sin(p.radians(i * 360 / npoints));
            p.vertex(x, y);
        }
        p.endShape(p.CLOSE);
    }
}, "p5-polygon")
