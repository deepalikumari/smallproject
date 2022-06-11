import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size =10, #size of the box where qr code will be displayed
    border = 5 
)
data = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test.png")