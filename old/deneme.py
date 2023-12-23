import cv2
from pyzbar.pyzbar import decode

def qr_code_reader(video_device=0):
    """
    Verilen bir video cihazından QR kodlarını okur ve videoyu bir pencerede gösterir.
    
    :param video_device: Kamera cihaz numarası (varsayılan olarak 0).
    :return: QR kod verilerini içeren bir liste.
    """
    cap = cv2.VideoCapture(video_device)
    qr_codes = []

    cv2.namedWindow("QR Code Reader", cv2.WINDOW_NORMAL)  # Pencereyi oluştur

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        decoded_objects = decode(frame)

        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            qr_codes.append(barcode_data)

        for obj in decoded_objects:
            # Barkodu ve türünü çerçeve üzerine çizin
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (0, 255, 0), 3)
            else:
                cv2.polylines(frame, [points], True, (0, 255, 0), 3)

            # Barkodu ve türünü ekrana yazdırın
            cv2.putText(frame, barcode_data, (obj.rect.left, obj.rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("QR Code Reader", frame)  # Pencerede görüntüyü göster

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return qr_codes

if __name__ == "__main__":
    qr_data = qr_code_reader()
    print("QR Kodlar:", qr_data)
