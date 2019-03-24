from gataConverter.scripts.readtable import Data
from gataConverter.scripts.Arlequin_structure import Arlequin
from gataConverter.scripts.R_structure import R
from django.core.files.storage import FileSystemStorage
import os
import zipfile
import shutil

class Converter:

    directoryPath = "gataConverter/tmp/"

    def __init__(self, file, formats):
        self.file = file
        self.formats = formats

    def convert(self):
        filename = self.save_file()
        data = Data(filename)
        if 'a' in self.formats:
            Arlequin(data)
        if 'r' in self.formats:
            R(data)
        os.remove(filename)
        zipFile = self.createZipFile()
        self.deleteTmpFiles()
        return zipFile

    def save_file(self):
        fs = FileSystemStorage()
        filename = fs.save(self.directoryPath+self.file.name, self.file)
        return filename

    def createZipFile(self):
        zipFilename = shutil.make_archive("output", 'zip', self.directoryPath)
        zipFile = open(zipFilename, 'rb')
        os.remove(zipFilename)
        return zipFile

    def deleteTmpFiles(self):
        for the_file in os.listdir(self.directoryPath):
            file_path = os.path.join(self.directoryPath, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)