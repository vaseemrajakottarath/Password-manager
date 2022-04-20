from pyexpat import model
from rest_framework import fields,serializers
from . models import Account

# from .models import UserAccount

# class UserRegister(serializers.ModelSerializer):
#     class Meta:
#         model=UserAccount
#         fields=['id','name','phone_number','email','password']

class UserRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Account
        fields = ['id','name','phone_number','email','date_of_birth','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        print(password)
        return instance

    def save(self):
        reg = Account(
            email=self.validated_data['email'],
            phone_number=self.validated_data['phone_number'],
            date_of_birth=self.validated_data['date_of_birth'],
            name=self.validated_data['name'],
        
        )
        if Account.objects.filter(phone_number=self.validated_data['phone_number']).exists():
            raise serializers.ValidationError({'error':'phone number already registered!!'})
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error':'password does not match!!'})
        reg.set_password(password)
        reg.save()
        print(password)
        return reg

class ChangePasswordSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True,required=True)
    password2 =serializers.CharField(write_only=True,required=True)
    old_password = serializers.CharField(write_only=True,required=True)
    class Meta:
        model=Account
        fields=('old_password','password','password2')
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password not match"})
        return attrs
    def validate_old_password(self,value):
        user=self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password":"old password is incorrect"})
        return value
    def update(self,instance,validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance