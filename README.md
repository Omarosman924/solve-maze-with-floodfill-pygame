# 🧩 Maze Drawer & Solver using Pygame

This project is an interactive **Maze Builder and Solver** built using **Python and Pygame**.  
Users can **manually draw paths**, and the program will compute a solution from the start to the end point using a custom **Flood Fill algorithm**.

---

## 🎮 Features

- Manually draw a path by pressing arrow keys.
- Save the drawn path to a file (`pos.txt`).
- Read path from file and reconstruct it visually.
- Solve the maze from end to start using a reverse flood-fill strategy.
- Display the shortest path from `start` to `end` in **yellow**.

---

## 🖱️ Controls

| Key        | Action         |
|------------|----------------|
| `Arrow Keys` | Move and draw path |
| `S`        | Stop drawing and save path |

---

## 🧠 Algorithms Used

- **Manual Drawing:** User controls the path via keyboard and it gets stored.
- **Flood Fill (Reverse):** From `end` to `start` using accessible neighbors to track all reachable cells.
- **Path Reconstruction:** From `start`, traces a shortest path backwards by intersecting valid previous steps.

---

## 🖼️ Visual Design

- **Grid Cells:** 20x20 pixels.
- **Start Point:** Red square.
- **End Point:** Blue square.
- **User Path:** White trail.
- **Solved Path:** Yellow trail with dots.
- **Cell Numbers (Optional):** Each cell can be labeled during solving with a step number.

---

## 📁 File Usage

- `pos.txt`  
  Contains the manually drawn path as a list of coordinates and directions.

---

## 🧰 Requirements

- Python 3.x
- Pygame

Install Pygame:

```bash
pip install pygame
```

---

## 🚀 How to Run

```bash
python maze_solver.py
```

Then:

1. Use arrow keys to draw a path from start to end.
2. Press `S` to stop and save the path.
3. The solver runs automatically and shows the solution in yellow.

---

## ⚠️ Notes

- The maze is static — the walls are always present, and only the user-created path is open.
- You must manually draw a valid path from start to end before solving.
- Some parts of the code (e.g., `right1`, `left1`) are used for special handling during path reconstruction.

---

## 📌 Author

- **Omar Osman**  
  A personal project to practice Pygame, basic pathfinding, and maze solving logic in Python.

---

## 🧠 Future Ideas

- Add auto maze generator using DFS or Kruskal's algorithm.
- Use BFS or A* for optimal pathfinding.
- Add GUI buttons for actions instead of just keyboard keys.
- Allow user to place walls and customize start/end positions.

