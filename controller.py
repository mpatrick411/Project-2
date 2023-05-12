from PyQt5.QtWidgets import *
from view import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.__score_p1 = 0
        self.__score_p2 = 0
        self.__turn = 1
        self.__active = True

        self.spaceUL.clicked.connect(lambda: self.click(1))
        self.spaceU.clicked.connect(lambda: self.click(2))
        self.spaceUR.clicked.connect(lambda: self.click(3))
        self.spaceL.clicked.connect(lambda: self.click(4))
        self.spaceMiddle.clicked.connect(lambda: self.click(5))
        self.spaceR.clicked.connect(lambda: self.click(6))
        self.spaceDL.clicked.connect(lambda: self.click(7))
        self.spaceD.clicked.connect(lambda: self.click(8))
        self.spaceDR.clicked.connect(lambda: self.click(9))

        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_reset.clicked.connect(lambda: self.reset())

    def click(self, space):
        self.label_2.setText('')
        if self.__active:
            if space == 1:
                if self.spaceUL.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceUL.setText('X')
                    else:
                        self.spaceUL.setText('O')
                    self.__turn += 1
            elif space == 2:
                if self.spaceU.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceU.setText('X')
                    else:
                        self.spaceU.setText('O')
                    self.__turn += 1
            if space == 3:
                if self.spaceUR.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceUR.setText('X')
                    else:
                        self.spaceUR.setText('O')
                    self.__turn += 1
            if space == 4:
                if self.spaceL.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceL.setText('X')
                    else:
                        self.spaceL.setText('O')
                    self.__turn += 1
            if space == 5:
                if self.spaceMiddle.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceMiddle.setText('X')
                    else:
                        self.spaceMiddle.setText('O')
                    self.__turn += 1
            if space == 6:
                if self.spaceR.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceR.setText('X')
                    else:
                        self.spaceR.setText('O')
                    self.__turn += 1
            if space == 7:
                if self.spaceDL.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceDL.setText('X')
                    else:
                        self.spaceDL.setText('O')
                    self.__turn += 1
            if space == 8:
                if self.spaceD.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceD.setText('X')
                    else:
                        self.spaceD.setText('O')
                    self.__turn += 1
            if space == 9:
                if self.spaceDR.text() == '':
                    if self.__turn % 2 == 1:
                        self.spaceDR.setText('X')
                    else:
                        self.spaceDR.setText('O')
                    self.__turn += 1
            self.label_win.setText('')
            self.check_win()

    def check_win(self):
        self.__active = False
        if self.__turn % 2 == 0:
            self.label_win.setText('Player 1 wins!')
            if self.spaceUL.text() == 'X' and self.spaceU.text() == 'X' and self.spaceUR.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            elif self.spaceL.text() == 'X' and self.spaceMiddle.text() == 'X' and self.spaceR.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            elif self.spaceDL.text() == 'X' and self.spaceD.text() == 'X' and self.spaceDR.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            elif self.spaceUL.text() == 'X' and self.spaceL.text() == 'X' and self.spaceDL.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            elif self.spaceU.text() == 'X' and self.spaceMiddle.text() == 'X' and self.spaceD.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            elif self.spaceUR.text() == 'X' and self.spaceR.text() == 'X' and self.spaceDR.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            elif self.spaceUL.text() == 'X' and self.spaceMiddle.text() == 'X' and self.spaceDR.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            elif self.spaceUR.text() == 'X' and self.spaceMiddle.text() == 'X' and self.spaceDL.text() == 'X':
                self.__score_p1 += 1
                self.p1_score.setText(str(self.__score_p1))
            else:
                self.__active = True
                self.label_win.setText('')
        else:
            self.label_win.setText('Player 2 wins!')
            if self.spaceUL.text() == 'O' and self.spaceU.text() == 'O' and self.spaceUR.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            elif self.spaceL.text() == 'O' and self.spaceMiddle.text() == 'O' and self.spaceR.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            elif self.spaceDL.text() == 'O' and self.spaceD.text() == 'O' and self.spaceDR.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            elif self.spaceUL.text() == 'O' and self.spaceL.text() == 'O' and self.spaceDL.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            elif self.spaceU.text() == 'O' and self.spaceMiddle.text() == 'O' and self.spaceD.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            elif self.spaceUR.text() == 'O' and self.spaceR.text() == 'O' and self.spaceDR.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            elif self.spaceUL.text() == 'O' and self.spaceMiddle.text() == 'O' and self.spaceDR.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            elif self.spaceUR.text() == 'O' and self.spaceMiddle.text() == 'O' and self.spaceDL.text() == 'O':
                self.__score_p2 += 1
                self.p2_score.setText(str(self.__score_p2))
            else:
                self.__active = True
                self.label_win.setText('')



    def clear(self):
        self.__turn = 1
        self.spaceUL.setText('')
        self.spaceU.setText('')
        self.spaceUR.setText('')
        self.spaceL.setText('')
        self.spaceMiddle.setText('')
        self.spaceR.setText('')
        self.spaceDL.setText('')
        self.spaceD.setText('')
        self.spaceDR.setText('')
        self.label_2.setText('Click any square to begin playing')
        self.label_win.setText('')
        self.__active = True

    def reset(self):
        self.__score_p1 = 0
        self.__score_p2 = 0
        self.p1_score.setText('0')
        self.p2_score.setText('0')
        self.label_win.setText('')
