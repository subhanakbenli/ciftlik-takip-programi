# # kütüphaneler 
from PyQt5.QtWidgets import *
import sys
import sqlite3
import datetime
import numpy as np
from AnaSayfa_ui import *
import cv2
from pyzbar.pyzbar import decode

uygulama = QApplication(sys.argv)
anaSayfa_main_window = QMainWindow()
anaSayfa_ui = Ui_Anasayfa_MainWindow()
anaSayfa_ui.setupUi(anaSayfa_main_window)
anaSayfa_main_window.show()

from hayvanEkle_ui import *
hayvanEkle_main_window = QMainWindow()
hayvanEkle_ui =  Ui_hayvanEkle_MainWindow()
hayvanEkle_ui.setupUi(hayvanEkle_main_window)

from hayvanBilgisi_ui import *
hayvanBilgisi_main_window = QMainWindow()
hayvanBilgisi_ui =  Ui_hayvanBilgisi_MainWindow()
hayvanBilgisi_ui.setupUi(hayvanBilgisi_main_window)

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


def Qr_oku_video(konum):
    # Kamera başlatma
    cap = cv2.VideoCapture(0)

    while True:
        # Kameradan bir kareyi al
        ret, frame = cap.read()

        # QR kodları tespit et
        decoded_objects = decode(frame)

        # Her bir QR kodunu işle
        for obj in decoded_objects:
            # QR kodunun içeriğini al
            qr_data = obj.data.decode('utf-8')

            # QR kodunun konumunu çiz
            points = obj.polygon
            if len(points) == 4:
                points = [(point.x, point.y) for point in points]  # Köşe noktalarını çiftler halinde al

                # Köşe noktalarını birleştirip çizgi çiz
                points = np.array(points, dtype=int)
                cv2.polylines(frame, [points], isClosed=True, color=(0, 255, 0), thickness=4)

            # QR kodu ekrana yazdır
            cv2.putText(frame, qr_data, (obj.rect.left, obj.rect.top - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

            print(f"QR Kodu: {qr_data}")
            curs.execute("UPDATE hayvanlar SET konum = ? WHERE kimlikNo = ?", (konum, qr_data))
            conn.commit()
        # Kameradan alınan kareyi göster
        cv2.imshow('QR Kod Okuyucu', frame)

        # Çıkış için 'q' tuşuna basın
        if cv2.waitKey(1) & 0xFF == ord('q'):            break

    # Kamera kapatma
    cap.release()
    cv2.destroyAllWindows()
    hayvanListele()

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

def kimlikleAra(kimlikNo):
    curs.execute("SELECT kimlikNo,cins,cinsiyet,dogumTarihi,agirlik,saglikDurumu,ekstraBilgiler,konum FROM hayvanlar Where kimlikNo = ?",(kimlikNo,))
    data = curs.fetchall()
    tabloDoldur(data)
       
 
def tabloDoldur(data,icerde=True,disarda=True,erkek=True,disi=True):
    anaSayfa_ui.tableWidget.clearContents()
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
            
            if konum=="İçeride":
                tablo_row_renklendir(anaSayfa_ui.tableWidget,counter-1,QtGui.QColor(25, 240, 60))
            if konum=="Dışarıda":
                tablo_row_renklendir(anaSayfa_ui.tableWidget,counter-1,QtGui.QColor(240, 20, 60))              

def tablo_row_renklendir(tablo,row,color):
    for col in range(tablo.columnCount()+1):
        item = tablo.item(row, col)
        if item:
            item.setBackground(color)    
        

def hayvanEkle_Ac():
    hayvanEkle_main_window.show()

def bilgiGuncelle():
    kimlikNo=hayvanBilgisi_main_window.windowTitle()
    yeni_ekstra = hayvanBilgisi_ui.ekstraBilgiler_textEdit.toPlainText() 
    curs.execute("UPDATE hayvanlar SET ekstraBilgiler = ? WHERE kimlikNo = ?", (yeni_ekstra,kimlikNo))
    conn.commit()
    
def bilgiGetir():
    hayvanBilgisi_main_window.show()
    sender_combo = anaSayfa_main_window.sender()
    if sender_combo:
        try:
            kimlikNo = anaSayfa_ui.tableWidget.selectedItems()[0].text()
        except:
            kimlikNo = -1
        hayvanBilgisi_main_window.setWindowTitle(str(kimlikNo))
        curs.execute("SELECT ekstraBilgiler FROM hayvanlar WHERE kimlikNo = ?", (kimlikNo,))
        data=curs.fetchone()
        for i in data:
                hayvanBilgisi_ui.ekstraBilgiler_textEdit.setText(i)
                
hayvanBilgisi_ui.ekstraBilgiler_textEdit.textChanged.connect(lambda : bilgiGuncelle())

anaSayfa_ui.tableWidget.doubleClicked.connect(lambda : bilgiGetir())
anaSayfa_ui.kimlikNoAra_pushButton.clicked.connect(lambda : kimlikleAra(anaSayfa_ui.kimlikNo_lineEdit.text()))
anaSayfa_ui.hayvanEkle_pushButton.clicked.connect(lambda : hayvanEkle_Ac())
anaSayfa_ui.QrOkut_giris.clicked.connect(lambda :   Qr_oku_video("İçeride") )
anaSayfa_ui.QrOkut_cikis.clicked.connect(lambda :   Qr_oku_video("Dışarıda") )
anaSayfa_ui.butunHayvanlariListele_pushButton.clicked.connect(lambda :
    hayvanListele())
anaSayfa_ui.uygunHayvanListele_pushButton.clicked.connect(lambda :
    hayvanListele(
        anaSayfa_ui.icerde_checkBox.isChecked(),
        anaSayfa_ui.disarida_checkBox.isChecked(),
        anaSayfa_ui.erkek_checkBox.isChecked(),
        anaSayfa_ui.disi_checkBox.isChecked()
    ))
hayvanEkle_ui.hayvanEkle_pushButton.clicked.connect(lambda : hayvanEkle())

sys.exit(uygulama.exec_())

