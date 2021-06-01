import cv2 #pemanggilan library

img = cv2.imread('BpkJk.jpg') #untuk membaca file Foto

wajah = cv2.CascadeClassifier('face-detect.xml') #untuk melakukan load XML untuk medeteksi wajah


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #menterjemahkan foto dalam bntuk gray

wajah = wajah.detectMultiScale(gray, 1.3, 5) #untuk mendetek gray yang ada difotonya
for (x,y,w,h) in wajah: #perulangan For untuk pembacaan atau perulangan pada foto, pada sumbuh x,y,w,h
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) #untuk mendeteksi gray pada sumbuh x,y

    cv_warna = img[y:y+h, x:x+w]
    cv_gray = gray[y:y+h, x:x+w]

cv2.imshow('Foto Normal', img) #untuk memunculkan foto yang kita baca tadi
cv2.waitKey(0) #tidak ada jeda, langsung dimunculkan
cv2.destroyAllWindows() #setelah integrasi diatas berhasil,deteksinya dijalankan
