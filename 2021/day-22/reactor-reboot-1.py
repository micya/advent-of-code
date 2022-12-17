def main():
    cube_status = {}

    with open("input.txt") as file:
        for line in file:
            parts = line.split(" ")

            status = True if parts[0] == "on" else False
            parts = parts[1].split(",")

            parts_x = parts[0].split("=")[1].split("..")
            x_min = max(int(parts_x[0]), -50)
            x_max = min(int(parts_x[1]), 50)

            parts_y = parts[1].split("=")[1].split("..")
            y_min = max(int(parts_y[0]), -50)
            y_max = min(int(parts_y[1]), 50)

            parts_z = parts[2].split("=")[1].split("..")
            z_min = max(int(parts_z[0]), -50)
            z_max = min(int(parts_z[1]), 50)

            for x in range(x_min, x_max + 1):
                for y in range(y_min, y_max + 1):
                    for z in range(z_min, z_max + 1):
                        cube_status[(x, y, z)] = status

    count = 0
    for cube in cube_status:
        if cube_status[cube]:
            count += 1

    print(f"count: {count}")

if __name__ == "__main__":
    main()