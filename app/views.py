from django.shortcuts import render,render_to_response
from django.http.response import HttpResponseRedirect,JsonResponse,HttpResponse
from django.core.files.storage import FileSystemStorage
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required
#import cv2 as cv
from django.contrib.auth import authenticate,login,logout
from social_django.models import UserSocialAuth
from django.utils.formats import localize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import json
from serializer import *
from rest_framework import viewsets
from rest_framework.views import APIView
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
            js={
            'comment':f.comment,
            'date':localize(f.comment_time),
            #'date':str(f.comment_time.date())+' '+str(f.comment_time.time()),
            'uname':f.comment_by.username,
            }

            #comment = request.POST.get('comment', '')
            return JsonResponse(js)
        else:
            return HttpResponse('not')


def profile(request,pk):


    u=User.objects.filter(username=pk)
    if u:
        #return render_to_response('registration/profile.html',{'user':u[0]})
        pform = ProfilePicForm()
        form = ProfileForm()
        c={'profile':form,'profile_pic':pform,'user':u[0]}
        return render(request,'registration/profile.html',c)

    else:
        #pform = ProfilePicForm()
        #form = ProfileForm()
        #c={'profile':form,'profile_pic':pform,'user':u}    
        return render_to_response('registration/profile.html',{'user':u})




@login_required(login_url='/accounts/login')
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


"""@login_required(login_url='/accounts/login')
def home(request):
    
    comment_form = Comment_form(request.POST)
    comment = Comments.objects.all()
    photos = Photos.objects.all().order_by('-created_date')            
    
    page = request.GET.get('page', 1)
    paginator = Paginator(photos, 3)

    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    
    data={
        #'photos':photos,
        'cmt':comment_form,
        'comments':comment,
        'photos':numbers        
    }

    return render(request, 'home.html', data)"""


#    return render(request,'home.html',data)

@login_required(login_url='/accounts/login')

def UpdateProfilePic(request):
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.profile_id = request.user.profile.id
            f.save()
            return HttpResponseRedirect('/updateprofile')
        else:
            HttpResponse('form not valid')
    else:
        pform = ProfilePicForm()
        form = ProfileForm()
        c={'profile':form,'profile_pic':pform}
        return render(request,'registration/profile.html',c)

from rest_framework.response import Response
from rest_framework import status

class PhotoSS(APIView):
    def get(self,request,format=None):
        photo = Photos.objects.all()
        serializer_context = {
            'request': request,
        }

        serializer = PhotoSerializer(photo, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class PhotoSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotoSerializer

class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def get_comment(request,p_id):
    c = Comments.objects.filter(photo_id_id=p_id)
    #page = request.GET.get('page', 1)
    #paginator = Paginator(c, 10)
    d = serializers.serialize('json',c)

    js = {
        'data':json.loads(d),
    }
    return JsonResponse(js)


@login_required(login_url='/accounts/login')
def UpdateProfile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.user_id = request.user.id
            f.save()
            return HttpResponseRedirect('/updateprofile/')
        else:
            return HttpResponse("unvalid")
    else:
        form = ProfileForm()
        pform = ProfilePicForm(request.POST, request.FILES)
        c={'profile':form,'profile_pic':pform}
        return render(request,'registration/profile.html',c)





@login_required(login_url='/accounts/login')
def Gallery(request):
    photo=Photos.objects.all().order_by('-created_date')
    photo_list=[]
    counter = 0
    while counter<len(photo):
        photo_list.append([p for p in photo[counter:counter+3]])
        counter+=3
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
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

@login_required(login_url='/accounts/login')
def Input(request):
    #r=Photos.objects.all().order_by('created_date').reverse()
    r=Photos.objects.all().order_by('-created_date')
    
    return render_to_response('post.html',{'photo':r,'user':request})        

def Login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        form=LoginForm()
        c={'form':form}
        #c.update(csrf(request))
        return render(request,'registration/login.html',c)

def Logout(request):
    logout(request)
    return render_to_response('registration/logout.html')


def auth(request):
    if request.method=='POST':
        response_data={}
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = authenticate(username=username, password=password)
        u=User.objects.filter(username=username)
        if not u:
            return HttpResponse('user')
        if user is not None:
            login(request,user)
            return HttpResponse('ok')
            #return HttpResponseRedirect('/')
        elif request.user.is_authenticated():
            #return HttpResponseRedirect('/')
            return HttpResponse('ok')
        else:
            return HttpResponse('password')


def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })