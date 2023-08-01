import qrcode
from PIL import Image
response_mappings = {
    'north': 'A',
    'south': 'B',
    'west': 'C',
    'east': 'D'
}

students = ['Student1', 'Student2', 'Student3', ...]

for student in students:
    
    qr_content = f"Student: {student}"

   
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    
    qr.add_data(qr_content)
    qr.make(fit=True)

    
    qr_img = qr.make_image(fill_color="black", back_color="white")

    
    qr_img.save(f"{student}.png")
