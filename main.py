#создай тут фоторедактор Easy Editor!
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QHBoxLayout, QFileDialog, QListWidget, QVBoxLayout
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageProcessor():
    def __init__(self):
        self.cur_Image = None
        self.cur_Name = None
        self.sub_folder = 'Modifided/'
    def loadImage(self, cur_Name):
        self.cur_Name = cur_Name
        image_path = os.path.join(workdir, cur_Name)
        self.cur_Image = Image.open(image_path)
    def showImage(self, path):
        imageLabel.hide()
        pixmap = QPixmap(path)
        w, h = imageLabel.width(), imageLabel.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        imageLabel.setPixmap(pixmap)
        imageLabel.show()
    def do_bw(self):
        self.cur_Image = self.cur_Image.convert('L')
        self.saveImage()
    def saveImage(self):
        path = os.path.join(workdir, self.sub_folder)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.cur_Name)
        self.cur_Image.save(image_path)
        self.showImage(image_path)
    def do_flip(self):
        self.cur_Image = self.cur_Image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
    def do_right(self):
        self.cur_Image = self.cur_Image.transpose(Image.ROTATE_270)
        self.saveImage()
    def do_left(self):
        self.cur_Image = self.cur_Image.transpose(Image.ROTATE_90)
        self.saveImage()
    def do_blur(self):
        self.cur_Image = self.cur_Image.filter(ImageFilter.BLUR)
        self.saveImage()
        


    #   teddy_gray = Teddy.convert('L')
    # teddy_gray.show()
    # teddy_gray.save('gray.jpg')
        
        
workdir = ''
app = QApplication([])
w = QWidget()
w.resize(350, 350)
w.setWindowTitle('Easy Editor')
btn_papka = QPushButton('Папка')
# print('Текущая директория: ', os.getcwd())

choose_list = QListWidget()
workImage = ImageProcessor()

imageLabel = QLabel('Картинка:')
btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')
btn_mirror = QPushButton('Зеркало')
btn_sharpness = QPushButton('Резкость')
btn_BW = QPushButton('Ч/Б')
layoutH_main = QHBoxLayout()
layoutH1_button = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()

layoutV1.addWidget(btn_papka)
layoutV1.addWidget(choose_list)
layoutV2.addWidget(imageLabel)
layoutH1_button.addWidget(btn_left)
layoutH1_button.addWidget(btn_right)
layoutH1_button.addWidget(btn_mirror)
layoutH1_button.addWidget(btn_sharpness)
layoutH1_button.addWidget(btn_BW)
layoutV2.addLayout(layoutH1_button)
layoutH_main.addLayout(layoutV1, 30)
layoutH_main.addLayout(layoutV2, 70)


def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = []
    for filename in files:
        for i in extensions:
            if filename.endswith(i):
                result.append(filename)
    return result

def showFilenamesList():
    choose_workdir()
    files = os.listdir(workdir)
    extensions = ['jpg', 'gif', 'png', 'jpeg']
    choose_list.clear()
    kartinki = filter(files, extensions)
    for kartinka in kartinki:
        choose_list.addItem(kartinka)

def showChosenImage():
    if choose_list.currentRow() >= 0:
        filename = choose_list.currentItem().text()
        workImage.loadImage(filename)
        image_path = os.path.join(workdir, workImage.cur_Name)
        workImage.showImage(image_path)













        
        
    
    





    
    
btn_sharpness.clicked.connect(workImage.do_blur)
btn_left.clicked.connect(workImage.do_left)
btn_right.clicked.connect(workImage.do_right)
btn_mirror.clicked.connect(workImage.do_flip)
btn_papka.clicked.connect(showFilenamesList)
btn_BW.clicked.connect(workImage.do_bw)
choose_list.currentRowChanged.connect(showChosenImage)
w.setLayout(layoutH_main)
w.show()
app.exec()
