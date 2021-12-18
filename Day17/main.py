import math as m

def goes_inside(x,y,v_x,v_y,y_min,y_max,x_min,x_max):
    while(1):
        x += v_x
        y += v_y
        if v_x > 0:
            v_x -= 1
        v_y -= 1
        if y >= y_min and y<=y_max and x >= x_min and x <= x_max:
            return True
        if y < y_min:
            return False
        if v_x == 0 and x<x_min:
            return False
        if x>x_max:
            return False
        
        
x_min = 288
x_max = 330
y_min = -96
y_max = -50

x = 0
y = 0

v_x = m.ceil(-1 + m.sqrt(8*x_min + 1 )/2)

max_vel = 1
for i in range(-y_min):
    target = goes_inside(x,y,v_x,i,y_min,y_max,x_min,x_max)
    if target and i > max_vel:
        max_vel = i
        
print(int(max_vel*(max_vel+1)/2))

count = 0
for i in range(x_max+1):
    for j in range(y_min,-y_min):
        target = goes_inside(x,y,i,j,y_min,y_max,x_min,x_max)
        if target:
            count += 1
            
print(count)