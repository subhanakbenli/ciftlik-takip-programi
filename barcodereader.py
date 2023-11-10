import cv2
from pyzbar.pyzbar import decode

def main():
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
                cv2.polylines(frame, [points], isClosed=True, color=(0, 255, 0), thickness=2)

            # QR kodu ekrana yazdır
            cv2.putText(frame, qr_data, (obj.rect.left, obj.rect.top - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

            print(f"QR Kodu: {qr_data}")

        # Kameradan alınan kareyi göster
        cv2.imshow('QR Kod Okuyucu', frame)

        # Çıkış için 'q' tuşuna basın
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera kapatma
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import numpy as np
    main()
