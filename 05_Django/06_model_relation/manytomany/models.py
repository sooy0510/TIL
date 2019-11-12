from django.db import models

# Create your models here.
class Doctor(models.Model):
  name = models.TextField()

  def __str__(self):
      return f'{self.pk}번 의사 {self.name}'


# class Patient(models.Model):
#   name = models.TextField()
#   #doctors = models.ManyToManyField(Doctor, through='Reservation',
#   # 역참조
#   doctors = models.ManyToManyField(Doctor,
#   # related_name 설정해주면 중개모델 안만들어도 db에 테이블 자동 생성
#   # 특이사항 등 추가할 사항이나 상황에 맞춰서 중개 모델 만들지 결정
#   related_name='patients')
#   # add와 remove활용할 수 있게 되멤ㅅ
#   #doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  
#   def __str__(self):
#       return f'{self.pk}번 환자 {self.name}'


class Patient(models.Model):
  name = models.TextField()
  doctors = models.ManyToManyField(Doctor, related_name='patients')
  
  def __str__(self):
      return f'{self.pk}번 환자 {self.name}'
  

# # 중개모델
# class Reservation(models.Model):
#   doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#   patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#   def __str__(self):
#       return f'{self.doctor.id}번 의사의 {self.patient.id}번 환자'
  