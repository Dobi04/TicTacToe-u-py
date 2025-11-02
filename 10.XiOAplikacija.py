import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
import random, time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(700,300,500,500)
        Label = QLabel("", self)
        Label.setGeometry(0,0,500,500)
        pixmap = QPixmap("Logo.png")
        Label.setPixmap(pixmap)

        self.setWindowTitle("TicTacGlow")
        self.setWindowIcon(QIcon("C:\\Users\\Ivan\\Pictures\\logo.png.png"))
        self.nameing_Buttons()
        self.layout_Button()
        self.player_turn = True
        self.players_turn()
        self.win_lost()

    def players_turn(self):
        self.clicking_Buttons()

    def nameing_Buttons(self):
        self.button1 = QPushButton("#1",self)
        self.button2 = QPushButton("#2",self)
        self.button3 = QPushButton("#3",self)
        self.button4 = QPushButton("#4",self)
        self.button5 = QPushButton("#5",self)
        self.button6 = QPushButton("#6",self)
        self.button7 = QPushButton("#7",self)
        self.button8 = QPushButton("#8",self)
        self.button9 = QPushButton("#9",self)

    def clicking_Buttons(self):
        self.button1.clicked.connect(self.clicked_Button)
        self.button2.clicked.connect(self.clicked_Button)
        self.button3.clicked.connect(self.clicked_Button)
        self.button4.clicked.connect(self.clicked_Button)
        self.button5.clicked.connect(self.clicked_Button)
        self.button6.clicked.connect(self.clicked_Button)
        self.button7.clicked.connect(self.clicked_Button)
        self.button8.clicked.connect(self.clicked_Button)
        self.button9.clicked.connect(self.clicked_Button)

    def layout_Button(self):
        self.button1.setGeometry(110,110,70,70)        
        self.button1.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button2.setGeometry(225,110,70,70)
        self.button2.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button3.setGeometry(335,110,70,70)
        self.button3.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button4.setGeometry(110,220,70,70)
        self.button4.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button5.setGeometry(225,220,70,70)
        self.button5.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button6.setGeometry(335,220,70,70)
        self.button6.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button7.setGeometry(110,325,70,70)
        self.button7.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button8.setGeometry(225,325,70,70)
        self.button8.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
        self.button9.setGeometry(335,325,70,70)
        self.button9.setStyleSheet("color: white;"
                                   "background-color: black;"
                                   "font-size: 50px;")
    
    def clicked_Button(self):
        clicked_button = self.sender()
        if self.player_turn:
            clicked_button.setText("X")
            clicked_button.setDisabled(True)
            clicked_button.setStyleSheet("color: #00ff22;"
                                         "background-color: #07380d;"
                                         "font-size: 100px;"
                                         "border: 2px solid #00ff22")
            
            self.player_turn = False
            self.win_lost()
            self.computer_try()

    def computer_try(self):
        computer_move = random.randint(1,9)
        self.computer_move(computer_move)

    def computer_move(self, computer_move):
        match computer_move:
            case 1:
                if self.button1.isEnabled():
                    self.button1.setText("O")
                    self.button1.setDisabled(True)
                    self.button1.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a;")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()

            case 2:
                if self.button2.isEnabled():
                    self.button2.setText("O")
                    self.button2.setDisabled(True)
                    self.button2.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()
                
            case 3:
                if self.button3.isEnabled():
                    self.button3.setText("O")
                    self.button3.setDisabled(True)
                    self.button3.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a;")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()
            
            case 4:
                if self.button4.isEnabled():
                    self.button4.setText("O")
                    self.button4.setDisabled(True)
                    self.button4.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a;")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()

            case 5:
                if self.button5.isEnabled():
                    self.button5.setText("O")
                    self.button5.setDisabled(True)
                    self.button5.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a;")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()
            
            case 6:
                if self.button6.isEnabled():
                    self.button6.setText("O")
                    self.button6.setDisabled(True)
                    self.button6.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a;")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()
            
            case 7:
                if self.button7.isEnabled():
                    self.button7.setText("O")
                    self.button7.setDisabled(True)
                    self.button7.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a;")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()
            
            case 8:
                if self.button8.isEnabled():
                    self.button8.setText("O")
                    self.button8.setDisabled(True)
                    self.button8.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()

            case 9:
                if self.button9.isEnabled():
                    self.button9.setText("O")
                    self.button9.setDisabled(True)
                    self.button9.setStyleSheet("color: #ff051a;"
                                               "background-color: #540c12;"
                                               "font-size: 100px;"
                                               "border: 2px solid #ff051a")
                    self.player_turn = True
                    self.win_lost()
                else:
                    self.computer_try()
    
    def win_lost(self):
        if ((self.button1.text() == "X" and self.button2.text() == "X" and self.button3.text() == "X") or
           (self.button4.text() == "X" and self.button5.text() == "X" and self.button6.text() == "X") or
           (self.button7.text() == "X" and self.button8.text() == "X" and self.button9.text() == "X") or
           (self.button1.text() == "X" and self.button4.text() == "X" and self.button7.text() == "X") or
           (self.button2.text() == "X" and self.button5.text() == "X" and self.button8.text() == "X") or
           (self.button3.text() == "X" and self.button6.text() == "X" and self.button9.text() == "X") or
           (self.button1.text() == "X" and self.button5.text() == "X" and self.button9.text() == "X") or
           (self.button3.text() == "X" and self.button5.text() == "X" and self.button7.text() == "X")):
            print("Player Won")
        elif ((self.button1.text() == "O" and self.button2.text() == "O" and self.button3.text() == "O") or
             (self.button4.text() == "O" and self.button5.text() == "O" and self.button6.text() == "O") or
             (self.button7.text() == "O" and self.button8.text() == "O" and self.button9.text() == "O") or
             (self.button1.text() == "O" and self.button4.text() == "O" and self.button7.text() == "O") or
             (self.button2.text() == "O" and self.button5.text() == "O" and self.button8.text() == "O") or
             (self.button3.text() == "O" and self.button6.text() == "O" and self.button9.text() == "O") or
             (self.button1.text() == "O" and self.button5.text() == "O" and self.button9.text() == "O") or
             (self.button3.text() == "O" and self.button5.text() == "O" and self.button7.text() == "O")):
            print("Player lost")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
