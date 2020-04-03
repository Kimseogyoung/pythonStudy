#!/usr/bin/env python
# coding: utf-8
#메인　창


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QGridLayout,QGroupBox,QComboBox,QLineEdit,QSlider
from PyQt5.QtGui import QPixmap, QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
import cv2

from ADproject_sticker.photoView import *

from ADproject_sticker.Stickernames import *



class UserModel(QStandardItemModel):#combobox에　이미지를　넣기　위해서　만든　클래스

    def __init__(self, data=None, parent=None):#data 는　튜플로이루어진　리스트
        QStandardItemModel.__init__(self, parent)
        for i, d in data:#i - 스티커이름　d -  스티커이미지경로
            item = QStandardItem(i)
            item.setData(d, Qt.DecorationRole)
            self.setItem(data.index((i,d)), 0, item)

    def data(self, QModelIndex, role=None):
        data = self.itemData(QModelIndex)
        if role == Qt.DisplayRole:
            return "%s" % (data[role])
        elif role in data and role == Qt.DecorationRole:
            return QPixmap(data[role]).scaledToHeight(25)
        elif role == Qt.UserRole:
            print(data[role])
        return QVariant()


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.view = CView(self)
        self.a=QPoint()
        print(self.mapToGlobal(QPoint(0,0)))
        #### Sticker manager Group Area
        ManageGroup=QGroupBox("Manage Sticker")


        self.stickerLabel=QLabel("스티커 번호/종류")
        self.stickernumberManageBox=QComboBox()
        self.kindofstickerManageBox=QComboBox()

        self.stickernumberManageBox.setStyleSheet("color:white;background:gray")

        self.stickernumberManageBox.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        #self.kindofstickerManageBox.addItems(stickerName)
        model = UserModel(list(zip(stickerName,stickerPath)))
        self.kindofstickerManageBox.setModel(model)


        self.makeButton=QPushButton("만들기")
        self.removeButton=QPushButton("지우기")

        Managelayout=QGridLayout()
        Managelayout.addWidget(self.stickerLabel,0,0)
        Managelayout.addWidget(self.stickernumberManageBox,0,1)
        Managelayout.addWidget(self.kindofstickerManageBox, 0, 2)
        Managelayout.addWidget(self.makeButton,0,3)
        Managelayout.addWidget(self.removeButton,0,4)



        ManageGroup.setLayout(Managelayout)
        #### Sticker manager Group Area




        #### Edit Group Area
        EditGroup=QGroupBox("Edit")
        self.currentEditLabel=QLabel("현재 편집중인 스티커 : "+str(currentSticker))


        opacityLabel=QLabel("투명도: ")
        sizeLabel=QLabel("  크기: ")

        self.opacity=QSlider(Qt.Horizontal,self)#투명도　슬라이더
        self.size=QSlider(Qt.Horizontal,self)#크기　슬라이더

        #각각　슬라이더의　최대　최소값
        self.opacity.setMaximum(100)
        self.opacity.setMinimum(0)
        self.size.setMaximum(479)
        self.size.setMinimum(20)


        Editlayout=QGridLayout()
        Editlayout.addWidget(self.currentEditLabel,0,0)
        Editlayout.addWidget(opacityLabel,1,1)
        Editlayout.addWidget(sizeLabel,2,1)
        Editlayout.addWidget(self.opacity,1,2)
        Editlayout.addWidget(self.size, 2, 2)


        EditGroup.setLayout(Editlayout)
        ##Edit Group Area



        ##Save Group Area
        SaveGroup = QGroupBox("Save")
        self.filename_ = QLabel("파일 명")
        self.savenameEdit = QLineEdit()
        self.saveButton=QPushButton("저장")


        Savelayout=QGridLayout()
        Savelayout.addWidget(self.filename_, 0, 0)
        Savelayout.addWidget(self.savenameEdit,0,1)
        Savelayout.addWidget(self.saveButton,0,2)

        SaveGroup.setLayout(Savelayout)
        ##Save Group Area

        ##Upload Group Area

        UploadGroup = QGroupBox("Upload")
        self.filename = QLabel("파일 명")
        self.filenameEdit = QLineEdit()
        self.uploadtitle = QLabel("글 제목")
        self.uploadtitleEdit = QLineEdit()
        self.uploadcontent = QLabel("글 내용")
        self.uploadcontentEdit = QLineEdit()
        self.uploadusername = QLabel("사용자 이름")
        self.uploadusernameEdit = QLineEdit()
        self.uploadButton = QPushButton("업로드")

        #내　블로그　해당　카테고리링크를　qlabel에　하이퍼링크로　걸기
        bloglink=QLabel("<a href=\"mybloglink\">"
                        "Click this link to go to my naverblog sticker category</a>")
        bloglink.setOpenExternalLinks(True)

        Uploadlayout = QGridLayout()
        Uploadlayout.addWidget(self.filename, 0, 0)
        Uploadlayout.addWidget(self.filenameEdit, 0, 1)
        Uploadlayout.addWidget(self.uploadtitle, 1, 0)
        Uploadlayout.addWidget(self.uploadtitleEdit, 1, 1)
        Uploadlayout.addWidget(self.uploadcontent, 2, 0)
        Uploadlayout.addWidget(self.uploadcontentEdit, 2, 1)
        Uploadlayout.addWidget(self.uploadusername, 3, 0)
        Uploadlayout.addWidget(self.uploadusernameEdit, 3, 1)
        Uploadlayout.addWidget(self.uploadButton, 4, 1)
        Uploadlayout.addWidget(bloglink, 5, 1)

        UploadGroup.setLayout(Uploadlayout)
        ##Upload Group Area



        self.removeButton.clicked.connect(self.view.removebuttonClicked)
        self.makeButton.clicked.connect(self.view.makebuttonClicked)
        self.saveButton.clicked.connect(self.view.savebuttonClicked)
        self.uploadButton.clicked.connect(self.view.uploadbuttonClicked)

        self.opacity.valueChanged.connect(self.view.OpsliderValueChanged)
        self.size.valueChanged.connect(self.view.sizesliderValueChanged)



        mainLayout=QGridLayout()

        mainLayout.addWidget(self.view,0,0,4,3)
        mainLayout.addWidget(ManageGroup,0,3)
        mainLayout.addWidget(EditGroup,1,3)
        mainLayout.addWidget(SaveGroup,2,3)
        mainLayout.addWidget(UploadGroup, 3, 3)
        self.setLayout(mainLayout)


        self.setWindowTitle('QPixmap')
        self.show()
        self.setFixedSize(self.width(), self.height())


    def moveEvent(self, e:QMoveEvent):#창이　움직일때마다　창의　모니터화면　좌표 받아오기
        self.a=e.pos()
        print("move",self.a)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
