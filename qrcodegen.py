# QR 코드 생성기, 파일명 지정은 옵션
# python qrcodegen.py "https://forms.gle/vhn99ZD1Gri1eh6b7" "custom_name.png"


import qrcode
import sys

def generate_qr(url, filename="qrcode.png"):
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size (minimum is 4)
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code as an image file
    img.save(filename)
    print(f"QR code generated and saved as '{filename}'")

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <URL>")
        sys.exit(1)
    
    # Get the URL from the command-line arguments
    url = sys.argv[1]
    
    # Generate the QR code
    generate_qr(url)
