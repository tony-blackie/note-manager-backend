from rest_framework import viewsets
from rest_framework.views import APIView
from dinosaurs.serializers import PersonSerializer, HashtagSerializer, NoteSerializer, GroupSerializer, QuestionnaireSerializer
from dinosaurs.models import Note, Person, Questionnaire, Hashtag
from django.contrib.auth.models import Group
import pdb
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
import json
from rest_framework import exceptions
import re
from rest_framework.response import Response
from django.http import JsonResponse
import os

def remove_slashes(string):
    return string.replace('/', '')

def pushParentIdIntoDeleteList(folderId, arrayToPushIds, allFolders):
    if folderId not in arrayToPushIds:
        arrayToPushIds.append(folderId)
    for item in allFolders:
        if item.parent == folderId:
            pushParentIdIntoDeleteList(item.id, arrayToPushIds, allFolders)


class PersonAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    queryset = Person.objects.all()

    def get(self, request):
        print('get request')

    def put(self, request):
        print('put request')

    def delete(self, request):
        print('delete request')

    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        is_staff = request.data['is_staff']

        user = Person.objects.create_user(
            username = username,
            password = password,
            email = email,
            is_staff = is_staff
        )
        user.save()

        serializer = PersonSerializer(instance=user)

        return HttpResponse(json.dumps(serializer.data))

# class FolderAPIView(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = FolderSerializer
#     queryset = Folder.objects.all()

#     def get(self, request, id = None):
#         if id == '':
#             if re.search(r'admin/dinosaurs/folder/$', request.path):
#                 folders = Folder.objects.all()
#                 serializer = FolderSerializer(folders, many=True)
#                 return Response(serializer.data)

#             if re.search(r'/folder/', request.path):
#                 userId = request.user.id

#                 if request.user.id == None:
#                     status = 400
#                     message = 'Login is required'
#                     return JsonResponse({'message': message}, status=status)

#                 folders = Folder.objects.filter(author=userId)
#                 if not folders:
#                     Folder.objects.create(
#                         name = 'initial',
#                         parent = 0,
#                         is_root = True,
#                         author = request.user
#                     )

#                 serializer = FolderSerializer(Folder.objects.filter(author = request.user.id), many=True)

#                 return Response(serializer.data)

#             # if re.search(r'/folder/', request.path):
#             #     userId = request.user.id

#             #     try:
#             #         folders = Folder.objects.filter(author=userId)
#             #     except Folder.DoesNotExist:
#             #         return Response([])

#             #     serializer = FolderSerializer(Folder.objects.filter(author = request.user.id), many=True)

#             #     return Response(serializer.data)
#         else:
#             id = int(remove_slashes(id))
#             userId = request.user.id
#             serializer = FolderSerializer(Folder.objects.get(author = request.user.id, id = id))
#             return Response(serializer.data)

#     def post(self, request, id = None):
#         userId = request.user.id

#         if request.data['parent'] != None:
#             parentFolder = Folder.objects.get(id=request.data['parent'])
#         else:
#             foldersForCurrentUser = Folder.objects.filter(author=userId)
#             for folder in foldersForCurrentUser:
#                 if folder.is_root == True:
#                     parentFolder = folder

#         Folder.objects.create(
#             name = request.data.get('name', 'newName'),
#             parent = parentFolder.id,
#             is_root = request.data.get('is_root', False),
#             author = request.user
#         )

#         serializer = FolderSerializer(Folder.objects.filter(author = request.user.id), many=True)
#         return Response(serializer.data)

#     def put(self, request, id = None):
#         userId = request.user.id
#         folderId = int(remove_slashes(id))
#         folder = Folder.objects.get(id = folderId, author = userId)

#         folder.name = request.data.get('name')
#         folder.save()

#         serializer = FolderSerializer(folder)
#         return Response(serializer.data)

#     def delete(self, request, id = None):
#         userId = request.user.id
#         folderId = int(remove_slashes(id))
#         allFolders = Folder.objects.filter(author = userId)

#         childFolderIdsToRemove = []

#         pushParentIdIntoDeleteList(folderId, childFolderIdsToRemove, allFolders)

#         for folderIdToRemove in childFolderIdsToRemove:
#             folder = Folder.objects.get(id=folderIdToRemove)
#             noteIds = folder.notes

#             if folder.is_root == True:
#                 return Response([])

#             for note in noteIds.all():
#                 dbNote = Note.objects.get(id=note.id)
#                 dbNote.delete()
#             folder.delete()

#         return Response([])

class HashtagAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()

    def get(self, request, id = None):
        if id == '':
            if re.search(r'admin/dinosaurs/hashtag/$', request.path):
                hashtags = Hashtag.objects.all()
                serializer = HashtagSerializer(hashtags, many=True)
                return Response(serializer.data)

            if re.search(r'/hashtag/', request.path):
                userId = request.user.id

                if request.user.id == None:
                    status = 400
                    message = 'Login is required'
                    return JsonResponse({'message': message}, status=status)

                hashtags = Hashtag.objects.filter(author=userId)
                # if not hashtags:
                #     Hashtag.objects.create(
                #         name = 'initial',
                #         author = request.user
                #     )

                serializer = HashtagSerializer(Hashtag.objects.filter(author = request.user.id), many=True)

                return Response(serializer.data)
        else:
            id = int(remove_slashes(id))
            userId = request.user.id
            serializer = HashtagSerializer(Hashtag.objects.get(author = request.user.id, id = id))
            return Response(serializer.data)

    def post(self, request, id = None):
        userId = request.user.id

        Hashtag.objects.create(
            name = request.data.get('name', 'newName'),
            author = request.user
        )

        serializer = HashtagSerializer(Hashtag.objects.filter(author = request.user.id), many=True)
        return Response(serializer.data)

    def put(self, request, id = None):
        userId = request.user.id
        hashtagId = int(remove_slashes(id))
        hashtag = Hashtag.objects.get(id = hashtagId, author = userId)

        hashtag.name = request.data.get('name')
        hashtag.save()

        serializer = HashtagSerializer(hashtag)
        return Response(serializer.data)

    def delete(self, request, id = None):
        userId = request.user.id
        hashtagId = int(remove_slashes(id))
        allHashtags = Hashtag.objects.filter(author = userId)

        hashtag = Hashtag.objects.get(id=hashtagId)

        hashtag.delete()

        return Response([])

class NoteAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    queryset = Note.objects.all()

    def get(self, request, id = None):
        def remove_slashes(string):
            return string.replace('/', '')

        if id == '':
            if re.search(r'admin/dinosaurs/note/$', request.path):
                notes = Note.objects.all()
                serializer = NoteSerializer(notes, context={'request': request}, many=True)
                return Response(serializer.data)

            if re.search(r'/note/$', request.path):
                userId = request.user.id

                if request.user.id == None:
                    status = 400
                    message = 'Login is required'
                    return JsonResponse({'message': message}, status=status)


                try:
                    notes = Note.objects.filter(author=userId)
                except Note.DoesNotExist:
                    return Response([])

                serializer = NoteSerializer(Note.objects.filter(author = request.user.id), context={'request': request}, many=True)

                return Response(serializer.data)

            if re.search(r'/note/', request.path):
                userId = request.user.id

                try:
                    notes = Note.objects.filter(author=userId)
                except Note.DoesNotExist:
                    return Response([])

                serializer = NoteSerializer(Note.objects.filter(author = request.user.id), context={'request': request}, many=True)

                return Response(serializer.data)
        else:
            id = int(remove_slashes(id))
            userId = request.user.id
            serializer = NoteSerializer(Note.objects.get(author = request.user.id, id = id))
            return Response(serializer.data)

    def post(self, request, id = None):
        userId = request.user.id

        note = Note.objects.create(
            name = request.data.get('name', 'newName'),
            text = request.data.get('text', 'defaultText'),
            author = request.user
        )

        selectedHashtags = request.data.get('hashtagsToAdd', None)
        allHashtags = request.data.get('allHashtags', None)

        if allHashtags:
            for hashtag in allHashtags:
                id = hashtag.get('id', None)

                if id == None:
                    note.hashtags.create(name=hashtag['name'], author=request.user)

        for hashtag in selectedHashtags:
            selectedHashtag = Hashtag.objects.get(
                name = hashtag['name'],
                author = request.user
            )
            note.hashtags.add(selectedHashtag)

        serializer = NoteSerializer(note, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id = None):
        noteId = int(remove_slashes(id))
        userId = request.user.id

        note = Note.objects.get(id = noteId)

        name = request.data.get('name', None)
        if name:
            note.name = name

        text = request.data.get('text', None)
        if text:
            note.text = text

        selectedHashtags = request.data.get('hashtagsToAdd', None)
        allHashtags = request.data.get('allHashtags', None)

        if allHashtags:
            for hashtag in allHashtags:
                isNew = hashtag.get('id', None)
                if isNew == None:
                    note.hashtags.create(name=hashtag['name'], author=request.user)

        hashtagsExistingOnNote = Hashtag.objects.filter(note__id=noteId)

        for existingHashtag in hashtagsExistingOnNote:
            wasDeleted = True
            for newHashtag in selectedHashtags:
                if existingHashtag.name == newHashtag['name']:
                    wasDeleted = False
            if wasDeleted:
                note.hashtags.remove(existingHashtag)

        for newHashtag in selectedHashtags:
            isNew = True
            for existingHashtag in hashtagsExistingOnNote:
                if existingHashtag.name == newHashtag['name']:
                    isNew = False
            if isNew:
                newHashtagObj = Hashtag.objects.get(id=newHashtag['id'])
                note.hashtags.add(newHashtagObj)

        note.save()

        serializer = NoteSerializer(note, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, id=None):
        noteId = int(remove_slashes(id))
        note = Note.objects.get(id=noteId)

        note.delete()

        serializer = NoteSerializer(note, context={'request': request})
        return Response(serializer.data)

class QuestionnaireViewAPI(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()

    def get(self, request, id=None):
        if id == '':
            if re.search(r'admin/dinosaurs/questionnaire/$', request.path):
                questionnaires = Questionnaire.objects.all()
                serializer = QuestionnaireSerializer(folders, many=True)
                return Response(serializer.data)

            if re.search(r'/questionnaire/$', request.path):
                userId = request.user.id

                if request.user.id == None:
                    status = 400
                    message = 'Login is required'
                    return JsonResponse({'message': message}, status=status)

                questionnaires = Questionnaire.objects.filter(author=request.user)

                serializer = QuestionnaireSerializer(Questionnaire.objects.filter(author = request.user), many=True)

                return Response(serializer.data)

            if re.search(r'/questionnaire/', request.path):
                userId = request.user.id

                try:
                    questionnaires = Questionnaire.objects.filter(author=userId)
                except Questionnaire.DoesNotExist:
                    return Response([])

                serializer = QuestionnaireSerializer(Questionnaire.objects.filter(author = request.user), many=True)

                return Response(serializer.data)
        else:
            id = int(remove_slashes(id))
            userId = request.user.id
            serializer = QuestionnaireSerializer(Questionnaire.objects.get(author = request.user, id = id))
            return Response(serializer.data)

    def post(self, request, id = None):
        userId = request.user.id

        questionnaire = Questionnaire.objects.create(
            color = request.data.get('color', False),
            hashtag = request.data.get('hashtag', False),
            i18n = request.data.get('i18n', False),
            importance = request.data.get('importance', False),
            text = request.data.get('text', ''),
            author = request.user
        )

        serializer = QuestionnaireSerializer(questionnaire)
        return Response(serializer.data)

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

from django.views.generic import View
# from django.http import HttpResponse
# from django.conf import settings
