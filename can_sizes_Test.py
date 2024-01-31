def compute_volume(radius, height):
    size = len(radius)
    volume = []
    for i in range(size):
        v = (math.pi *(radius[i] ** 2)) * height[i]
        volume.append(v)
    return volume

def main(name, radius, height, cost_per_can):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    cost_efficiency = compute_cost_efficiency(volume, cost_per_can)
    position_1, best_storage_efficiency = compute_best_storage_efficiency(storage_efficiency)
    position_2, best_cost_efficiency = compute_best_cost_efficiency(cost_efficiency)
    display_results = compute_and_display_results(name, storage_efficiency, cost_efficiency, position_1, position_2)
    return print("Thank you!")
 
def compute_volume(radius, height):
    size = len(radius)
    volume = []
    for i in range(size):
        v = (math.pi *(radius[i] ** 2)) * height[i]
        volume.append(v)
    return volume
 
def compute_surface_area(radius, height):
    size = len(radius)
    surface_area = []
    for i in range(size):
        s = (math.pi*2) * radius[i] * (radius[i] + height[i])
        surface_area.append(s)
    return surface_area
 
def compute_storage_efficiency(volume, surface_area):
    size = len(volume)
    storage_efficiency = []
    for i in range(size):
        s = volume[i] / surface_area[i]
        storage_efficiency.append(s)
    return storage_efficiency
 
def compute_cost_efficiency(volume, cost_per_can):
    size = len(volume)
    cost_efficiency = []
    for i in range(size):
        c = volume[i] / cost_per_can[i]
        cost_efficiency.append(c)
    return cost_efficiency
 
def compute_best_storage_efficiency(storage_efficiency):
    best_storage_efficiency = 0
    n = len(storage_efficiency)
    for i in storage_efficiency:
        if i > best_storage_efficiency:
            best_storage_efficiency = i
    for i in range(n):
        if best_storage_efficiency == storage_efficiency[i]:
            position = i
    return position, best_storage_efficiency
 
def compute_best_cost_efficiency(cost_efficiency):
    best_cost_efficiency = 1000000000
    n = len(cost_efficiency)
    for i in cost_efficiency:
        if i < best_cost_efficiency:
            best_cost_efficiency = i
    for i in range(n):
        if best_cost_efficiency == cost_efficiency[i]:
            position = i
    return position, best_cost_efficiency
 
def compute_and_display_results(name,storage_efficiency, cost_efficiency, position_1, position_2):
    print(f"Best COST Efficiency:\nname: {name[position_2]}| Storage Efficiency: {storage_efficiency[position_2]:.2f} | Cost Efficiency: ${cost_efficiency[position_2]:.2f}")
    print("\n")
    print(f"Best STORAGE Efficiency:\nname: {name[position_1]}| Storage Efficiency: {storage_efficiency[position_1]:.2f} | Cost Efficiency: ${cost_efficiency[position_1]:.2f}")
    print("\n")
   
name = ["#1 Picnic","#1 Tall","#2","#2.5","#3 Cylinder","#5","#6Z","#8Z short","#10","#211","#300","#303"]    
radius = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
height = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]
cost_per_can = [0.28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42]
 
import math
# teste = compute_volume(radius, height)
# print(teste)
# exit()
 
 
main(name, radius, height, cost_per_can)