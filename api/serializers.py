from rest_framework import serializers
from .models import User,Note

class SignUpSerializer(serializers.ModelSerializer):
    password2=serializers.CharField()
    class Meta:
        model=User
        fields=["email","username","password","password2"]

    def validate(self, attrs):
        pass1=attrs.get("password")
        pass2=attrs.get("password2")
        if pass1!=pass2:
            raise serializers.ValidationError({"msg":"both passwords are not same"})
        
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    


class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model=User
        fields=["email","password"]




class AddNoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # Assuming 'user' is a foreign key field in the Note model

    class Meta:
        model = Note
        fields = ["user", "title", "description", "tag"]

    def create(self, validated_data):
        user = self.context.get("user")
        validated_data['user'] = user
        # note = super().create(validated_data)
        # return note
        return Note.objects.create(**validated_data)
    

class GetNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ["id","title", "description", "tag"]
class UpdateNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ["title", "description", "tag"]
