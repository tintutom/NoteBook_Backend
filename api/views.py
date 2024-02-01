from rest_framework.decorators import api_view
from .serializers import SignUpSerializer, LoginSerializer, AddNoteSerializer,GetNoteSerializer,UpdateNoteSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Note



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(["POST"])
def signup(req):
    serializer = SignUpSerializer(data=req.data)
    if serializer.is_valid(raise_exception=True):
        user=serializer.save()
        token = get_tokens_for_user(user)
        return Response({"msg": "Account Created Succesfully", "token": token,"success":True}, status=status.HTTP_201_CREATED)
    else:
        return Response({"msg": "error in signup","success":False}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def login(req):
    serializer = LoginSerializer(data=req.data)
    if serializer.is_valid(raise_exception=True):
        email = req.data.get("email")
        password = req.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({"msg": "Login Succesfully", "token": token,"success":True}, status=status.HTTP_201_CREATED)
        else:
            return Response({"msg": "Wrong User","success":False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def addnote(req):
    serializer = AddNoteSerializer(data=req.data, context={'user': req.user})

    print(req.user)
    print(req.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"msg": "Note Created Succesfully"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"msg": "Note not created"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def getnote(req):
    notes = Note.objects.filter(user=req.user)   
    serializer = GetNoteSerializer(notes, many=True)
    return Response({"msg": "YOUR NOTES","data":serializer.data}, status=status.HTTP_202_ACCEPTED)
@api_view(["DELETE"])
def deletenote(req,id):
    note = Note.objects.get(pk=id)
    note.delete()  
    return Response({"msg": "YOUR NOTE DELETED"}, status=status.HTTP_202_ACCEPTED)
@api_view(["PUT"])
def updatenote(req,id):
    note = Note.objects.get(pk=id)
    serializer=UpdateNoteSerializer(data=req.data,instance=note)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg": "YOUR NOTE Updated"}, status=status.HTTP_202_ACCEPTED)
    return Response({"msg": "YOUR NOTE NOT Updated"}, status=status.HTTP_400_BAD_REQUEST)
    
    
