from django.contrib.auth.models import User
from .models import remainders

out = remainders.objects.filter(User = 'user')
print(out)