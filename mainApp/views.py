from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Referral
from rest_framework.authtoken.models import Token
from django.db.models import Q
from rest_framework import status

@api_view(['POST'])
def register_user(request):
    try:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        referral_code = request.data.get('referral_code')

        # Check if a user with the provided email already exists
        email = CustomUser.objects.filter(email=email).first()
        username = CustomUser.objects.filter(username=name).first()

        if email:
            return Response({'message': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if username:
            return Response({'message': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user instance with the provided name as the username
        user = CustomUser.objects.create_user(username=name, email=email, password=password)

        # Assign referral code if provided
        if referral_code:
            user.referral_code = referral_code
            user.save()

            # assign points to referring user
            referring_user = CustomUser.objects.filter(Q(referral_code=user.username) | Q(referral_code=user.code)).first()
            if referring_user:
                referring_user.points += 1
                referring_user.save()
                print(referring_user.points,"Points")

        token, token_created = Token.objects.get_or_create(user=user)

        return Response({'user_id': user.id, 'message': 'User registered successfully', 'token': token.key})
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_details(request):
    try:
        user = request.user
        return Response({
            'name': user.username,
            'email': user.email,
            'referral_code': user.referral_code,
            'timestamp': user.timestamp
        })
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_referrals(request):
    try:
        user = request.user
        referrals = CustomUser.objects.filter(Q(referral_code=user.username) | Q(referral_code=user.code))
        # referrals = CustomUser.objects.filter(referral_code=user.username)
        referral_data = [{'name': referral.username, 'email': referral.email, 'timestamp': referral.timestamp} for referral in referrals]
        return Response(referral_data)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
