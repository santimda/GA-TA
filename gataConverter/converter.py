from gataConverter.scripts.readtable import Data
from gataConverter.scripts.Arlequin_structure import Arlequin
from gataConverter.scripts.R_structure import R
from gataConverter.scripts.Structure_structure import Structure
from django.core.files.storage import FileSystemStorage
from xlrd import XLRDError
import os
import zipfile
import shutil

class Converter:

    directoryPath = "gataConverter/tmp/convertedFiles/"
    zipFilePath = "gataConverter/tmp/output"

    def __init__(self, file = None, formats = None):
        self.file = file
        self.formats = formats

    def convert(self):
        filename = self.save_file()
        try:
            data = Data(filename)
            if 'a' in self.formats:
                Arlequin(data)
            if 'r' in self.formats:
                R(data)
            if 's' in self.formats:
                Structure(data)
            os.remove(filename)
            zipFile = self.createZipFile()
        except XLRDError:
            raise XLRDError
        finally:
            self.deleteTmpFiles()
        return zipFile

    def save_file(self):
        fs = FileSystemStorage()
        filename = fs.save(self.directoryPath+self.file.name, self.file)
        return filename

    def createZipFile(self):
        zipFilename = shutil.make_archive(self.zipFilePath, 'zip', self.directoryPath)
        return zipFilename

    def deleteTmpFiles(self):
        for the_file in os.listdir(self.directoryPath):
            file_path = os.path.join(self.directoryPath, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)

    def getAndDeleteZipFile(self):
        zipFilename = self.zipFilePath+".zip"
        zipFile = open(zipFilename, 'rb')
        os.remove(zipFilename)
        return zipFile
