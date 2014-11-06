import pyqrcode, sys

def generate_qr_code(code):
    url = pyqrcode.create('http://prove-it.gov.uk/checkreference/%s' % code)
    url.svg('static/prove-it.svg', scale=4, module_color="#7D007D")
    return True