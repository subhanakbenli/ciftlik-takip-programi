# # kütüphaneler 
from PyQt5.QtWidgets import *
import sys
import sqlite3
import datetime

from AnaSayfa_ui import *
uygulama = QApplication(sys.argv)
anaSayfa_main_window = QMainWindow()
anaSayfa_ui = Ui_Anasayfa_MainWindow()
anaSayfa_ui.setupUi(anaSayfa_main_window)
anaSayfa_main_window.show()

from hayvanEkle_ui import *
hayvanEkle_main_window = QMainWindow()
hayvanEkle_ui =  Ui_hayvanEkle_MainWindow()
hayvanEkle_ui.setupUi(hayvanEkle_main_window)

conn=sqlite3.connect("database.db")
curs=conn.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS hayvanlar(kimlikNo INTEGER PRIMARY KEY AUTOINCREMENT,cins Text,cinsiyet Text,dogumTarihi Date,agirlik Float,saglikDurumu Text,ekstraBilgiler Text,konum Text)")



# QR kod oluşturacak fonksiyon
def Qr_olustur(data):
    import qrcode 
     # Barkodu oluştur
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Barkodu bir PIL (Pillow) görüntüsü olarak al
    img = qr.make_image(fill_color="black", back_color="white")

    # Görüntüyü kaydet
    img.save(f"QR/{data}.png")  # veya "barkod.jpg" olarak kaydedebilirsiniz
# Qr okuma işlemi için bir fonksiyon
def Qr_oku(image_path):
    import cv2
    from pyzbar.pyzbar import decode
    # Resmi yükle
    image = cv2.imread(image_path)
    
    # Barkodları tespit etmek için decode() kullanın
    decoded_objects = decode(image)

    for obj in decoded_objects:
        # Barkodu ve türünü alın
        barcode_data = obj.data.decode('utf-8')
        # barcode_type = obj.type
        return barcode_data
        # Barkodu ve türünü ekrana yazdırın
        # print(f'Tür: {barcode_type}, Barkod: {barcode_data}')
    return None

def hayvanEkle():
    cins=hayvanEkle_ui.cins_lineEdit.text()
    cinsiyet=hayvanEkle_ui.cinsiyet_comboBox.currentText()
    dogumtarihi=hayvanEkle_ui.dogumTarihi_dateEdit.date().toPyDate()
    try:    agirlik=float(hayvanEkle_ui.agirlik_lineEdit.text())
    except:
        hayvanEkle_ui.statusbar.showMessage("!!Ağırlık bilgisi istenen \nformata dönüştürülemedi!! ")
        return ValueError 
    ekstrabilgiler = hayvanEkle_ui.ekstraBilgiler_textEdit.toPlainText()

    curs.execute("INSERT INTO hayvanlar (cins,cinsiyet,dogumTarihi,agirlik,saglikDurumu,ekstraBilgiler,konum) Values(?,?,?,?,?,?,?)",
                (cins,cinsiyet,dogumtarihi,agirlik,hayvanEkle_ui.saglik_comboBox_2.currentText(),ekstrabilgiler,"İçeride"))
    conn.commit()
    hayvanEkle_ui.statusbar.showMessage("Çiftliğinize başarıyla kaydedildi.")

def hayvanListele(icerde=True,disarda=True,erkek=True,disi=True):
    
    curs.execute("SELECT kimlikNo,cins,cinsiyet,dogumTarihi,agirlik,saglikDurumu,ekstraBilgiler,konum FROM hayvanlar")
    data = curs.fetchall()
    tabloDoldur(data,icerde,disarda,erkek,disi)

def tabloDoldur(data,icerde,disarda,erkek,disi):
    list1=[]
    list2=[]
    if icerde:
        list1.append("İçeride")
    if disarda:
        list1.append("Dışarıda")
    if erkek:
        list2.append("Erkek")
    if disi:    
        list2.append("Dişi")
    counter=0
    for kimlikNo,cins,cinsiyet,dogumTarihi,agirlik,saglikDurumu,ekstraBilgiler,konum in data:
        if (konum in list1) and (cinsiyet in list2):
            counter+=1
            anaSayfa_ui.tableWidget.setRowCount(counter)
            anaSayfa_ui.tableWidget.setItem(counter-1,0,QTableWidgetItem(str(kimlikNo)))
            anaSayfa_ui.tableWidget.setItem(counter-1,1,QTableWidgetItem(str(cins)))
            anaSayfa_ui.tableWidget.setItem(counter-1,2,QTableWidgetItem(str(cinsiyet)))
            anaSayfa_ui.tableWidget.setItem(counter-1,3,QTableWidgetItem(str(dogumTarihi)))
            anaSayfa_ui.tableWidget.setItem(counter-1,4,QTableWidgetItem(str(agirlik)))
            anaSayfa_ui.tableWidget.setItem(counter-1,5,QTableWidgetItem(str(saglikDurumu)))
            anaSayfa_ui.tableWidget.setItem(counter-1,6,QTableWidgetItem(str(konum)))
    anaSayfa_ui.tableWidget
        

def hayvanEkle_Ac():
    hayvanEkle_main_window.show()






anaSayfa_ui.hayvanEkle_pushButton.clicked.connect(lambda : hayvanEkle_Ac())
anaSayfa_ui.butunHayvanlariListele_pushButton.clicked.connect(lambda :
    hayvanListele(
        anaSayfa_ui.icerde_checkBox.isChecked(),
        anaSayfa_ui.disarida_checkBox.isChecked(),
        anaSayfa_ui.erkek_checkBox.isChecked(),
        anaSayfa_ui.disi_checkBox.isChecked()
    ))
hayvanEkle_ui.hayvanEkle_pushButton.clicked.connect(lambda : hayvanEkle())

sys.exit(uygulama.exec_())

