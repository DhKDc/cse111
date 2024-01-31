import math
 
can_title = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
can_radius = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
can_height = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]
can_cost = [0.28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42]
 
def main():
    size=len(can_radius)
    for i in range(size):
        vol = compute_volume(can_radius[i], can_height[i])
        surface_area = compute_surface_area(can_radius[i], can_height[i])
        eficiency= vol/surface_area
        print(f'{can_title[i]} {vol:.2f} {surface_area:.2f} {eficiency:.2f}')
 
def compute_volume(radius, height):
    volume = (math.pi)*(radius ** 2) * (height)
    return volume
 
def compute_surface_area(radius, height):
    surface_area = 2*(math.pi)*(radius)*(radius + height)
    return surface_area

main()