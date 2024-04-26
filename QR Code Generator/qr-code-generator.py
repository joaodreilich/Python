# IMPORT MODULES
import qrcode


# DECLARATIONS
VERSION = '0.02'
OPTIONS = ['0', '1', '2']


# FUNCTIONS
def get_data_type_input(show_text:str):
    '''Verification if user input is valid in a list of correct possibilities (OPTIONS)

    Args:
        show_text (str): Question for user to input a valid answer

    Returns:
        str: String that contains value that exists in OPTIONS
    '''
    while True:
        try:
            data_type = str(input('Select one: '))
            if data_type in OPTIONS:
                return data_type
        except ValueError:
            print('INCORRECT VALUE!')
            print('Please select a valid option!')
            print('1 for URL (https://site.com), 2 for PLAIN TEXT or 0 to EXIT')

def str_url_treatment(url):
    '''Treats a given string to a standard.
    i.e: https://url.com

    Args:
        url (string): user input data
    '''

    url = url.strip()
    url = url.replace(' ', '')
    url = url.casefold()

    if 'https://' or 'http://' not in url:
        url = 'http://' + url
    
    return url


# SPLASH SCREEN
print('=' * 20)
print('Welcome to PYTHON QR CODE GENERATOR')
print('v' + VERSION)
print('=' * 20)
print()


# USER INPUT DATA TO QR CODE
print('Please select what data type will you insert:')
print('1 for URL (https://site.com), 2 for PLAIN TEXT or 0 to EXIT')
data_type = str(get_data_type_input('Select one: '))

# LOOP TO POSSIBLE OUTPUTS
while data_type in ['1', '2']:
    if data_type == '1':
        print()
        url = str(input('Please, type your URL: '))
        data = str_url_treatment(url)
    elif data_type == '2':
        data = str(input('Type your PLAIN TEXT: '))


    # QR CODE GENERATION
    print()
    print('GENERATING QR CODE...')
    qrImg = qrcode.make(data)


    # USER INPUT FILENAME
    print()
    outputName = str(input('What will be the file name? ')) + '.png'


    # QR CODE IMAGE EXPORT
    print()
    print('COMPLETED!')
    print('Thank you! See you later!')
    qrImg.save(outputName)
    break
else:
    print('Thanks! See you later!')