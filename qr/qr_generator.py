import pyqrcode, sys

def generate_qr_code(code):
    url = pyqrcode.create('http://lr-prove-it.herokuapp.com/checkreference/%s' % code)
    url.svg('static/prove-it.svg', scale=4, module_color="#7D007D")
    return True
