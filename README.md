# ⚙️ Round Robin Scheduler (GUI)

## 📌 Overview

This project is a **Graphical User Interface (GUI) application** that simulates the **Round Robin CPU Scheduling algorithm** using PyQt6.

It allows users to input process burst times and a time quantum, then visualizes the execution order in a clean table format.

---

## 🎯 Objective

The goal of this project is to demonstrate how CPU scheduling works in operating systems, specifically using the **Round Robin algorithm**, through an interactive and user-friendly interface.

---

## 🛠️ Technologies Used

* Python
* PyQt6

---

## 🧠 Algorithm Used

**Round Robin Scheduling**:

* Each process gets a fixed time slice (Time Quantum)
* Processes are executed in a cyclic order
* If a process is not finished, it goes back to the queue

---

## 🚀 Features

* Simple and clean GUI
* User input for:

  * Process burst times
  * Time quantum
* Displays execution order in a table
* Styled interface (colors, fonts, layout)
* Interactive button to run the algorithm

---

## 🖥️ How It Works

1. Enter burst times (comma separated)

   ```
   Example: 8, 4, 6
   ```
2. Enter time quantum

   ```
   Example: 3
   ```
3. Click **Run Round Robin**
4. The table will display:

   * Process ID (P1, P2, …)
   * Time slot order

---

## 📁 Project Structure

```id="c93f21"
Round-Robin-Algorithm-/
│
├── main.py        # algorithm implementation
└── README.md      # Project documentation
└── untitled.ui
```

---

## 💡 Example Input

* Burst Times: `8, 4, 6`
* Time Quantum: `3`

### Output (Example)

| Process | Time Slot   |
| ------- | ----------- |
| P2      | Time Slot 1 |
| P3      | Time Slot 2 |
| P1      | Time Slot 3 |

---

## ⭐ Notes

* This project is for educational purposes
* Helps visualize CPU scheduling concepts
* Can be extended to include:

  * Waiting time calculation
  * Turnaround time
  * Gantt chart visualization
