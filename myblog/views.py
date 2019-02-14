from .models import Article,Photo,Leacot
# Create your views here.
from django.shortcuts import render,redirect, HttpResponse
from django.db.models import Q
# Create your views here.
def index(request,num='0'):
	if(num=='1'):
		content = {'博客':  Article.objects.filter(category='IT相关')[:10], "位置": "IT相关"}
	elif(num=='2'):
		content = {'博客': Article.objects.filter(category='好软分享')[:10], "位置": "好软分享"}
	elif (num == '3'):
		content = {'博客': Article.objects.filter(category='摄影设计')[:10], "位置": "摄影设计"}
	elif (num == '4'):
		content = {'博客': Article.objects.filter(category='旅游杂记')[:10], "位置": "旅游杂记"}
	elif (num == '0'):
		content = {'博客': Article.objects.filter(~Q(category='留言板'))[:10], "位置": "默认"}
	return render(request, "blog/index.html", content)
def details(request,blog_id):
	if request.method == 'GET':
		content = {'blog': Article.objects.get(id=blog_id),"评论":Leacot.objects.filter(blog=blog_id)}
		return render(request,"blog/details.html",content)
	elif request.method == 'POST':
		article=Article.objects.get(id=blog_id)
		a_row = Leacot(content=request.POST['desc'], blog=article)
		a_row.save()
		content = {'blog': Article.objects.get(id=blog_id),"评论":Leacot.objects.filter(blog=blog_id)}
		return render(request, "blog/details.html", content)
def about(request):
	return render(request, "blog/about.html")
def leacots(request):
	if request.method == 'GET':
		content = {'leacots': Leacot.objects.filter(blog=1)}
		return render(request, "blog/leacots.html",content)
	elif request.method == 'POST':
		a_row = Leacot(content=request.POST['留言'])
		a_row.save()
		content = {'leacots': Leacot.objects.filter(blog=1)}
		return render(request, "blog/leacots.html", content)
def photos(request):
	content = {'照片': Photo.objects.all()}
	return render(request, "blog/album.html",content)
def myindex(request):
	page=request.GET.get('page',1)
	page_count=20
	content = {'博客':  Article.objects.filter(category='IT相关')[(page-1)*page_count:page*page_count], "位置": "IT相关"}
	return HttpResponse(content)