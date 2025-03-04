from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client


class SupabaseStorage(Storage):
    def __init__(self, bucket_name="storage-medics", **kwargs):
        self.bucket_name = bucket_name

        self.supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        self.storage_client = self.supabase.storage.from_(self.bucket_name)

    def _open(self, name, mode="rb"):
        # Implement the method to open a file from Supabase
        pass

    def _save(self, name, content):
        # Implement the method to save a file to Supabase
        print(content)
        content_file = content.file
        content_file.seek(0)  # Move the file pointer to the beginning
        content_bytes = content_file.read()
        data = self.supabase.storage.from_(self.bucket_name).upload(name, content_bytes)
        return data.json()["Key"]  # name/path of the file

    def exists(self, name):
        # Implement the method to check if a file exists in Supabase
        pass

    def url(self, name):
        # Implement the method to return the URL for a file in Supabase
        return f"{settings.SUPABASE_URL}/storage/v1/object/public/{name}"
