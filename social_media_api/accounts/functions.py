from accounts.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
def create_token(username):
	user = User.objects.get(username=username)
	token = Token.objects.create(user=user)

	return token.key

def get_token(username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return {"error": "User Does Not Exist!"}
	try: 
		token = Token.objects.get(user=user)
	except Token.DoesNotExist:
		token = Token.objects.create(user=user)

	return {"token": token.key}
