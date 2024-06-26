from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from club.models import Club
from team.models import Team
from tier.models import Tier
from core.models import TimeStampedModel
from django.core.validators import MinValueValidator, MaxValueValidator

# CustomUserManager 정의 (CustomUser모델을 사용하려면 필수적으로 필요한 매니저)
class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone number must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('birth', 1900)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)



# 사용자 정의 사용자 커스텀 모델
class CustomUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    # 성별필드에 choices 구현
    GENDER_CHOICES = (
        ('male', '남성'),
        ('female', '여성'),
    )
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    birth = models.IntegerField(
        validators=[
            MinValueValidator(1900), # 필드의 값이 설정된 최소값 이상
            MaxValueValidator(2050) # 필드의 값이 설정된 최대값 이하
        ])
    username = models.CharField(max_length=255) 
    phone = models.CharField(max_length=255, unique=True)
    auth = models.CharField(max_length=255, blank=True, null=True)
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, blank=True, null=True) # 사용자가 클럽에 속하지 않아도 되며, 사용자 입력 폼에서도 클럽 필드를 비워둘 수 있음
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, blank=True, null=True) 
    tier = models.ForeignKey(Tier, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_staff = models.BooleanField(default=False) # 관리자 페이지 접속 가능하게 하는 staff 기능
    is_active = models.BooleanField(default=True) # is_active 활용하여, 계정을 비활성화 가능 (유저 삭제 대신 False)
    image_url = models.ForeignKey('image_url.ImageUrl', on_delete=models.DO_NOTHING, blank=True, null=True)
    objects = CustomUserManager()
    
    
    USERNAME_FIELD = 'phone' # USERNAME_FIELD 로 지정된 값을 흔히 말하는 로그인 ID로 사용됨.
    
    REQUIRED_FIELDS = [] # 슈퍼유저 생성시 요구되는 필드 목록 설정
    
    def __str__(self):
        return self.phone
    

    class Meta:
        db_table = 'users'