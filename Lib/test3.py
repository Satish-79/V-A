
'''
from test2 import *
from VABP import *

de = VAUIThread()
de.start()
abc = MainThread()
abc.start()
'''

import multithreading

class Demo(multithreading.MultiThread):
    def task(self, task):
        print(task)

task_list = range(1, 3 + 1)

demo = Demo(task_list, threads=3)

# Start
demo.start()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''