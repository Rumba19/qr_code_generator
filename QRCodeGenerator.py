import qrcode

def generate_qr_code(url):

    # Generate the QR Code
    qr = qrcode.QRCode(
        version=1,   
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # level of error correction
        box_size=10,   
        border=4,   
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    # Create the image for the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the generated image
    img.save('qrcode.png')

    print("QR Code generated and saved as 'qrcode.png'")
 
if __name__ == "__main__":
    url = input("Enter the URL to generate a QR Code: ")
    generate_qr_code(url)

