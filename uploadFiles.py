import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Xm-KS6BySOsAAAAAAAAAAdb0KtP3k7-TL9f_UitDkwqu_sJau7r2dQKq2CIb7ach'
    transferData = TransferData(access_token)

    file_from = input("Enter File Path To Transfer: ")
    file_to = input("Enter File Path To Upload: ")

    transferData.upload_file(file_from, file_to)
    print("File Moved.")

main()