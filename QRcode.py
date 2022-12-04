import pyqrcode
import png
from pyqrcode import QRCode

url = "www.igoraza.com"

s = pyqrcode.create(url)
s.svg("igorza.svg",scale=8)
s.png("igoraza.png",scale=8)


