# Kütüphaneleri içe aktar
from PyQt5.QtWidgets import *
import sys
import sqlite3
import numpy as np
import cv2
from pyzbar.pyzbar import decode
import os

# PyQt uygulamasını başlat
uygulama = QApplication(sys.argv)

# AnaSayfa penceresini oluştur
anaSayfa_main_window = QMainWindow()

# AnaSayfa tasarımını içe aktar ve pencereyi ayarla
from ui_design.AnaSayfa_ui import *
anaSayfa_ui = Ui_Anasayfa_MainWindow()
anaSayfa_ui.setupUi(anaSayfa_main_window)
anaSayfa_main_window.show()

# HayvanEkle penceresini oluştur
from ui_design.hayvanEkle_ui import *
hayvanEkle_main_window = QMainWindow()
hayvanEkle_ui = Ui_hayvanEkle_MainWindow()
hayvanEkle_ui.setupUi(hayvanEkle_main_window)

# HayvanBilgisi penceresini oluştur
from ui_design.hayvanBilgisi_ui import *
hayvanBilgisi_main_window = QMainWindow()
hayvanBilgisi_ui = Ui_hayvanBilgisi_MainWindow()
hayvanBilgisi_ui.setupUi(hayvanBilgisi_main_window)

# SQLite veritabanı bağlantısını oluştur
conn = sqlite3.connect("database.db")
curs = conn.cursor()

# Hayvanlar tablosunu oluştur (eğer yoksa)
curs.execute("CREATE TABLE IF NOT EXISTS hayvanlar(kimlikNo INTEGER PRIMARY KEY AUTOINCREMENT,cins Text,cinsiyet Text,dogumTarihi Date,agirlik Float,saglikDurumu Text,ekstraBilgiler Text,konum Text)")

class CustomComboBox(QComboBox):
    def wheelEvent(self, event):
        event.ignore()

# QR kod oluşturacak fonksiyon
def Qr_olustur():
    data=hayvanBilgisi_main_window.windowTitle()
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
    try:
        os.makedirs("QR")
    except FileExistsError:
        pass
    img.save(f"QR/{data}.png")  # veya "barkod.jpg" olarak kaydedebilirsiniz
    hayvanBilgisi_ui.statusbar.showMessage(f"{data}- Qr oluşturuldu ",5000)

# Dosyadan  Qr okuma işlemi için bir fonksiyon 
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

# Kameradan  Qr okuma işlemi için bir fonksiyon 
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
    # Kullanıcı arayüzünden giriş al
    cins = hayvanEkle_ui.cins_lineEdit.text()
    cinsiyet = hayvanEkle_ui.cinsiyet_comboBox.currentText()
    dogumtarihi = hayvanEkle_ui.dogumTarihi_dateEdit.date().toPyDate()

    try:
        # Ağırlık bilgisini float'a dönüştür
        agirlik = float(hayvanEkle_ui.agirlik_lineEdit.text())
    except ValueError:
        # Hata durumunda kullanıcıya bilgi ver ve fonksiyondan çık
        hayvanEkle_ui.statusbar.showMessage("!! Ağırlık bilgisi istenen formata dönüştürülemedi !!")
        return ValueError 

    # Ekstra bilgileri al
    ekstrabilgiler = hayvanEkle_ui.ekstraBilgiler_textEdit.toPlainText()

    # Veritabanına hayvan bilgilerini ekle
    curs.execute("INSERT INTO hayvanlar (cins, cinsiyet, dogumTarihi, agirlik, saglikDurumu, ekstraBilgiler, konum) Values (?, ?, ?, ?, ?, ?, ?)",
                (cins, cinsiyet, dogumtarihi, agirlik, hayvanEkle_ui.saglik_comboBox_2.currentText(), ekstrabilgiler, "İçeride"))
    
    # Veritabanı değişikliklerini kaydet
    conn.commit()

    # Kullanıcıya başarı mesajını göster
    hayvanEkle_ui.statusbar.showMessage("Çiftliğinize başarıyla kaydedildi.")


def hayvanListele(icerde=True, disarda=True, erkek=True, disi=True):
    # Veritabanından hayvanları seç
    curs.execute("SELECT kimlikNo,cins,cinsiyet,dogumTarihi,agirlik,saglikDurumu,ekstraBilgiler,konum FROM hayvanlar")
    data = curs.fetchall()
    # Tabloyu doldur
    tabloDoldur(data, icerde, disarda, erkek, disi)

def kimlikleAra(kimlikNo):
    # Veritabanından belirli bir kimlik numarasına sahip hayvanı seç
    curs.execute("SELECT kimlikNo,cins,cinsiyet,dogumTarihi,agirlik,saglikDurumu,ekstraBilgiler,konum FROM hayvanlar WHERE kimlikNo = ?", (kimlikNo,))
    data = curs.fetchall()
    # Tabloyu doldur
    tabloDoldur(data)

def tabloDoldur(data, icerde=True, disarda=True, erkek=True, disi=True):
    # Tabloyu temizle
    anaSayfa_ui.tableWidget.clearContents()
    
    list1 = []
    list2 = []
    
    # İçeride ve dışarıda seçeneklerini listeye ekle
    if icerde:
        list1.append("İçeride")
    if disarda:
        list1.append("Dışarıda")
    
    # Erkek ve dişi seçeneklerini listeye ekle
    if erkek:
        list2.append("Erkek")
    if disi:
        list2.append("Dişi")
    
    counter = 0
    
    for kimlikNo, cins, cinsiyet, dogumTarihi, agirlik, saglikDurumu, ekstraBilgiler, konum in data:
        # Belirtilen konum ve cinsiyet seçeneklerine göre filtrele
        if (konum in list1) and (cinsiyet in list2):
            counter += 1
            anaSayfa_ui.tableWidget.setRowCount(counter)
            
            # Tabloya verileri ekle
            anaSayfa_ui.tableWidget.setItem(counter-1, 0, QTableWidgetItem(str(kimlikNo)))
            anaSayfa_ui.tableWidget.setItem(counter-1, 1, QTableWidgetItem(str(cins)))
            anaSayfa_ui.tableWidget.setItem(counter-1, 2, QTableWidgetItem(str(cinsiyet)))
            anaSayfa_ui.tableWidget.setItem(counter-1, 3, QTableWidgetItem(str(dogumTarihi)))
            anaSayfa_ui.tableWidget.setItem(counter-1, 4, QTableWidgetItem(str(agirlik)))

            combo_box = CustomComboBox()
            combo_box.addItems(["Sağlıklı","Hasta"])
            combo_box.setCurrentText(saglikDurumu)
            anaSayfa_ui.tableWidget.setCellWidget(counter-1, 5, combo_box)

            if saglikDurumu=="Sağlıklı":
                combo_box.setStyleSheet("background-color: rgb(200,150,185);")
            else:
                combo_box.setStyleSheet("background-color: red;")
            
            combo_box.currentTextChanged.connect(lambda : saglikGuncelle())

            anaSayfa_ui.tableWidget.setItem(counter-1, 6, QTableWidgetItem(str(konum)))
            
            # Sil butonu oluştur ve kırmızı renk uygula
            delete_button = QPushButton("Sil")
            delete_button.clicked.connect(lambda: hayvanSil())
            delete_button.setStyleSheet("background-color: red;")
            anaSayfa_ui.tableWidget.setCellWidget(counter-1, 7, delete_button)

            # İçerideki ve dışarıdaki hayvanları farklı renklerde göster
            if konum == "İçeride":
                tablo_row_renklendir(anaSayfa_ui.tableWidget, counter-1, QtGui.QColor(25, 240, 60))
            elif konum == "Dışarıda":
                tablo_row_renklendir(anaSayfa_ui.tableWidget, counter-1, QtGui.QColor(240, 20, 60))

def tablo_row_renklendir(tablo, row, color):
    # Belirtilen satır ve renge göre tablo satırını renklendir
    for col in range(tablo.columnCount()+1):
        item = tablo.item(row, col)
        if item:
            item.setBackground(color)

def hayvanSil():
    try:
        # Gönderen butonu belirle
        sender_button = anaSayfa_main_window.sender()
        if sender_button:
            # Gönderen butonun konumunu al
            index = anaSayfa_ui.tableWidget.indexAt(sender_button.pos())
            if index.isValid():
                # Konum geçerliyse, satırı al
                row = index.row()
                kimlikNo = anaSayfa_ui.tableWidget.item(row, 0).text()

                # Veritabanından hayvanı sil
                curs.execute("DELETE FROM hayvanlar WHERE kimlikNo = ?", (kimlikNo,))
                conn.commit()

                # Silme işlemi başarılı mesajı
                anaSayfa_ui.statusbar.showMessage(f"{kimlikNo} başarıyla silindi", 5000)
                # Hayvan listesini güncelle
                hayvanListele()

    except:
        # Hata durumunda mesaj göster
        anaSayfa_ui.statusbar.showMessage("! Masa Silme İşleminde hata oluştu !", 5000)

def hayvanEkle_Ac():
    # Hayvan ekle penceresini aç
    hayvanEkle_main_window.show()

def bilgiGuncelle():
    # Bilgileri güncelle
    kimlikNo = hayvanBilgisi_main_window.windowTitle()
    yeni_ekstra = hayvanBilgisi_ui.ekstraBilgiler_textEdit.toPlainText()
    curs.execute("UPDATE hayvanlar SET ekstraBilgiler = ? WHERE kimlikNo = ?", (yeni_ekstra, kimlikNo))
    conn.commit()
    
def saglikGuncelle():
    try:
        # Gönderen butonu belirle
        sender_button = anaSayfa_main_window.sender()
        if sender_button:
            # Gönderen butonun konumunu al
            index = anaSayfa_ui.tableWidget.indexAt(sender_button.pos())
            if index.isValid():
                # Konum geçerliyse, satırı al
                row = index.row()
                kimlikNo = anaSayfa_ui.tableWidget.item(row, 0).text()
                saglikDurumu =sender_button.currentText()

                curs.execute("UPDATE hayvanlar SET saglikDurumu = ? WHERE kimlikNo = ?", (saglikDurumu, kimlikNo))

                conn.commit()

                anaSayfa_ui.statusbar.showMessage(f"{kimlikNo} başarıyla güncellendi", 5000)
                hayvanListele()

    except:
        # Hata durumunda mesaj göster
        anaSayfa_ui.statusbar.showMessage("! Hayvan güncelleme işleminde bir hata oluştu !", 5000)
def bilgiGetir():
    # Bilgileri getir
    hayvanBilgisi_main_window.show()
    sender_combo = anaSayfa_main_window.sender()
    if sender_combo:
        try:
            # Seçili satırdaki kimlik numarasını al
            kimlikNo = anaSayfa_ui.tableWidget.selectedItems()[0].text()
        except:
            kimlikNo = -1
        hayvanBilgisi_main_window.setWindowTitle(str(kimlikNo))
        curs.execute("SELECT ekstraBilgiler FROM hayvanlar WHERE kimlikNo = ?", (kimlikNo,))
        data = curs.fetchone()
        for i in data:
            hayvanBilgisi_ui.ekstraBilgiler_textEdit.setText(i)

# Ekstra bilgilerin değiştiğinde güncelleme işlemini tetikleyen bağlantı
hayvanBilgisi_ui.ekstraBilgiler_textEdit.textChanged.connect(lambda: bilgiGuncelle())

# QR kod oluşturma işlemini tetikleyen bağlantı
hayvanBilgisi_ui.QROlustur_pushButton.clicked.connect(lambda: Qr_olustur())

# Tablodaki bir hücreye çift tıklanıldığında bilgi getirme işlemini tetikleyen bağlantı
anaSayfa_ui.tableWidget.doubleClicked.connect(lambda: bilgiGetir())

# Kimlik numarasına göre arama işlemini tetikleyen bağlantı
anaSayfa_ui.kimlikNoAra_pushButton.clicked.connect(lambda: kimlikleAra(anaSayfa_ui.kimlikNo_lineEdit.text()))

# Yeni hayvan ekleme penceresini açma işlemini tetikleyen bağlantı
anaSayfa_ui.hayvanEkle_pushButton.clicked.connect(lambda: hayvanEkle_Ac())

# İçeri veya dışarı QR kodunu taratma işlemini tetikleyen bağlantılar
anaSayfa_ui.QrOkut_giris.clicked.connect(lambda: Qr_oku_video("İçeride"))
anaSayfa_ui.QrOkut_cikis.clicked.connect(lambda: Qr_oku_video("Dışarıda"))

# Tüm hayvanları listeleme işlemini tetikleyen bağlantı
anaSayfa_ui.butunHayvanlariListele_pushButton.clicked.connect(lambda: hayvanListele())

# Belirli koşullara göre uygun hayvanları listeleme işlemini tetikleyen bağlantı
anaSayfa_ui.uygunHayvanListele_pushButton.clicked.connect(lambda:
    hayvanListele(
        anaSayfa_ui.icerde_checkBox.isChecked(),
        anaSayfa_ui.disarida_checkBox.isChecked(),
        anaSayfa_ui.erkek_checkBox.isChecked(),
        anaSayfa_ui.disi_checkBox.isChecked()
    ))

# Yeni hayvan ekleme işlemini tetikleyen bağlantı
hayvanEkle_ui.hayvanEkle_pushButton.clicked.connect(lambda: hayvanEkle())

sys.exit(uygulama.exec_())

