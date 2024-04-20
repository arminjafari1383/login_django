from django.http import HttpResponse
from rest_framework.views import APIView
from ..models import Personsignup
from .serializers import PersonsignupSerializer
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser


class Login(APIView):
    queryset = Personsignup.objects.all()
    serializer_class = PersonsignupSerializer

    def check_username_unique(self, entered_username):
        if User.objects.filter(username=entered_username).exists():
            return False
        return True

    def post(self, request):
        body = request.data
        entered_username = body.get('username')
        entered_email = body.get('entered_email')

        # ابتدا بررسی کنید که آیا نام کاربری منحصر به فرد است
        if not self.check_username_unique(entered_username):
            return HttpResponse('این نام کاربری قبلاً انتخاب شده است.', status=400)

        try:
            email_user = Personsignup.objects.get(email=entered_email)
            if email_user.email == entered_email:
                email_user.delete()
                try:
                    email_user = User.objects.get(email=entered_email)
                except User.DoesNotExist:
                    # ایجاد کاربر جدید با نام کاربری و ایمیل
                    current_user = User.objects.create(username=entered_username, email=entered_email)
                    return HttpResponse('کاربر با موفقیت ایجاد شد.', status=201)
        except Personsignup.DoesNotExist:
            # ایجاد کاربر جدید با نام کاربری و ایمیل
            current_user = User.objects.create(username=entered_username, email=entered_email)
            return HttpResponse('کاربر با موفقیت ایجاد شد.', status=201)
        except IntegrityError as e:
            # اگر خطایی در مورد محدودیت‌های پایگاه داده رخ دهد
            return HttpResponse(str(e), status=400)

        return HttpResponse('عملیات با موفقیت انجام شد.', status=200)