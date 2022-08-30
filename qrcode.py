import pyqrcode
import png
from pyqrcode import QRCode

s="https://pranavsportifolio.netlify.app/"

url = pyqrcode.create(s)

url.svg("mqQr_code.svg" , scale=10)
url.png("mqQr_code.png" , scale=10)

