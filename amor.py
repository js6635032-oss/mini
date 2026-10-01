import qrcode

# Mensaje que aparecerá al escanear el QR
mensaje = """
❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️

       TE AMO
     MI AMOR ❤️

❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️
"""

# Crear el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Agregar el mensaje
qr.add_data(mensaje)
qr.make(fit=True)

# Crear imagen del QR
imagen = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Guardar el QR
imagen.save("qr_te_amo.png")

print("❤️ ¡Código QR creado correctamente! ❤️")
print("El archivo se guardó como: qr_te_amo.png")