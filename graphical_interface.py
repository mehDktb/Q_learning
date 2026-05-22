import tkinter as tk

CELL_SIZE = 60

class GridViewer:
    def __init__(self, grid_map, path, start, goal):
        self.grid_map = grid_map
        self.path = path
        self.start = start
        self.goal = goal

        self.zoom = 1.0

        self.rows = len(grid_map)
        self.cols = len(grid_map[0])

        self.root = tk.Tk()
        self.root.title("RL Grid Viewer")

        # scrollable canvas
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<MouseWheel>", self.zoom_canvas)

        self.draw()

        self.root.mainloop()

    def zoom_canvas(self, event):
        if event.delta > 0:
            self.zoom *= 1.1
        else:
            self.zoom *= 0.9

        self.canvas.delete("all")
        self.draw()

    def draw(self):
        colors = {
            0: "white",
            1: "green",
            2: "blue",
            3: "gray",
            4: "yellow",
            5: "black",
            6: "gold",
        }

        size = int(CELL_SIZE * self.zoom)

        for r in range(self.rows):
            for c in range(self.cols):

                x1 = c * size
                y1 = r * size
                x2 = x1 + size
                y2 = y1 + size

                val = int(self.grid_map[r][c])

                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=colors.get(val, "pink"),
                    outline="black"
                )

        # path
        for (r, c) in self.path:
            x = c * size + size // 2
            y = r * size + size // 2
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="red")

        # start
        self.canvas.create_text(
            self.start[1]*size + size//2,
            self.start[0]*size + size//2,
            text="S"
        )

        # goal
        self.canvas.create_text(
            self.goal[1]*size + size//2,
            self.goal[0]*size + size//2,
            text="G"
        )