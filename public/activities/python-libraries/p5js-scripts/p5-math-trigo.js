let sliderAngle;
let checkboxSchoolMode;

new p5(p => {
    p.setup = function() {
        p.createCanvas(300, 300);
    }

    function updateSliderAngle() {
        if (p.mouseX >= 0 && p.mouseX < p.width && p.mouseY >= 0 && p.mouseY < p.height) {
            const dx = p.mouseX - p.width/2;
            const dy = adjustForSchoolMode(p.mouseY - p.height/2);
            const angle = (Math.atan2(dy, dx) + p.TWO_PI) % p.TWO_PI; // avoid -ve values b/c of the slider
            sliderAngle.value(p.degrees(angle));
        }
    }

    p.mousePressed = function() {
        updateSliderAngle();
    }

    p.mouseDragged = function() {
        updateSliderAngle();
    }

    function adjustForSchoolMode(y) {
        let mult = checkboxSchoolMode.checked() ? -1 : +1;
        return mult * y;
    }

    p.draw = function() {
        const angle = p.radians(sliderAngle.value()) % p.TWO_PI;
        const radius = p.height/2.5;
        const diameter = 2 * radius;
        const x = Math.cos(angle);
        const y = Math.sin(angle);

        p.background(240);
        p.push();
        
        p.translate(p.width/2, p.height/2);
        
        // Draw the axis.
        p.textAlign(p.LEFT, p.CENTER);
        p.line(-p.width/2, 0, p.width/2, 0);
        p.text("x", p.width/2-10, 10);
        p.text("-1", -radius-15, -10);
        p.text("+1", radius+3, -10);
        p.line(0, p.height/2, 0, -p.height/2);
        p.text("y", 5, adjustForSchoolMode(p.height/2-8));
        p.text("-1", -15, adjustForSchoolMode(-radius-10));
        p.text("+1", -18, adjustForSchoolMode(radius+10));
        
        // Draw the circle.
        p.noFill();
        p.circle(0, 0, diameter);
        
        // Draw the radius and the angle.
        p.stroke("green");
        p.line(0, 0, x*radius, adjustForSchoolMode(y*radius));
        if (checkboxSchoolMode.checked()) {
            p.arc(0, 0, radius/2, radius/2, -angle, 0);
        } else {
            p.arc(0, 0, radius/2, radius/2, 0, angle);
        }
        p.textAlign(p.CENTER, p.CENTER);
        p.text("a", 1.5 * radius/4 * Math.cos(angle/2), adjustForSchoolMode(1.5 * radius/4 * Math.sin(angle/2)));
        
        // Draw the cos.
        p.stroke("red");
        p.line(0, adjustForSchoolMode(radius*y), radius*x, adjustForSchoolMode(radius*y));
        p.textAlign(p.CENTER, p.CENTER);
        p.text("x", radius*x/2, adjustForSchoolMode(radius*y-10));
        
        // Draw the sin.
        p.stroke("blue");
        p.line(radius*x, 0, radius*x, adjustForSchoolMode(radius*y));
        p.textAlign(p.LEFT, p.CENTER);
        p.text("y", radius*x+10, adjustForSchoolMode(radius*y/2));

        // Draw the legend.
        p.textAlign(p.LEFT, p.BOTTOM);
        p.stroke("green");
        let a = (p.degrees(angle) + 360) % 360;
        p.text(`a = ${a.toFixed(0)}`, -p.width/2+10, p.height/2-40);
        p.stroke("red");
        p.text(`x = cos(a) = ${x.toFixed(2)}`, -p.width/2+10, p.height/2-25);
        p.stroke("blue");
        p.text(`y = sin(a) = ${y.toFixed(2)}`, -p.width/2+10, p.height/2-10);

        p.pop();
    }
}, "p5-trigo")
