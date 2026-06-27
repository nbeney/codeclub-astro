new p5(p => {
    let sliderAngle;
    let labelAngle;

    p.setup = function() {
        p.createCanvas(250, 250);

        let divContainer = p.createDiv();
        sliderAngle = p.createSlider(-360, 360, 60, 1).parent(divContainer);
        p.createSpan("   ").parent(divContainer); // spacer
        labelAngle = p.createSpan("???").parent(divContainer);
    }

    function updateSliderAngle() {
        if (p.mouseX >= 0 && p.mouseX < p.width && p.mouseY >= 0 && p.mouseY < p.height) {
            const dx = p.mouseX - p.width/2;
            const dy = p.mouseY - p.height/2;
            const angle = Math.atan2(dy, dx);
            sliderAngle.value(p.degrees(angle));
        }
    }

    p.mousePressed = function() {
        updateSliderAngle();
    }

    p.mouseDragged = function() {
        updateSliderAngle();
    }

    p.draw = function() {
        let diameter = p.height * 0.7;

        let angleDeg = sliderAngle.value();
        let angleRad = p.radians(angleDeg);
        labelAngle.html(`${angleDeg}° = ${angleRad.toFixed(2)} rad`);

        p.background(240);

        p.push();
        p.translate(p.width/2, p.height/2);

        // Draw the angle pie slice.
        p.fill(200, 255, 200); // light green
        p.stroke("green");
        if (angleRad === 0) {
            p.line(0, 0, diameter/2, 0);
        } else {
            let start = (angleRad >= 0) ? 0 : angleRad;
            let stop = (angleRad >= 0) ? angleRad : 0;
            p.arc(0, 0, diameter, diameter, start, stop, p.PIE);
            p.arc(0, 0, diameter/4, diameter/4, start, stop, p.PIE);
        }

        // Draw the circle.
        p.noFill();
        p.stroke(0);
        p.circle(0, 0, diameter);
        for (const pair of [
            [0, "0"], 
            [45, "π/4"], 
            [90, "π/2"],
            [135, "3π/4"],
            [180, "π"],
            [225, "5π/4"],
            [270, "3π/2"],
            [315, "7π/4"]
        ]) {
            let deg = pair[0]
            let rad = pair[1]
            p.push();
            p.rotate(p.radians(deg));
            p.translate(diameter/2, 0);
            p.line(-5, 0, 5, 0);
            p.noStroke();
            p.fill("blue");
            p.textAlign(p.RIGHT, p.CENTER);
            p.text(`${deg}`, -10, 0);
            p.fill("red");
            p.textAlign(p.LEFT, p.CENTER);
            p.text(rad, 10, 0);
            p.pop();
        }

        p.pop();
    }
}, "p5-angles")
