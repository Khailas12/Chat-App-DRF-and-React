from rest_framework.test import APITestCase
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from six import BytesIO
from PIL import Image


def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    data = BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


class TestFileUpload(APITestCase):
    file_upload_url = '/message/file-upload'

    def test_file_uplpad(self):
        the_image = create_image(None, 'batman.png')
        the_image_file = SimpleUploadedFile('font.png', the_image.getvalue())
        data = {
            
        }
