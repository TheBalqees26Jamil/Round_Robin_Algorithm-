import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette, QIcon

class RoundRobinScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Round Robin Scheduler")
        self.setGeometry(100, 100, 600, 500)


        self.setWindowIcon(QIcon("C:\\Users\\DELL\\Desktop\\Icons\\brain.png"))


        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(215, 189, 226 ))
        self.setPalette(palette)

        self.layout = QVBoxLayout()


        self.instructions = QLabel("Enter Process Burst Times (comma separated):")
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.instructions.setStyleSheet("font-size: 16px; font-weight: bold; color: #333; margin-bottom: 10px;")
        self.layout.addWidget(self.instructions)


        self.process_input = QLineEdit()
        self.process_input.setPlaceholderText("e.g. 8, 4, 6")
        self.process_input.setStyleSheet("font-size: 14px; padding: 8px; border-radius: 5px; border: 1px solid #ccc;")
        self.layout.addWidget(self.process_input)


        self.time_quantum_label = QLabel("Enter Time Quantum:")
        self.time_quantum_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_quantum_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #333; margin-top: 20px;")
        self.layout.addWidget(self.time_quantum_label)


        self.time_quantum_input = QLineEdit()
        self.time_quantum_input.setPlaceholderText("e.g. 3")
        self.time_quantum_input.setStyleSheet("font-size: 14px; padding: 8px; border-radius: 5px; border: 1px solid #ccc;")
        self.layout.addWidget(self.time_quantum_input)


        self.run_button = QPushButton("Run Round Robin")
        self.run_button.setStyleSheet("font-size: 16px;font-weight: bold; background-color: #8f094c ; color: white; padding: 10px; border-radius: 5px;")  # 991a65
        self.run_button.clicked.connect(self.run_round_robin)
        self.layout.addWidget(self.run_button)


        self.result_table = QTableWidget(self)
        self.result_table.setRowCount(0)
        self.result_table.setColumnCount(2)
        self.result_table.setHorizontalHeaderLabels(["Process", "Time Slot"])
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.result_table.setStyleSheet("font-size: 14px; border: 1px solid #ccc;")
        self.layout.addWidget(self.result_table)


        self.setLayout(self.layout)

    def run_round_robin(self):
        # Get inputs
        burst_times = list(map(int, self.process_input.text().split(',')))
        time_quantum = int(self.time_quantum_input.text())

        processes = len(burst_times) 

        remaining_times = burst_times.copy() 
        queue = list(range(processes)) 

        execution_order = []  
        executed_processes = set()  

        while queue:
            process_index = queue.pop(0)
            burst_time = remaining_times[process_index] 

            if process_index not in executed_processes:
                executed_processes.add(process_index) 
                execution_order.append(f"P{process_index+1}")  

            if burst_time > time_quantum:

                remaining_times[process_index] -= time_quantum

                queue.append(process_index)  
            else:


                remaining_times[process_index] = 0  

        
        sorted_execution_order = sorted(execution_order, key=lambda x: burst_times[int(x[1])-1]) 
        
        self.result_table.setRowCount(0)

        
        for i, process in enumerate(sorted_execution_order):
            self.result_table.insertRow(i)
            self.result_table.setItem(i, 0, QTableWidgetItem(process))
            self.result_table.setItem(i, 1, QTableWidgetItem(f"Time Slot {i+1}"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RoundRobinScheduler()
    window.show()
    sys.exit(app.exec())

