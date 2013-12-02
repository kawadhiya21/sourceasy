from django.contrib.auth.models import User

def create_user(email, password):
    user = User.objects.create(username=email , email=email)
    user.set_password(password)
    user.save()
    return user
