from rest_framework import serializers
from Books_Archive.models import Books

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    file_url = serializers.SerializerMethodField()
    file = serializers.ImageField(write_only=True)  # set write_only to True if you want to hide file field in query result.

    class Meta:
        model = Books
        fields = '__all__'

    #  get full path of where the images where saved
    def get_file_url(self, gallary_class):
        file_url_unsecured = gallary_class.file.url
        file_url = file_url_unsecured.replace('http', 'https')

        return file_url
