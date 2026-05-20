import tkinter as tk

CELL_SIZE = 60

def draw_grid(grid_map, path, start, goal):
    rows = len(grid_map)
    cols = len(grid_map[0])

    root = tk.Tk()
    root.title("Q-Learning Grid")

    canvas = tk.Canvas(root, width=cols*CELL_SIZE, height=rows*CELL_SIZE)
    canvas.pack()

    colors = {
        0: "white",   # road
        1: "green",   # jungle
        2: "blue",    # swamp
        3: "gray",    # mountain
        4: "yellow",  # desert
        5: "gold",    # goal
    }

    for r in range(rows):
        for c in range(cols):
            x1 = c * CELL_SIZE
            y1 = r * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            cell_value = int(grid_map[r][c])  # ✅ fix

            canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=colors.get(cell_value, "black"),  # ✅ safe fallback
                outline="black"
            )

    # draw path
    for (r, c) in path:
        x = c * CELL_SIZE + CELL_SIZE//2
        y = r * CELL_SIZE + CELL_SIZE//2
        canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")

    # start
    canvas.create_text(
        start[1]*CELL_SIZE+30,
        start[0]*CELL_SIZE+30,
        text="S",
        font=("Arial", 16, "bold")
    )

    # goal
    canvas.create_text(
        goal[1]*CELL_SIZE+30,
        goal[0]*CELL_SIZE+30,
        text="G",
        font=("Arial", 16, "bold")
    )

    root.mainloop()