from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class TotalCommander(QMainWindow):
    def __init__(self):
        super(TotalCommander, self).__init__()

        self.setupMenus()
        self.setupToolBar()
        self.interfejs()

    def interfejs(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Ready")

        mainLayout = QHBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0,0,0,0)

        self.grid = QGridLayout()
        self.grid.setSpacing(0)

        self.vbox = QVBoxLayout ()
        self.vbox.setSpacing(5)

        self.text = QTextEdit()

        self.gridcolor = QGridLayout()
        self.gridcolor.setSpacing(1)

        self.combo = QComboBox()
        self.combo.addItem('10', 10)
        self.combo.addItem('11', 11)
        self.combo.addItem('12', 12)
        self.combo.addItem('13', 13)
        self.combo.addItem('14', 14)        

        self.vbox.addWidget(self.combo)
        
        self.radio_button_one = QRadioButton('Times New Roman')
        self.radio_button_two = QRadioButton('Arial')
        self.radio_button_three = QRadioButton('Courier New')
        self.radio_button_one.setChecked(True)

        self.vbox.addWidget(self.radio_button_one)
        self.vbox.addWidget(self.radio_button_two)
        self.vbox.addWidget(self.radio_button_three)
        
        self.radio_button_group = QButtonGroup()
        self.radio_button_group.addButton(self.radio_button_one)
        self.radio_button_group.addButton(self.radio_button_two)
        self.radio_button_group.addButton(self.radio_button_three)        

        self.but1 = QPushButton()
        self.but1.setStyleSheet("background-color: silver")
        self.but2 = QPushButton()
        self.but2.setStyleSheet("background-color: red")
        self.but3 = QPushButton()
        self.but3.setStyleSheet("background-color: yellow")
        self.but4 = QPushButton()
        self.but4.setStyleSheet("background-color: green")
        self.but5 = QPushButton()
        self.but5.setStyleSheet("background-color: brown")
        self.but6 = QPushButton()
        self.but6.setStyleSheet("background-color: grey")
        self.but7 = QPushButton()
        self.but7.setStyleSheet("background-color: orange")
        self.but8 = QPushButton()
        self.but8.setStyleSheet("background-color: pink")
        self.but9 = QPushButton()
        self.but9.setStyleSheet("background-color: blue")

        self.gridcolor.addWidget(self.but1,0,0,1,1)
        self.gridcolor.addWidget(self.but2,0,1,1,1)
        self.gridcolor.addWidget(self.but3,0,2,1,1)
        self.gridcolor.addWidget(self.but4,1,0,1,1)
        self.gridcolor.addWidget(self.but5,1,1,1,1)
        self.gridcolor.addWidget(self.but6,1,2,1,1)
        self.gridcolor.addWidget(self.but7,2,0,1,1)
        self.gridcolor.addWidget(self.but8,2,1,1,1)
        self.gridcolor.addWidget(self.but9,2,2,1,1)
        
        self.text.setText('Pole tekstowe')
        self.grid.addWidget(self.text,0,0,1,1)
        self.vbox.addLayout(self.gridcolor)

        self.radio_button_one.toggled.connect(self.czcionka)
        self.radio_button_two.toggled.connect(self.czcionka)
        self.radio_button_three.toggled.connect(self.czcionka)
        self.combo.activated.connect(self.czcionka)
        self.but1.clicked.connect(lambda:self.tlo('silver'))
        self.but2.clicked.connect(lambda:self.tlo('red'))
        self.but3.clicked.connect(lambda:self.tlo('yellow'))
        self.but4.clicked.connect(lambda:self.tlo('green'))
        self.but5.clicked.connect(lambda:self.tlo('brown'))
        self.but6.clicked.connect(lambda:self.tlo('grey'))
        self.but7.clicked.connect(lambda:self.tlo('orange'))
        self.but8.clicked.connect(lambda:self.tlo('pink'))
        self.but9.clicked.connect(lambda:self.tlo('blue'))

        widget1 = QWidget()
        widget1.setLayout(self.vbox)
        widget1.setFixedWidth(150)
        
        mainLayout.addWidget(widget1, 0, Qt.AlignTop)
        mainLayout.addLayout(self.grid)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        self.setStyleSheet("""QStatusBar {
         border: 1px solid black;
        }""")

        self.setGeometry(70, 70, 530, 400)
        self.setWindowIcon(QIcon('notatnik.png'))
        self.setWindowTitle("QNotatnik")


    def tlo(self, kolor):
        self.text.setStyleSheet("background-color: %s" % kolor)
        self.statusbar.showMessage('Wybrano kolor tla')

    def czcionka(self, index):
        font = QFont()
        font.setPointSize(self.combo.itemData(index))

        if self.radio_button_one.isChecked() == True:            
            font.setFamily("Times New Roman")
        if self.radio_button_two.isChecked() == True:            
            font.setFamily("Arial")
        if self.radio_button_three.isChecked() == True:
            font.setFamily("Courier New")

        self.text.setFont(font)
        self.statusbar.showMessage('Ustawiono czcionke')

    def openfile(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)

      if dlg.exec_():
        filename = dlg.selectedFiles()
        data = open(filename[0], 'rt').read()
        self.text.setText(data)
        self.statusbar.showMessage('Otworzono plik')

    def savefile(self):
      name = QFileDialog.getSaveFileName(self, 'Save File', "Text files (*.txt)")
      if name[0] != '':
        file = open(name[0],'w')
        text = self.text.toPlainText()
        file.write(text)
        file.close()
        self.statusbar.showMessage('Zapisano')
      else:
        self.statusbar.showMessage('Anulowano zapis do pliku')

    def setupMenus(self):

        plikMenu = self.menuBar().addMenu("Plik")
        plikMenu.addSeparator()

        edycjaMenu = self.menuBar().addMenu("Edycja")
        edycjaMenu.addSeparator()
        
        nowyAction = QAction("Nowy", self)
        otworzAction = QAction("Otworz", self)
        zapiszAction = QAction("Zapisz", self)
        zapiszjakoAction = QAction("Zapisz jako...", self)
        koniecAction = QAction("Koniec", self)

        otworzAction.triggered.connect(self.openfile)
        zapiszAction.triggered.connect(self.savefile)

        plikMenu.addAction(nowyAction)
        plikMenu.addAction(otworzAction)
        plikMenu.addAction(zapiszAction)
        plikMenu.addAction(zapiszjakoAction)
        plikMenu.addAction(koniecAction)        

        wytnijAction = QAction("Wytnij", self)
        wytnijAction.setShortcut("Ctrl+X")
        kopiujAction = QAction("Kopiuj", self)
        kopiujAction.setShortcut("Ctrl+C")
        wklejAction = QAction("Wklej", self)
        wklejAction.setShortcut("Ctrl+V")
        zaznaczAction = QAction("Zaznacz wszystko", self)
        zaznaczAction.setShortcut("Ctrl+A")
                
        edycjaMenu.addAction(wytnijAction)
        edycjaMenu.addAction(kopiujAction)
        edycjaMenu.addAction(wklejAction)
        edycjaMenu.addAction(zaznaczAction)

    def setupToolBar(self):
    	tb = self.addToolBar("toolbar")

    	nowy = QAction(QIcon("nowy.png"),"nowy",self)
    	otworz = QAction(QIcon("otworz.png"),"otworz",self)
    	szukaj = QAction(QIcon("szukaj.png"),"szukaj",self)
    	zapisz = QAction(QIcon("zapisz.png"),"zapisz",self)
    	cofnij = QAction(QIcon("undo.png"),"cofnij",self)
    	dalej = QAction(QIcon("redo.png"),"dalej",self)
    	wytnij = QAction(QIcon("scissors.png"),"wytnij",self)
    	kopiuj = QAction(QIcon("copy.png"),"kopiuj",self)
    	wklej = QAction(QIcon("paste.png"),"wklej",self)

    	otworz.triggered.connect(self.openfile)
    	zapisz.triggered.connect(self.savefile)

    	dalej.setEnabled(False)

    	tb.addAction(nowy)
    	tb.addAction(otworz)    	
    	tb.addAction(szukaj)    	
    	tb.addAction(zapisz)
    	tb.addSeparator()    	
    	tb.addAction(cofnij)   	
    	tb.addAction(dalej)
    	tb.addSeparator()    	
    	tb.addAction(wytnij)    	
    	tb.addAction(kopiuj)    	
    	tb.addAction(wklej)
    	tb.addSeparator()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = TotalCommander()
    okno.show()
    sys.exit(app.exec_())
