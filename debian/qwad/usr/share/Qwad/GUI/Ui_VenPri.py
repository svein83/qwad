# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ssorgatem/Documents/python/qwad/GUI/VenPri.ui'
#
# Created: Mon Jul 27 19:07:42 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Qwad(object):
    def setupUi(self, Qwad):
        Qwad.setObjectName("Qwad")
        Qwad.resize(481, 296)
        Qwad.setMinimumSize(QtCore.QSize(481, 296))
        Qwad.setMaximumSize(QtCore.QSize(481, 296))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Qwad.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(Qwad)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 251))
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setObjectName("tabWidget")
        self.unpacktab = QtGui.QWidget()
        self.unpacktab.setObjectName("unpacktab")
        self.MuestraRutaWad = QtGui.QLineEdit(self.unpacktab)
        self.MuestraRutaWad.setGeometry(QtCore.QRect(160, 40, 241, 25))
        self.MuestraRutaWad.setObjectName("MuestraRutaWad")
        self.BotonRutaWad = QtGui.QToolButton(self.unpacktab)
        self.BotonRutaWad.setGeometry(QtCore.QRect(70, 40, 91, 25))
        self.BotonRutaWad.setObjectName("BotonRutaWad")
        self.MuestraRutaExtraer = QtGui.QLineEdit(self.unpacktab)
        self.MuestraRutaExtraer.setGeometry(QtCore.QRect(160, 110, 241, 25))
        self.MuestraRutaExtraer.setObjectName("MuestraRutaExtraer")
        self.BotonRutaExtraer = QtGui.QToolButton(self.unpacktab)
        self.BotonRutaExtraer.setGeometry(QtCore.QRect(70, 110, 91, 25))
        self.BotonRutaExtraer.setAutoRaise(False)
        self.BotonRutaExtraer.setArrowType(QtCore.Qt.NoArrow)
        self.BotonRutaExtraer.setObjectName("BotonRutaExtraer")
        self.Desempaqueta = QtGui.QPushButton(self.unpacktab)
        self.Desempaqueta.setGeometry(QtCore.QRect(170, 180, 121, 25))
        self.Desempaqueta.setObjectName("Desempaqueta")
        self.TMDviewer = QtGui.QWidget()
        self.TMDviewer.setObjectName("TMDviewer")
        self.TMDfilepath = QtGui.QLineEdit(self.TMDviewer)
        self.TMDfilepath.setGeometry(QtCore.QRect(150, 10, 241, 25))
        self.TMDfilepath.setObjectName("TMDfilepath")
        self.TMDfilebutton = QtGui.QToolButton(self.TMDviewer)
        self.TMDfilebutton.setGeometry(QtCore.QRect(60, 10, 91, 25))
        self.TMDfilebutton.setObjectName("TMDfilebutton")
        self.widget = QtGui.QWidget(self.TMDviewer)
        self.widget.setGeometry(QtCore.QRect(10, 50, 451, 147))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.TitleID = QtGui.QLabel(self.widget)
        self.TitleID.setObjectName("TitleID")
        self.gridLayout.addWidget(self.TitleID, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 2)
        self.idASCII = QtGui.QLabel(self.widget)
        self.idASCII.setObjectName("idASCII")
        self.gridLayout.addWidget(self.idASCII, 0, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.Version = QtGui.QLabel(self.widget)
        self.Version.setObjectName("Version")
        self.gridLayout.addWidget(self.Version, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.TitleType = QtGui.QLabel(self.widget)
        self.TitleType.setObjectName("TitleType")
        self.gridLayout.addWidget(self.TitleType, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.GroupID = QtGui.QLabel(self.widget)
        self.GroupID.setObjectName("GroupID")
        self.gridLayout.addWidget(self.GroupID, 2, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.BootIndex = QtGui.QLabel(self.widget)
        self.BootIndex.setObjectName("BootIndex")
        self.gridLayout.addWidget(self.BootIndex, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)
        self.AccessRights = QtGui.QLabel(self.widget)
        self.AccessRights.setObjectName("AccessRights")
        self.gridLayout.addWidget(self.AccessRights, 3, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.Contents = QtGui.QLabel(self.widget)
        self.Contents.setObjectName("Contents")
        self.gridLayout.addWidget(self.Contents, 4, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)
        self.Reserved = QtGui.QLabel(self.widget)
        self.Reserved.setObjectName("Reserved")
        self.gridLayout.addWidget(self.Reserved, 4, 4, 1, 1)
        self.IOSversion = QtGui.QLabel(self.widget)
        self.IOSversion.setObjectName("IOSversion")
        self.gridLayout.addWidget(self.IOSversion, 2, 1, 1, 1)
        self.packtab = QtGui.QWidget()
        self.packtab.setObjectName("packtab")
        self.MuestraRutaEmpaquetado = QtGui.QLineEdit(self.packtab)
        self.MuestraRutaEmpaquetado.setGeometry(QtCore.QRect(160, 110, 241, 25))
        self.MuestraRutaEmpaquetado.setObjectName("MuestraRutaEmpaquetado")
        self.MuestraRutaDesempaquetado = QtGui.QLineEdit(self.packtab)
        self.MuestraRutaDesempaquetado.setGeometry(QtCore.QRect(160, 40, 241, 25))
        self.MuestraRutaDesempaquetado.setObjectName("MuestraRutaDesempaquetado")
        self.BotonRutaEmpaquetado = QtGui.QToolButton(self.packtab)
        self.BotonRutaEmpaquetado.setGeometry(QtCore.QRect(70, 110, 91, 25))
        self.BotonRutaEmpaquetado.setAutoRaise(False)
        self.BotonRutaEmpaquetado.setArrowType(QtCore.Qt.NoArrow)
        self.BotonRutaEmpaquetado.setObjectName("BotonRutaEmpaquetado")
        self.BotonRutaDesempaquetado = QtGui.QToolButton(self.packtab)
        self.BotonRutaDesempaquetado.setGeometry(QtCore.QRect(70, 40, 91, 25))
        self.BotonRutaDesempaquetado.setObjectName("BotonRutaDesempaquetado")
        self.Empaqueta = QtGui.QPushButton(self.packtab)
        self.Empaqueta.setGeometry(QtCore.QRect(170, 180, 121, 25))
        self.Empaqueta.setObjectName("Empaqueta")
        self.NUStab = QtGui.QWidget()
        self.NUStab.setObjectName("NUStab")
        self.NusOutputPath = QtGui.QLineEdit(self.NUStab)
        self.NusOutputPath.setGeometry(QtCore.QRect(140, 150, 241, 25))
        self.NusOutputPath.setObjectName("NusOutputPath")
        self.Download_from_NUS = QtGui.QPushButton(self.NUStab)
        self.Download_from_NUS.setGeometry(QtCore.QRect(170, 180, 121, 25))
        self.Download_from_NUS.setObjectName("Download_from_NUS")
        self.NusOutputButton = QtGui.QToolButton(self.NUStab)
        self.NusOutputButton.setGeometry(QtCore.QRect(40, 150, 91, 25))
        self.NusOutputButton.setAutoRaise(False)
        self.NusOutputButton.setArrowType(QtCore.Qt.NoArrow)
        self.NusOutputButton.setObjectName("NusOutputButton")
        self.enteredTitleID = QtGui.QLineEdit(self.NUStab)
        self.enteredTitleID.setGeometry(QtCore.QRect(95, 45, 161, 25))
        self.enteredTitleID.setObjectName("enteredTitleID")
        self.TitleIDlabel = QtGui.QLabel(self.NUStab)
        self.TitleIDlabel.setGeometry(QtCore.QRect(40, 51, 101, 20))
        self.TitleIDlabel.setObjectName("TitleIDlabel")
        self.Title = QtGui.QLabel(self.NUStab)
        self.Title.setGeometry(QtCore.QRect(0, 10, 121, 21))
        self.Title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Title.setObjectName("Title")
        self.comboBox = QtGui.QComboBox(self.NUStab)
        self.comboBox.setGeometry(QtCore.QRect(125, 10, 150, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(QtCore.QString())
        self.comboBox2 = QtGui.QComboBox(self.NUStab)
        self.comboBox2.setGeometry(QtCore.QRect(280, 10, 170, 25))
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem(QtCore.QString())
        self.decryptCheck = QtGui.QCheckBox(self.NUStab)
        self.decryptCheck.setEnabled(False)
        self.decryptCheck.setGeometry(QtCore.QRect(40, 122, 130, 23))
        self.decryptCheck.setChecked(False)
        self.decryptCheck.setObjectName("decryptCheck")
        self.pack_in_WAD_checkbox = QtGui.QCheckBox(self.NUStab)
        self.pack_in_WAD_checkbox.setGeometry(QtCore.QRect(120, 122, 150, 23))
        self.pack_in_WAD_checkbox.setChecked(True)
        self.pack_in_WAD_checkbox.setObjectName("pack_in_WAD_checkbox")
        self.ChooseRegion = QtGui.QComboBox(self.NUStab)
        self.ChooseRegion.setGeometry(QtCore.QRect(230, 122, 150, 23))
        self.ChooseRegion.setObjectName("ChooseRegion")
        self.ChooseRegion.addItem(QtCore.QString())
        self.VersionlineEdit = QtGui.QLineEdit(self.NUStab)
        self.VersionlineEdit.setGeometry(QtCore.QRect(325, 45, 71, 25))
        self.VersionlineEdit.setObjectName("VersionlineEdit")
        self.versionlabel = QtGui.QLabel(self.NUStab)
        self.versionlabel.setGeometry(QtCore.QRect(265, 50, 51, 20))
        self.versionlabel.setObjectName("versionlabel")
        self.availableVersions = QtGui.QLabel(self.NUStab)
        self.availableVersions.setGeometry(QtCore.QRect(170, 81, 300, 40))
        self.availableVersions.setObjectName("availableVersions")
        self.availableLabel = QtGui.QLabel(self.NUStab)
        self.availableLabel.setGeometry(QtCore.QRect(40, 90, 120, 20))
        self.availableLabel.setObjectName("availableLabel")
        self.tabWidget.addTab(self.NUStab, "")
        self.tabWidget.addTab(self.unpacktab, "")
        self.tabWidget.addTab(self.packtab, "")
        self.tabWidget.addTab(self.TMDviewer, "")
        Qwad.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Qwad)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 481, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuAyuda = QtGui.QMenu(self.menuBar)
        self.menuAyuda.setObjectName("menuAyuda")
        Qwad.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(Qwad)
        self.statusBar.setObjectName("statusBar")
        Qwad.setStatusBar(self.statusBar)
        self.actionAcerca_de_Qwad = QtGui.QAction(Qwad)
        self.actionAcerca_de_Qwad.setIcon(icon)
        self.actionAcerca_de_Qwad.setObjectName("actionAcerca_de_Qwad")
        self.actionAbout_Qt = QtGui.QAction(Qwad)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/qt4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Qt.setIcon(icon1)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout_Wii_Signer = QtGui.QAction(Qwad)
        self.actionAbout_Wii_Signer.setObjectName("actionAbout_Wii_Signer")
        self.menuAyuda.addAction(self.actionAcerca_de_Qwad)
        self.menuAyuda.addAction(self.actionAbout_Qt)
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(Qwad)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Qwad)

    def retranslateUi(self, Qwad):
        Qwad.setWindowTitle(QtGui.QApplication.translate("Qwad", "Qwad - a WAD management tool", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaWad.setToolTip(QtGui.QApplication.translate("Qwad", "Ruta hacia el archivo WAD que quieres desempaquetar", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaWad.setText(QtGui.QApplication.translate("Qwad", "WAD file", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaExtraer.setToolTip(QtGui.QApplication.translate("Qwad", "Carpeta donde se almacenaran los contenidos del archivo WAD", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaExtraer.setText(QtGui.QApplication.translate("Qwad", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.Desempaqueta.setText(QtGui.QApplication.translate("Qwad", "Unpack", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unpacktab), QtGui.QApplication.translate("Qwad", "Unpack WAD", None, QtGui.QApplication.UnicodeUTF8))
        self.TMDfilebutton.setToolTip(QtGui.QApplication.translate("Qwad", "Ruta hacia el archivo WAD que quieres desempaquetar", None, QtGui.QApplication.UnicodeUTF8))
        self.TMDfilebutton.setText(QtGui.QApplication.translate("Qwad", "TMD file", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Qwad", "Title ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Qwad", "Title ID (ascii):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Qwad", "Title Version:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Qwad", "Title Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Qwad", "Required IOS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Qwad", "Group ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Qwad", "Boot index:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Qwad", "Access rights:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Qwad", "Contents:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Qwad", "Reserved:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TMDviewer), QtGui.QApplication.translate("Qwad", "TMD viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaEmpaquetado.setToolTip(QtGui.QApplication.translate("Qwad", "Carpeta y nombre del nuevo WAD", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaEmpaquetado.setText(QtGui.QApplication.translate("Qwad", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaDesempaquetado.setToolTip(QtGui.QApplication.translate("Qwad", "Ruta hacia la carpeta que empaquetar en WAD", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonRutaDesempaquetado.setText(QtGui.QApplication.translate("Qwad", "Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.Empaqueta.setText(QtGui.QApplication.translate("Qwad", "Pack", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.packtab), QtGui.QApplication.translate("Qwad", "Pack WAD", None, QtGui.QApplication.UnicodeUTF8))
        self.Download_from_NUS.setText(QtGui.QApplication.translate("Qwad", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.NusOutputButton.setToolTip(QtGui.QApplication.translate("Qwad", "Carpeta y nombre del nuevo WAD", None, QtGui.QApplication.UnicodeUTF8))
        self.NusOutputButton.setText(QtGui.QApplication.translate("Qwad", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.TitleIDlabel.setText(QtGui.QApplication.translate("Qwad", "Title ID", None, QtGui.QApplication.UnicodeUTF8))
        self.Title.setText(QtGui.QApplication.translate("Qwad", "Choose title:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Qwad", "Choose IOS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox2.setItemText(0, QtGui.QApplication.translate("Qwad", "Choose Region First!", None, QtGui.QApplication.UnicodeUTF8))
        self.ChooseRegion.setItemText(0, QtGui.QApplication.translate("Qwad", "Choose Region", None, QtGui.QApplication.UnicodeUTF8))
        self.decryptCheck.setText(QtGui.QApplication.translate("Qwad", "Decrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.pack_in_WAD_checkbox.setText(QtGui.QApplication.translate("Qwad", "Pack as WAD", None, QtGui.QApplication.UnicodeUTF8))
        self.versionlabel.setText(QtGui.QApplication.translate("Qwad", "Version:", None, QtGui.QApplication.UnicodeUTF8))
        self.availableLabel.setText(QtGui.QApplication.translate("Qwad", "Available Versions:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NUStab), QtGui.QApplication.translate("Qwad", "Download from NUS", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("Qwad", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAcerca_de_Qwad.setText(QtGui.QApplication.translate("Qwad", "About Qwad", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("Qwad", "About Qt", None, QtGui.QApplication.UnicodeUTF8))

import Qwad_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Qwad = QtGui.QMainWindow()
    ui = Ui_Qwad()
    ui.setupUi(Qwad)
    Qwad.show()
    sys.exit(app.exec_())

