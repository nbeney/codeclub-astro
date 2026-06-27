new p5(p => {
    let sliderAmp;
    let labelAmp;
    let sliderFreq;
    let labelFreq;
    let labelAngle;

    p.setup = function() {
        p.createCanvas(600, 300);

        const divContainer = p.createDiv();

        const divAmp = p.createDiv("Amplitude: ").parent(divContainer);
        sliderAmp = p.createSlider(-0.4 * p.height, 0.4 * p.height, 0.4 * p.height, 1).parent(divAmp);
        p.createSpan("     ").parent(divAmp); // spacer
        labelAmp = p.createSpan("???").parent(divAmp);

        const divFreq = p.createDiv("Frequency: ").parent(divContainer);
        sliderFreq = p.createSlider(0.1, 10, 1, 0.1).parent(divFreq);
        p.createSpan("     ").parent(divAmp); // spacer
        labelFreq = p.createSpan("???").parent(divFreq);

        const divAngle = p.createDiv("Angle: ").parent(divContainer);
        sliderAngle = p.createSlider(0, p.width, 60, 1).parent(divAngle);
        p.createSpan("     ").parent(divAmp); // spacer
        labelAngle = p.createSpan("???").parent(divAngle);

        checkboxSchoolMode = p.createCheckbox("School mode (y-axis up, angles counter-clockwise)", false).parent(divContainer);
    }

    function updateSliderAngle() {
        if (p.mouseX >= 0 && p.mouseX < p.width && p.mouseY >= 0 && p.mouseY < p.height) {
            sliderAngle.value(p.mouseX);
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
        const freq = sliderFreq.value();
        const amp = sliderAmp.value();
        const angleDeg = sliderAngle.value();
        const angleRad = p.radians(angleDeg);

        labelAmp.html(amp.toFixed(1));
        labelFreq.html(freq.toFixed(1));
        labelAngle.html(angleDeg.toFixed(1));
        
        p.background(240);

        p.push();
        p.translate(0, p.height/2);
        
        // Draw the axis.
        p.textAlign(p.LEFT, p.CENTER);
        p.line(0, 0, p.width, 0);
        p.text("x", p.width-10, 10);
        p.line(1, p.height/2, 1, -p.height/2);
        p.text("y", 5, adjustForSchoolMode(p.height/2-8));
        
        // Draw the cos graph.
        p.stroke("red");
        let dx = 2;
        let px, py;
        for (let x = 0; x < p.width; x += dx) {
            let y = amp * Math.cos(p.radians(freq * x));
            if (px !== undefined) {
                p.line(px, adjustForSchoolMode(py), x, adjustForSchoolMode(y));
            }
            px = x;
            py = y;
        }
        
        // Draw the sin graph.
        p.stroke("blue");
        px = undefined;
        py = undefined;
        for (let x = 0; x < p.width; x += dx) {
            let y = amp * Math.sin(p.radians(freq * x));
            if (px !== undefined) {
                p.line(px, adjustForSchoolMode(py), x, adjustForSchoolMode(y));
            }
            px = x;
            py = y;
        }
        
        // Draw the global angle.
        yCos = amp * Math.cos(freq * angleRad);
        ySin = amp * Math.sin(freq * angleRad);
        p.stroke("grey");
        p.line(angleDeg, -p.height/2, angleDeg, p.height/2);
        p.push();
        p.strokeWeight(7);
        p.stroke("red");
        p.point(angleDeg, adjustForSchoolMode(yCos));
        p.stroke("blue");
        p.point(angleDeg, adjustForSchoolMode(ySin));
        p.pop();
        
        // Draw the legend.
        p.textAlign(p.RIGHT, p.BOTTOM);
        p.stroke("red");
        p.text(`y = amp * cos(freq * x)`, p.width/2-10, p.height/2-8);
        p.textAlign(p.LEFT, p.BOTTOM);
        p.stroke("blue");
        p.text(`y = amp * sin(freq * x)`, p.width/2+10, p.height/2-8);

        p.pop();
    }
}, "p5-cos-sin")
