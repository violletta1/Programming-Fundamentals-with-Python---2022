fires_cells = input().split("#")
water = int(input())
effort = 0
total_fire = []
for i in range(len(fires_cells)):
    level, cell = fires_cells[i].split(" = ")
    cell = int(cell)
    if level == "Low" and not 1 <= cell <= 50:#if level == "Low" and cell > 50:
        continue
    if level == "Medium" and not 51 <= cell <= 80:
        continue
    if level == "High" and not 81 <= cell <= 125:
        continue
    if water < cell:
        continue
    water -= cell
    total_fire.append(cell)

    effort += cell * 0.25
print("Cells:")
for el in total_fire:
    print(type(el))
    print(f" - {str(el)}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {str(sum(total_fire))}")
