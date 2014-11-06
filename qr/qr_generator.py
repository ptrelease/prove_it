import pyqrcode, sys
import os.path

def generate_qr_code(code):

    if os.path.exists("/static/prove-it.svg"):
        os.remove("/static/prove-it.svg")

    url = pyqrcode.create('http://lr-prove-it.herokuapp.com/checkreference/%s' % code)
    url.svg('static/prove-it.svg', scale=4, module_color="#7D007D")
    return True
