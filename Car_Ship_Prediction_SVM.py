# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 00:55:45 2021

@author: Achraf rahouti
"""

from sklearn import svm
clf=svm.SVC(C=1.2,kernel='linear')


import cv2 as cv
import numpy as np
from PyQt5 import QtWidgets,QtGui,QtCore
from UI_tp3 import Ui_MainWindow  # importing our generated file
import sys
import matplotlib.pyplot as plt
import glob
class mywindow(QtWidgets.QMainWindow):
    path1=""
    images=[]
    Y=[]
    def __init__(self):
    
        super(mywindow, self).__init__()
    
        self.ui = Ui_MainWindow()

        self.pathCar="DB2C/obj_car/*.jpg"
        self.pathShip="DB2C/obj_ship/*.jpg"
        self.ui.setupUi(self)
        self.path1=""
        self.ui.btn.clicked.connect(self.selectImg)
        self.apprentissage()
        self.test()



    # =========================================================================
    #  FUNCTION 
    # =========================================================================
    def selectImg(self):
        self.ui.dialog.setDirectory(QtCore.QDir.currentPath())
        self.ui.dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if self.ui.dialog.exec_() == QtWidgets.QDialog.Accepted:
            file_full_path = str(self.ui.dialog.selectedFiles()[0])
            print(("select file"))
        else:
            return None
        self.ui.resultat.setText(file_full_path)
        self.path1=file_full_path
        img=plt.imread(self.path1)
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)                       
        ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
        width = 120         ## New width and height to resize the image
        height = 80
        img = cv.resize(img, (width, height), interpolation=cv.INTER_AREA)
        img=np.array(img)                #
        img=img.flatten()
        pixmap = QtGui.QPixmap(self.path1)
        pixmap4 = pixmap.scaled(146,100, QtCore.Qt.KeepAspectRatio)
        self.ui.img.setPixmap(QtGui.QPixmap(pixmap4))
        self.ui.img.adjustSize()
        print(clf.predict([img]))
        
        self.ui.resultat.setText("L'objet que vous choisi est :"+clf.predict([img])[0])
        
        
    def ReadAndPrepare(self,ch,obj):
        path = glob.glob(ch)
        for path_img in path:
            img=plt.imread(path_img)  # reading image (Folder path and image name )
            img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)                       
            cv.threshold(img,127,255,cv.THRESH_BINARY)
            width = 120         ## New width and height to resize the image
            height = 80
            img = cv.resize(img, (width, height), interpolation=cv.INTER_AREA)
            img=np.array(img)                #
            img=img.flatten()                # Flatten image 
            self.images.append(img) 
            self.Y.append(obj)
            
            
    def apprentissage(self):
        import time
        self.ReadAndPrepare(self.pathCar,"CAR")
        self.ReadAndPrepare(self.pathShip,"SHIP")
        start=time.time()
        clf.fit(self.images,self.Y)
        end=time.time()
        predected=clf.predict(self.images)
        tauxApp=[]
        for i in range(0,len(self.Y)):
                 if self.Y[i] == predected[i]:
                    tauxApp.append(predected[i])
        print("Le temps d'execution :",end-start)
        print("Le taux de reconnaissance sur la base d'Apprentissage :",(len(tauxApp)/len(self.Y))*100)        
    def test(self):
        testD=[ "CAR",
                "CAR",
                "CAR",
                "CAR",
                "CAR",
                "CAR",
                "CAR",
                "CAR",
                "CAR",
                "CAR",
                "CAR",
                "SHIP",
                "SHIP",
                "SHIP",
                "SHIP",
                "SHIP",
                "SHIP",
                "SHIP",
                "SHIP",
                "SHIP",
                "SHIP"]
        folderT="DataToPredict/"
        tauxT=[]
        for file in range(1,22):
            img=plt.imread(folderT+str(file)+".jpg") # reading image (Folder path and image name )
            img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)                       
            cv.threshold(img,127,255,cv.THRESH_BINARY)
            width = 120         ## New width and height to resize the image
            height = 80
            img = cv.resize(img, (width, height), interpolation=cv.INTER_AREA)
            img=np.array(img)                #
            img=img.flatten()
            pred=clf.predict([img])
            if pred[0] == testD[file-1] :
                tauxT.append(pred[0])
        print("Le taux de reconnaissance sur la base de Test",(len(tauxT)/len(testD))*100)
    
app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())