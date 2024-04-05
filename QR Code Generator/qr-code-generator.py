# IMPORT MODULES
import qrcode

# USER INPUT DATA TO QR CODE
data = str(input('Type what information you want to show with QR Code (if it is an URL type the complete path, ie. https://mysite.com): '))

# QR CODE GENERATION
qrImg = qrcode.make(data)

# USER INPUT FILENAME
outputName = str(input('What will be the file name? ')) + '.png'

# QR CODE IMAGE EXPORT
qrImg.save(outputName)