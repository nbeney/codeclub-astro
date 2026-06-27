/*
from p5 import *
from math import cos, sin

def setup():
    size(300, 300)
    color_mode(HSB)

def draw():
    # frame_count increases by one every time
    angle_rad = radians(frame_count)

    # Calculate the new diameter.
    freq = 1  # change to adjust the speed
    diameter = map(sin(freq * angle_rad), -1, 1, height*0.1, height*0.9)
    
    # Calculate the new color.
    freq = 0.2  # change to adjust the speed
    hue = map(cos(freq * angle_rad), -1, 1, 0, 255)

    # Update the canvas.
    background(240)  # lightgrey
    translate(width/2, height/2)
    fill(hue, 255, 255)
    stroke_weight(3)
    circle(0, 0, diameter)

run()
*/

new p5(p => {
    p.setup = function() {
        p.createCanvas(300, 300);
    }

    p.draw = function() {
        let angle_rad = p.radians(p.frameCount);

        let freq = 1;
        let diameter = p.map(p.sin(freq * angle_rad), -1, 1, p.height*0.1, p.height*0.9);
        
        freq = 0.2;
        let hue = p.map(p.cos(freq * angle_rad), -1, 1, 0, 255);

        p.colorMode(p.RGB);
        p.background(240);
        p.translate(p.width/2, p.height/2);
        p.colorMode(p.HSB);
        p.fill(hue, 255, 255);
        p.strokeWeight(3);
        p.circle(0, 0, diameter);
    }
}, "p5-pulse")
