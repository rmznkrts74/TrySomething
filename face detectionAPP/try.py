import face_recognition

# Kayıtlı yüzlerin fotoğraflarını yükle
known_image_1 = face_recognition.load_image_file("brad.jpg")
known_image_2 = face_recognition.load_image_file("kıvanc.jpg")
known_image_3 = face_recognition.load_image_file("ramazan.jpg")

# Kayıtlı yüzlerin özelliklerini hesapla
known_face_encoding_1 = face_recognition.face_encodings(known_image_1)[0]
known_face_encoding_2 = face_recognition.face_encodings(known_image_2)[0]
known_face_encoding_3 = face_recognition.face_encodings(known_image_3)[0]

#
import cv2
import face_recognition

# Kayıtlı yüzleri yükle
known_face_encodings = [known_face_encoding_1, known_face_encoding_2, ...] # kayıtlı yüz kodlarının listesi
known_face_names = ["Brad", "Kıvanc","Ramazan"] # kayıtlı yüzlerin isimlerinin listesi

# Sonsuz döngüde, kameradan görüntü yakala ve yüzleri tespit et
video_capture = cv2.VideoCapture(0) 

while True:
    # Görüntü yakala
    ret, frame = video_capture.read()

    # Yüzleri tespit et
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Tespit edilen yüzlerin etrafına dikdörtgen çiz ve eşleştirme yap
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Tespit edilen yüzü çıkar
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # Eşleşen yüzün adını bul
        name = "Bilinmiyor"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Tespit edilen yüzün etrafına dikdörtgen çiz ve ismini yaz
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Çıktı görüntüsünü göster
    cv2.imshow('Video', frame)

    # Çıkış yapmak için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizleme
video_capture.release()
cv2.destroyAllWindows()
