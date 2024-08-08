import base64
import segno
import os

class QRCodeGenerator():
    
    
    def convert_image_to_encoded_string(self, image_path:str):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    
    def create_qr_code(self, document_id:str):
        print("create qr code method: ",document_id)
        
        qrcode = segno.make_qr(document_id)
        file_path = f"{document_id}.png"
        qrcode.save(file_path, scale=10)
        
        qrcode_encoded = self.convert_image_to_encoded_string(file_path)
        image_string = qrcode_encoded.decode('utf-8')
        
        # remove file
        os.remove(file_path)
        
        
        print(image_string)
        
        return 'data:image/png;base64,' + image_string