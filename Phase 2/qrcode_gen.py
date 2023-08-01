import qrcode
from PIL import Image

response_mappings = {
    'north': 'A',
    'south': 'B',
    'west': 'C',
    'east': 'D'
}

# students = ["Student1","Student2","Student3","Student4","Student5","Student6","Student7","Student8","Student9","Student10","Student11","Student12","Student13","Student14","Student15","Student16","Student17","Student18","Student19","Student20","Student21","Student22","Student23","Student24","Student25","Student26","Student27","Student28","Student29","Student30"]
students = ['Student1','Student2','Student3']
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
