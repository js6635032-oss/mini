import qrcode

url = "https://js6635032-oss.github.io/mini/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=5
)

qr.add_data(url)
qr.make(fit=True)

imagen = qr.make_image(
    fill_color="black",
    back_color="white"
)

imagen.save("QR_AMOR_FINAL.png")

print("❤️ QR creado correctamente ❤️")
print("Página:", url)
print("Archivo: QR_AMOR_FINAL.png")