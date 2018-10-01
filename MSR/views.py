# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Max
from django.shortcuts import render
from MSR.models import videoMetaData
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def login_user(request):
    if request.POST:
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
	user2 = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/MSR/home/')
    return render(request, 'MSR/login.html')


@login_required(login_url='/MSR/login')
def index(request):    
	# user = authenticate(username='john', password='secret')
    # if request.POST['uname'] == 'raja' and request.POST['psw'] == 'cvitmsr22':
    return render(request, 'MSR/home.html')
    # else:
    # 	return render(request, 'MSR/login.html')


# def login(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     return render(request, 'MSR/login.html')

def searchVideo(request):
	print("search ", request.GET['vidName'])
	result = list(videoMetaData.objects.filter(title=request.GET['vidName']).values())[0]

	args = {'comments' : result['comments'], 'title' : result['title']}
	return render(request, 'MSR/videoList.html', args)
@login_required(login_url='/MSR/login')
def saveComments(request):
	vid = videoMetaData.objects.get(title=request.GET['title'])
	vid.comments = request.GET['comments']
	vid.save()
	return HttpResponse('Successfully Saved')
@login_required(login_url='/MSR/login')
def addVideos(request):
	vid = videoMetaData(title=request.GET['vidNo'])
	vid.save()
	return HttpResponse('Successfully Saved')
@login_required(login_url='/MSR/login')
def m1Done(request):
	print("m1done")
	vid = videoMetaData.objects.get(title=request.GET['vidNo'])
	vid.method1 = 1
	vid.save()
	return HttpResponse('Successfully Saved')

def rawVideos(request):
	vid = videoMetaData.objects.all().aggregate(Max('title'))
	totalVid = int(vid['title__max'])
	pageno = int(request.GET['page'])
	frm = (pageno - 1) * 18 + 1
	upto = frm + 18
	if upto > totalVid:
		upto = totalVid
	vid_list = list(range(frm, upto+1))
	pages = totalVid / 18
	if totalVid % 18 != 0:
		pages += 1

	# print(frm, upto, vid_list, pages, totalVid)
	if request.GET['vidCat'] == 'Raw':
		return render(request, 'MSR/rawVideos.html', {'vid': vid_list, 
			'brk': range(6, totalVid+1, 6), 'pages': range(1, int(pages)+1, 1)})
	else:
		# return render(request, 'MSR/existingRes.html', {'vid':list(range(1, vid['title__max']+1)), 
		# 	'brk': range(6, vid['title__max']+1, 6)})
		return render(request, 'MSR/existingRes.html', {'vid': vid_list, 
			'brk': range(6, totalVid+1, 6), 'pages': range(1, int(pages)+1, 1)})
	# list(range(1, vid['title__max']+1))

def m1Videos(request):
	vid = videoMetaData.objects.filter(method1=1)
	totalVid = vid.count()
	pageno = int(request.GET['page'])
	frm = (pageno - 1) * 18 + 1
	upto = frm + 18
	if upto > totalVid:
		upto = totalVid
	vid_list = []
	for i in range(frm, upto+1):
		vid_list.append(vid[i-1].title)
	pages = totalVid / 18
	if totalVid % 18 != 0:
		pages += 1
	print(frm, upto)	
	print(vid_list)
	return render(request, 'MSR/method1.html', {'vid': vid_list, 
		'brk': range(6, totalVid+1, 6), 'pages': range(1, int(pages)+1, 1)})
