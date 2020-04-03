#!/usr/bin/env python
# coding: utf-8
# 이벤트　처리，스티커편집　캔버스　코드


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ADproject_sticker.mainWindow import *
from ADproject_sticker.Stickernames import *
from ADproject_sticker.errorclass import *
from ADproject_sticker.serverUpload import NaverBlog,serverupload
from ADproject_sticker.camCapture import capturecam





class Pixmap(QPixmap):
        #a = QPixmap(path)
         #   a = a.scaled(w,h, Qt.KeepAspectRatio, Qt.FastTransformation)  줄여쓰기

    def __init__(self,path,w,h):
        super().__init__(QPixmap(path).scaled(w, h, Qt.KeepAspectRatio, Qt.FastTransformation))




class Label(QLabel):
    def __init__(self,parent,number):
        super().__init__(parent=parent)
        self.number=number
        self.parent=parent#parent은　Cview
        self.mainwindow=self.parent.parent #parent의　parent이니까　mainwindow창（cview의　부모）

        # 초기투명도　１로　설정
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setOpacity(1)


    def setOpacity(self,opacity):# 투명도　설정　메서드
        self.opacity_effect.setOpacity(opacity)
        self.setGraphicsEffect(self.opacity_effect)

    def setstartpos(self):#make이후　시작위치　설정
        self.setGeometry(1, 1, self.size, self.size)

    def setPixmapandSize(self,pixmap):#pixmap설정
        self.setPixmap(pixmap)
        self.size=pixmap.width()
        self.setGeometry(self.x(),self.y(),self.size,self.size)

    def mousePressEvent(self, event):
        """
        mouse가 위젯 위에서 클릭됐을때만 반응
        """
        global currentSticker
        if not self.underMouse():
            return
        self.raise_()#맨위로　설정
        currentSticker = self.number #현재　편집중인　스티커　번호　변경
        self.mainwindow.currentEditLabel.setText("현재 편집 중인 스티커 : " + str(currentSticker))

        #클릭시　선택한　스티커의　원래　투명도，크기정보를　슬라이더에　옮김
        self.mainwindow.opacity.setValue(self.opacity_effect.opacity()*100)
        self.mainwindow.ypos.setValue(self.y())
        self.mainwindow.size.setValue(self.size)

        print('stickerclick',currentSticker)

    def mouseMoveEvent(self, e):
        self.setGeometry( e.globalX()-self.mainwindow.a.x()-self.size//2 ,
                          e.globalY()- self.mainwindow.a.y()-self.size//2 , self.size, self.size)
        #e.globalX()-self.mainwindow.a.x()-self.size//2 -> 마우스의　화면상　위치　－　메인창의화면상위치　－스티커　너비／／２　







class CView(QGraphicsView):

    def __init__(self,parent):

        super().__init__(parent)
        self.parent=parent
        #self.setMouseTracking(True)#마우스　클릭안해도　이동감지

        capturecam()#사진캡처

        pixmap = QPixmap('a.jpg')

        self.scene = QGraphicsScene()

        self.scene.addPixmap(pixmap)
        self.setScene(self.scene)

        self.scene.setSceneRect(0,0,640,480)

        self.items = []


        self.al = [x for x in range(11)]
        for x in range(11): self.al[x]=Label(self,x)

        self.ap = [x for x in range(11)]


    def removebuttonClicked(self):
        """removebutton 클릭했을 때"""
        stknumber=int(self.parent.stickernumberManageBox.currentText())

        self.al[stknumber].clear()#초기화
        self.ap[stknumber]=0#초기화
        currentStickers[stknumber]='None'

        print('remove button click')

    def makebuttonClicked(self):
        """makebutton 클릭했을 때"""
        global currentSticker
        stknumber=int(self.parent.stickernumberManageBox.currentText())

        self.ap[stknumber] = Pixmap(stickerPath[stickerName.index(self.parent.kindofstickerManageBox.currentText())],30,30)
        #이미지 설정/기본 크기 설정

        self.al[stknumber].setPixmapandSize(self.ap[stknumber])
        self.al[stknumber].setstartpos()
        #1,1위치에 배치


        currentStickers[stknumber]=self.parent.kindofstickerManageBox.currentText()
        # currentStikers에 사용중인 스티커번호:스티커이름 업데이트

        currentSticker=stknumber
        self.parent.currentEditLabel.setText("현재 편집 중인 스티커 : " + str(currentSticker))
        print('make button click' , currentStickers,currentSticker)


    def OpsliderValueChanged(self):
        """투명도슬라이더가 움직였을때"""
        try:
            global currentSticker
            if (currentStickers[currentSticker] == "None"):
                raise Nonselectsticker()
            self.al[currentSticker].setOpacity(self.parent.opacity.value()/100)#투명도　값은　０～１이라　나눠줌

        except Nonselectsticker:
            print("스티커가 선택되지 않음")

        print("apply new stickerinfo")


    def sizesliderValueChanged(self):
        """size슬라이더가 움직였을때 """
        try:
            global currentSticker
            if (currentStickers[currentSticker] == "None"):
                raise Nonselectsticker()
            self.ap[currentSticker] = Pixmap(stickerPath[stickerName.index(currentStickers[currentSticker])],
                                    int(self.parent.size.value()),int(self.parent.size.value()))
                    # currentStickers에서 스티커 종류불러오기로 pixmap저장
                    # 매번 불러오지 않으면 작아지면서 화질깨짐  #크기조정
            self.al[currentSticker].setPixmapandSize(self.ap[currentSticker])

        except Nonselectsticker:
            print("스티커가 선택되지 않음")

        print("apply new stickerinfo")




    def savebuttonClicked(self):
        """savebutton 클릭했을 때"""
        img = QPixmap(self.grab(self.sceneRect().toRect()))
        img.save('Editedphoto/'+self.parent.savenameEdit.text()+'.png', 'PNG')
        print('save button click')

    def uploadbuttonClicked(self):
        serverupload(""+self.parent.filenameEdit.text()+".png")
        # 블로그에　업로드하기
        naver = NaverBlog('colisel', '0b4700fd236d0c776358abae61b15a49')  # 내　블로그　아이디，　블로그　암호코드　
        naver.post(self.parent.uploadtitleEdit.text(), "<h2>"+self.parent.uploadcontentEdit.text()+"</h2>"
                            "<h4>"+self.parent.uploadusernameEdit.text()+"</h4>"
                            " <img src=http://colisej.cafe24.com/web/photo/"+self.parent.filenameEdit.text()+".png>", 'Sticker')
        print("uploadbutton click")

    def mousePressEvent(self, event):
        """cview를　클릭했을때　편집중인스티커　초기화　하도록　클릭이벤트　처리"""
        global currentSticker

        if not self.underMouse():
            return
        self.raise_()
        currentSticker=0
        self.parent.currentEditLabel.setText("현재 편집 중인 스티커 : "+str(currentSticker))

        print('viewclick',currentSticker)


