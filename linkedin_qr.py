# Install PyQRCode and pypng via terminal using 
# "-pip install PyQRCode and -pip install pypng"

import pyqrcode
import png

link = "https://www.linkedin.com/in/ivan-wu-900092218/"
qr_code = pyqrcode.create(link)
qr_code.png("LinkedInQR.png", scale = 5)
