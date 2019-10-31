import requests
from django.shortcuts import render, redirect
from faker import Faker
from .models import Job

# Create your views here.
def index(request):
  jobs = Job.objects.all()
  context = {'jobs':jobs}
  return render(request, 'jobs/index.html',context)

def new(requst):
  return render(requst, 'jobs/new.html')

def past_job(request):
  name = request.POST.get('name')
  faker = Faker('ko_KR') 
  user = Job.objects.filter(name=name).first()
  
  if user:
    past_job = user.past_job

  else:
    #faker = Faker('ko-KR')
    faker = Faker()
    past_job = faker.job()
    job = Job(name=name, past_job=past_job)
    job.save()

  api_url = 'http://api.giphy.com/v1/gifs/search'
  api_key = 'EJrj23vHajiPsSLk3iovWjeusslgcm95'

  data = requests.get(f'{api_url}?api_key={api_key}&q={past_job}&limit=1&lang=ko').json()
  

  # 예외처리
  try:
    img_url = data.get('data')[0].get('images').get('original').get('url')
  except IndexError:
    img_url = None

  context = {
        'name': name,
        'past_job': past_job,
        'img_url': img_url,  
    }

  return render(request, 'jobs/result.html',context)
