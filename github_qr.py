# Install PyQRCode and pypng via terminal using 
# "-pip install PyQRCode and -pip install pypng"

import pyqrcode
import png

link = "https://github.com/bluccii"
qr_code = pyqrcode.create(link)
qr_code.png("GithubQR.png", scale = 5)
