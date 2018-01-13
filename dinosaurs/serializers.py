from dinosaurs.models import Hashtag, Note, Person, Questionnaire
from rest_framework import serializers
from django.contrib.auth.models import Group

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Note.objects.all())
    # folders = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Folder.objects.all())
    hashtags = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Hashtag.objects.all())

    class Meta:
        model = Person
        fields = ('id', 'username', 'email', 'password', 'notes', 'hashtags')

# class FolderSerializer(serializers.HyperlinkedModelSerializer):
#     notes = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Note.objects.all())

#     class Meta:
#         model = Folder
#         fields = ('id', 'name', 'parent', 'is_root', 'notes')

class HashtagSerializer(serializers.HyperlinkedModelSerializer):
    # notes = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Note.objects.all())

    class Meta:
        model = Hashtag
        fields = ('id', 'name')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    hashtags = serializers.PrimaryKeyRelatedField(many=True, queryset=Hashtag.objects.all())
    class Meta:
        model = Note
        fields = ('id', 'name', 'hashtags', 'text', 'date')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('id', 'color', 'hashtag', 'i18n', 'importance', 'text')