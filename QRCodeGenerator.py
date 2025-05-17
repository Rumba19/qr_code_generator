import qrcode

def generate_qr_code(url):
    """
    Generates a QR Code from the provided URL and saves it as an image file.
    
    Args:
        url (str): The URL to be converted into a QR code.
    """
    # Generate the QR Code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # level of error correction
        box_size=10,  # size of each box in the QR code grid
        border=4,  # thickness of the border
    )
    
    qr.add_data(url)
    qr.make(fit=True)

    # Create the image for the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the generated image
    img.save('qrcode.png')

    print("QR Code generated and saved as 'qrcode.png'")

# Example usage
if __name__ == "__main__":
    url = input("Enter the URL to generate a QR Code: ")
    generate_qr_code(url)

