
import cv2
from pyzbar.pyzbar import decode

# Barkod okuma işlemi için bir fonksiyon tanımlayın
def read_barcodes(image_path):
    # Resmi yükle
    image = cv2.imread(image_path)

    # Barkodları tespit etmek için decode() kullanın
    decoded_objects = decode(image)

    for obj in decoded_objects:
        # Barkodu ve türünü alın
        barcode_data = obj.data.decode('utf-8')
        barcode_type = obj.type

        # Barkodu ve türünü ekrana yazdırın
        print(f'Tür: {barcode_type}, Barkod: {barcode_data}')

# Barkodları okumak istediğiniz fotoğrafın yolunu belirtin
image_path = 'QR\sd.png'

# Barkodları okuma fonksiyonunu çağırın
read_barcodes(image_path)

