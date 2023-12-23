import qrcode

# Barkod metni
def barcode_olustur(data):

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

for j in range(1,26):
    barcode_olustur(j)
