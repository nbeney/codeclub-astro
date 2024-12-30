from p5 import *
from math import *

def setup():
    global FUNCTIONS
    FUNCTIONS = [
        draw_france,
        draw_south_africa,
        draw_greenland,
        draw_seychelles,
        draw_united_states,
        draw_antigua_barbuda,
        draw_panama,
        draw_marshalls_islands,
        draw_burundi,
        draw_north_macedonia,
        draw_bahrain,
    ]

    size(600, 400)
    FUNCTIONS[0]()
    
def draw():
    FUNCTIONS[frame_count % len(FUNCTIONS)]()
    
def draw_france():
    third = width / 3
    
    background("white")
    no_stroke()
    fill("blue")
    rect(0, 0, third, height)
    fill("red")
    rect(2*third, 0, third, height)

def draw_south_africa():
    ratio = width / 600
    angle = PI/4 * 3.1
    thickness = 80 * ratio
    gap_x = 35 * ratio
    gap_y = 20 * ratio
    
    background("white")
    no_stroke()

    fill("green")
    rect(0, height/2 - thickness/2, width, thickness)
    arc(width/2, height/2, 1000, 1000, +angle, -angle)
    
    fill("yellow")
    arc(width/2 * 0.65, height/2, 1000, 1000, +angle, -angle)
    
    fill("black")
    arc(width/2 * 0.55, height/2, 1000, 1000, +angle, -angle)
    
    fill("red")
    arc(width/2 - gap_x, height/2 - thickness/2 - gap_y, 1000, 1000, -angle, 0)
    
    fill("blue")
    arc(width/2 - gap_x, height/2 + thickness/2 + gap_y, 1000, 1000, 0, +angle)

def draw_greenland():
    cx = width * 0.35
    cy = height/2
    radius = height * 0.7
    
    background("white")
    no_stroke()

    fill("red")
    rect(0, height/2, width, height)
    arc(cx, cy, radius, radius, PI, 0)

    fill("white")
    arc(cx, cy, radius, radius, 0, PI)

def draw_seychelles():
    cx = 0
    cy = height
    diameter = 3*width
    colors = ["blue", "yellow", "red", "white", "green"]
    weights = [3, 2, 3, 1.5, 1.5]
    total = sum(weights)
    percents = [_ / total for _ in weights]
    angles = [PI/2 * _ for _ in percents]
    
    background("grey")
    no_stroke()

    last = -PI/2
    for (color, angle) in zip(colors, angles):
        fill(color)
        arc(cx, cy, diameter, diameter, last, last + angle)
        last += angle

def draw_united_states():
    background("white")
    no_stroke()

    # Draw the stripes
    num_reds = 7
    num_whites = num_reds - 1
    num_stripes = num_reds + num_whites
    thickness = height / num_stripes
    for i in range(0, num_reds):
        fill("red")
        rect(0, i * 2 * thickness, width, thickness)

    # Draw the blue rectangle
    fill("blue")
    rect_width = width * 0.4
    rect_height = height/2 + thickness/2
    rect(0, 0, rect_width, rect_height)

    # Draw the stars
    fill("white")
    radius = 7 * width / 600
    
    num_rows = 9
    margin_y = rect_height * 0.05
    gap_y = (rect_height - 2*margin_y - num_rows*2*radius) / (num_rows - 1)

    num_cols = 6
    margin_x = rect_width * 0.05
    gap_x = (rect_width - 2*margin_x - num_cols*2*radius) / (num_cols - 1)
    
    for row in range(0, num_rows):
        cy = margin_y + radius + row * (2*radius + gap_y)

        if row % 2 == 0:
            num_cols = 6
            margin_x_adj = margin_x
        else:
            num_cols = 5
            margin_x_adj = (rect_width - num_cols*2*radius - (num_cols-1)*gap_x) / 2
        
        for col in range(0, num_cols):
            cx = margin_x_adj + radius + col * (2*radius + gap_x)
            star(5, cx, cy, radius)

def draw_antigua_barbuda():
    background("black")
    no_stroke()

    fill("yellow")
    star(16, width/2, 2*height/6, height/4)

    fill("dodgerblue")
    rect(0, 2*height/6, width, height/5)

    fill("white")
    rect(0, 2*height/6 + height/5, width, height)

    fill("red")
    triangle(0, 0, 0, height, width/2, height)
    triangle(width, 0, width, height, width/2, height)

def draw_panama():
    background("white")
    no_stroke()

    radius = 60

    fill("blue")
    rect(0, height/2, width/2, height/2)
    star(5, width/4, height/4, radius)

    fill("red")
    rect(width/2, 0, width/2, height/2)
    star(5, 3*width/4, 3*height/4, radius)

def draw_marshalls_islands():
    background("mediumblue")
    no_stroke()

    radius = 60 * width / 600

    # Draw the star
    fill("white")
    cx = width/5
    cy = height/3
    radius = height/4
    star(24, cx, cy, radius * 0.7)
    star(4, cx, cy, radius, ratio=0.05)

    # Draw the stripes
    h = height/6
    fill("orange")
    triangle(0, height, width, 0, width, h)
    fill("white")
    triangle(0, height, width, h, width, 2*h)

def draw_burundi():
    background("white")
    no_stroke()

    gap = 20
    
    # Draw the triangles
    fill("green")
    triangle(width/2 - gap, height/2, 0, gap, 0, height - gap)
    triangle(width/2 + gap, height/2, width, gap, width, height - gap)
    fill("red")
    triangle(width/2, height/2 - gap, gap, 0, width - gap, 0)
    triangle(width/2, height/2 + gap, gap, height, width - gap, height)

    # Draw the circle
    fill("white")
    diameter = height / 2
    push_matrix()
    translate(width/2, height/2)
    circle(0, 0, diameter)
    fill("red")
    stroke("green")
    stroke_weight(2)
    star(6, 0, -40, height/15, ratio=0.58)
    star(6, -40, 30, height/15, ratio=0.58)
    star(6, +40, 30, height/15, ratio=0.58)
    pop_matrix()

def draw_north_macedonia():
    background("red")
    no_stroke()

    side = 60

    # Draw the beams
    fill("yellow")
    triangle(width/2, height/2, 0, 0, side, 0)
    triangle(width/2, height/2, width, 0, width - side, 0)
    triangle(width/2, height/2, 0, height, side, height)
    triangle(width/2, height/2, width, height, width - side, height)
    triangle(width/2, height/2, 0, height/2 - side/2, 0, height/2 + side/2)
    triangle(width/2, height/2, width, height/2 - side/2, width, height/2 + side/2)    
    triangle(width/2, height/2, width/2 - side/2, 0, width/2 + side/2, 0)
    triangle(width/2, height/2, width/2 - side/2, height, width/2 + side/2, height)
    
    # Draw the circle
    fill("yellow")
    stroke("red")
    stroke_weight(5)
    circle(width/2, height/2, height/7)

def draw_bahrain():
    background("red")
    no_stroke()

    fill("white")
    rect(0, 0, width/4, height)

    h = height/5
    for i in range(5):
        x1 = width/4 - 1
        x2 = x1 + width/8
        y = i * h
        triangle(x1, y, x1, y + h, x2, y + h/2)


def star(n, cx, cy, radius, ratio=0.4, angle=0):
    external_radius = radius
    internal_radius = external_radius * ratio
    delta = PI / n 
    
    push_matrix()
    translate(cx, cy)
    rotate(angle)
    
    begin_shape()
    for i in range(n):
        a = -PI/2 + i * 2*PI / n
        b = a + delta
        vertex(external_radius * cos(a), external_radius * sin(a))
        vertex(internal_radius * cos(b), internal_radius * sin(b))
    end_shape(CLOSE)

    pop_matrix()

run(frame_rate=0.5)