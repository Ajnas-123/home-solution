from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect,JsonResponse
from homesolutionapp.models import *
import hashlib
import random
import string
from django.conf import settings
from django.core.mail import send_mail
from reportlab.pdfgen import canvas
from django.views.generic import View
from homesolution.utils import render_to_pdf
from django.views.decorators.cache import cache_control
@cache_control(no_cache=True,must_revalidate=True,no_store=True)



# Create your views here.
def img(request):
	if request.method=='POST':
		image=request.FILES['img']
		query=gallery_tb(image=image)
		query.save()
		return render(request,'index.html')
	else:
		i=gallery_tb.objects.all()
		return render(request,'img.html',{'i':i})



def imgview(request):
	i=gallery_tb.objects.all()
	return render(request,'img.html',{'i':i})










def display(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def error(request):
	return render(request,'error.html')

def gallery(request):
	return render(request,'gallery.html')

def services(request):
	return render(request,'services.html')

def typography(request):
	return render(request,'typography.html')

def user_register(request):
	if request.method=='POST':
		uname=request.POST['Username']
		upass=request.POST['Password']
		uemail=request.POST['Email']
		uphone=request.POST['Phone']
		uplace=request.POST['Place']
		uaddress=request.POST['Address']
		hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()

		check=user_tb.objects.all().filter(email=uemail)
		if check:
			workers=worker_tb.objects.all()

			return render(request,'index.html',{'msg':'already exist'})
		else:
			x = ''.join(random.choices(uname + string.digits, k=8))
			y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
			subject = 'welcome to Leaders IT Solution'
			message = f'Hi {uname}, thank you for registering in leaders it solution. your user username: {uname} and  password: {upass}.'
			email_from = settings.EMAIL_HOST_USER 
			recipient_list = [uemail, ] 
			send_mail( subject, message, email_from, recipient_list ) 


			query=user_tb(username=uname,password=hashpass,email=uemail,phone=uphone,place=uplace,address=uaddress)
			query.save()
			workers=worker_tb.objects.all()

			return render(request,'index.html')
	else:
		workers=worker_tb.objects.all()

		return render(request,'index.html',{'workers':workers})


def user_login(request):
	if request.method=='POST':
		uname=request.POST['Username']
		upass=request.POST['Password']
		hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()

		query=user_tb.objects.filter(username=uname,password=hashpass)
		if query:
			for x in query:
				request.session['userid']=x.id
				request.session['username']=x.username

				uid=request.session['userid']
				workers=worker_tb.objects.all()

			return render(request,'index.html',{'success':"Login Succesful",'workers':workers})
		else:
			workers=worker_tb.objects.all()

			return render(request,'index.html',{'error':"Incorrect username/password",'workers':workers})	
	else:
			workers=worker_tb.objects.all()

			return render(request,'index.html',{'workers':workers})	



def user_logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
		del request.session['username']

	return render(request,"index.html")






def worker_register(request):
	if request.method=='POST':
		uname=request.POST['Username']
		upass=request.POST['Password']
		hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()

		uemail=request.POST['Email']
		uphone=request.POST['Phone']
		uplace=request.POST['Place']
		uaddress=request.POST['Address']
		check=worker_tb.objects.all().filter(email=uemail)
		if check:
			return render(request,'index.html',{'msg':'already exist'})
		else:
			query=worker_tb(username=uname,password=hashpass,email=uemail,phone=uphone,place=uplace,address=uaddress)
			query.save()
			workers=worker_tb.objects.all()

			return render(request,'index.html',{'workers':workers})
	else:
		workers=worker_tb.objects.all()

		return render(request,'index.html',{'workers':workers})


def worker_login(request):
	if request.method=='POST':
		uname=request.POST['Username']
		upass=request.POST['Password']
		hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()

		query=worker_tb.objects.filter(username=uname,password=hashpass)
		if query:
			for x in query:
				request.session['workerid']=x.id
				request.session['workername']=x.username

				wid=request.session['workerid']
				workers=worker_tb.objects.all()

			return render(request,"index.html",{'success':"Login Succesful"})
		else:
			workers=worker_tb.objects.all()

			return render(request,'index.html',{'error':"Incorrect username/password",'workers':workers})	
	else:
			workers=worker_tb.objects.all()

			return render(request,'index.html')	


def worker_logout(request):
	if request.session.has_key('workerid'):
		del request.session['workerid']
		del request.session['workername']

	return render(request,"index.html")



def complaint_register(request):
	if request.session.has_key('userid'):

		if request.method=='POST':
			print("POST")
			ui=request.session['userid']
			uid=user_tb.objects.get(id=ui)


			wi=request.POST['worker']
			print(wi)
			woid=worker_tb.objects.get(id=wi)
			complainttext=request.POST['complaint']
			date=request.POST['date']
			# check=complaint_tb.objects.filter(workerid=woid)
			complsave=complaint_tb(date=date,userid=uid,workerid=woid,complaint=complainttext)
			complsave.save()
			workers=worker_tb.objects.all()
			return render(request,'index.html',{'workers':workers})
		else:

			workers=worker_tb.objects.all()

			return render(request,'index.html',{'workers':workers})

	else:
		return render(request,'index.html')





def admin_login(request):
	if request.method=='POST':
		uname=request.POST['username']
		upass=request.POST['password']

		query=admin_tb.objects.filter(username=uname,password=upass)
		if query:
			for x in query:
				request.session['adminid']=x.id
				request.session['adminname']=x.username

				wid=request.session['adminid']
				query=user_tb.objects.all()
				query1=worker_tb.objects.all()
				query2=complaint_tb.objects.all()

			return HttpResponseRedirect("/admin_view/",{'success':"Login Succesful",'queryset':query,'queryset1':query1,'queryset2':query2,'user':query})
		else:

			

			return render(request,'login2.html',{'error':"Incorrect username/password"})	
	else:

			

			return render(request,'login2.html')


def admin_page(request):
	if request.session.has_key('adminid'):
		query=user_tb.objects.all()
		query1=worker_tb.objects.all()
		query2=complaint_tb.objects.all()
		return render(request,"admin.html",{'queryset':query,'queryset1':query1,'queryset2':query2,'user':query})
	else:
		return render(request,'login2.html')




def admin_logout(request):
	if request.session.has_key('adminid'):
		del request.session['adminid']
		del request.session['adminname']

	return render(request,"index.html")








def show_details(request):
	print("hello")
	a=request.GET.get('p')
	b=user_tb.objects.all().filter(id=a)
	for x in b:
		p=x.username	
		q=x.email	
		r=x.phone	
		s=x.place	
		t=x.address	
	dat={"aa":p,"bb":q,"cc":r,"dd":s,"ee":t}
	return JsonResponse(dat)



def download(request):
	if request.session.has_key('adminid'):
		# myid=request.GET['userid']
		ut=user_tb.objects.all()
		pdf=render_to_pdf('pdfdownload.html',{'ut':ut})
		return HttpResponse(pdf,content_type='application/pdf')
	else:
		return render(request,'admin_login')



























		



