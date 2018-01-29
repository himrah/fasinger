from django.shortcuts import render,render_to_response
from django.http.response import HttpResponseRedirect,JsonResponse,HttpResponse
from django.core.files.storage import FileSystemStorage
from app.models import *
from app.forms import *
import cv2 as cv
from django.contrib.auth import authenticate,login
#from django.contrib import auth

# Create your views here.

"""def resize(request,img):
    image=cv.imread('4hssNgw.jpg')
    image.shape[1]
    r=100.0/image.shape[1]
    dim = (100,int(image.shape[0]*r))
    resize=cv.resize(image,dim,interpolation = cv.INTER_AREA)
    cv.imwrite("res.jpg",resize)"""

def registration(request):
    form=Registrationform(request.POST or None)
    login_form=LoginForm()
    c={'form':form,'login_form':login_form}
    if request.method=='POST':
        if form.is_valid():
     #       print("valiiddd")
            form.save()
            return HttpResponse('ok')
        else:
            #print("this is else part")
            ems=str(request.POST.get('username'))
            u=request.POST.get('email')
            #print(type(ems))
            l=str(u)
            u=str(ems)
            #print(User.objects.filter(email=l))
            #print(u)
            #print(User.objects.filter(email=l))

            #print(User.objects.filter(username=u))
            #ems = cleaned_data.get('email')
            #u = self.cleaned_data.get('username')

            if User.objects.filter(username=u):
                return HttpResponse('user')
                #raise forms.ValidationError("Username Already exist")
            elif User.objects.filter(email=l):
                return HttpResponse('email')
                #raise forms.ValidationError("Email already exist")
            else:
                form.save()
                #print(form)
                return HttpResponse('new')
                #return HttpResponseRedirect('/accounts/login')
                #return HttpResponseRedirect('/login')
            #return HttpResponse('error')

    return render(request,'registration/registration.html',c)
    #return render(request,'registration/registration.html')


def ajax_comment(request,p_id):
    if request.method == 'POST':
        form = Comment_form(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.comment_by_id=request.user.id
            f.photo_id_id = p_id
            f.save()
            return HttpResponse('OK')
        else:
            return HttpResponse('Not')




def home(request):
    comment_form = Comment_form(request.POST)
    comment = Comments.objects.all()
    photos = Photos.objects.all().order_by('-created_date')            
    
    data={
        'photos':photos,
        'cmt':comment_form,
        'comments':comment,
    }
    return render(request,'home.html',data)

def Gallery(request):
    #photo=Photos.objects.all()
    photo=Photos.objects.all().order_by('-created_date')
    photo_list=[]
    counter = 0
    while counter<len(photo):
        photo_list.append([p for p in photo[counter:counter+3]])
        counter+=3
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            f=form.save()
            #form.save(commit=False)
            f.upload_by_id=request.user.id
            f.save()
            return HttpResponseRedirect('/')
        else:
            HttpResponse("unvalid")
    else:
        form = PhotoForm()
        c={'form':form,'photos':photo_list}
        return render(request,'input.html',c)

"""def Input(request):
    if request.method=='POST':
        form=ImageInputForm(request.POST,request.FILES)
        if form.is_valid():            
            form.save()
            
            img = request.POST.get('photo', '')
            #img = request.FILES['photo']
            image=cv.imread(img)
            image.shape[1]
            r=100.0/image.shape[1]
            dim = (100,int(image.shape[0]*r))
            resize=cv.resize(image,dim,interpolation = cv.INTER_AREA)
            cv.imwrite('media/photos')
            #img = request.POST.get('username', '')
            #return HttpResponse(img)
            return HttpResponseRedirect('/')
        return HttpResponse('Not Valid')    
    else:
        form=ImageInputForm()
        c={'form':form}
        return render(request,'input.html',c)"""

def Input(request):
    #r=Photos.objects.all().order_by('created_date').reverse()
    r=Photos.objects.all().order_by('-created_date')
    
    return render_to_response('post.html',{'photo':r,'user':request.user})        

def Login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form=LoginForm()
        c={'form':form}
        #c.update(csrf(request))
        return render(request,'registration/login.html',c)

def auth(request):
    if request.method=='POST':
        response_data={}
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = authenticate(username=username, password=password)
        u=User.objects.filter(username=username)
        if not u:
            return HttpResponse('username not found')
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        elif request.user.is_authenticated():
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('not found')