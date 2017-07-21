#coding = utf-8
from django.shortcuts import render,redirect,HttpResponse
from app.models import Item,Blog,Comment,Day
import time
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User 
from django.http import Http404
from .forms import CommentForm
#from haystack.forms import SearchForm
from django.views import generic
from .models import PhotoItem, Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
#登录系统
def home_page(request):
    if request.method == 'POST':
        username=request.POST['user'] 
        password=request.POST['mima']  
        user = authenticate(username=username,password=password)
        if user and user.is_active:  
            login(request, user) 
            request.session['username'] = username
            return redirect('list/')
        else:
            return redirect('/')
    return render(request,'home.html')

#主页
def list_page(request):
    username = request.session.get('username')
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'],times = time.strftime("%Y-%m-%d %X", time.localtime()))
    items = Item.objects.all()
    return render(request,'list.html',{'items':items,'username':username})


def logout_view(request):
    logout(request)
    return store_view(request)
def gy_page(request):
	return render(request,'gy.html')


#相册系统
class IndexView(generic.ListView):
    template_name = 'items/index.html'
    def get_queryset(self):
        return PhotoItem.objects.all()[:5]
        
class ListView(generic.ListView):
    model = PhotoItem
    template_name = 'items/items_list.html'
        
class ItemDetailView(generic.DetailView):
    model = PhotoItem    
    template_name = 'items/items_detail.html'
class PhotoDetailView(generic.DetailView):
    model = Photo
    template_name = 'items/photos_detail.html'


#日志系统
def day_page(request):
    days = Day.objects.all().order_by('-created')
    return render(request,'day.html',{'days': days})
def new_day(request):
    try:
    	if request.method == 'POST':
            title = request.POST['title']
            author = request.POST['author']
            content = request.POST['content']
            errors = []
            if len(title) < 1:  
                errors.append("标题不能为空")  
                return render(request,'newday.html',{'errors':errors}) 
            if len(author) < 1:
                errors.append("作者不能为空")
                return render(request,'newday.html',{'errors':errors})  
            if len(content) < 1:
                errors.append("内容不能为空")
                return render(request,'newday.html',{'errors':errors})
            Day.objects.create(title = request.POST['title'],author = request.POST['author'],content = request.POST['content'])
            return redirect("http://127.0.0.1:8000/list/day/")
    except Exception as e:
    	errors.append(str(e))
    	return render(request,'newday.html',{'errors':errors}) 
    return render(request,'newday.html')
def day_detail(request, Day_id):
    try:
        day = Day.objects.get(id=Day_id)
    except day.DoesNotExist:
        raise Http404
    return render(request, 'day-detail.html', {'day':day})


#动态
def dt_page(request):
	return render(request,'dt.html')

#更多
def gd_page(request):
	return render(request,'gd.html')


#个人信息系统
def xx_page(request):
    usernameas = request.session.get('username')
    if request.method == 'POST':
            username=request.POST['name']  
            password1=request.POST['password1'] 
            password2=request.POST['password2'] 
            email=request.POST['email'] 
            phone=request.POST['phone'] 
            user = User.objects.get(username = usernameas)
            if user.password == password1:
                user.username = username
                user.password = password2
                user.email = email
                user.phone = phone
                user.save()
                request.session['username'] = username
                return redirect('http://127.0.0.1:8000/list')
    return render(request,'xx.html')


#注册系统
def userRegister(request):  
    try:  
        if request.method=='POST':  
            username=request.POST['name']  
            password1=request.POST['password1'] 
            password2=request.POST['password2'] 
            email=request.POST['email'] 
            phone=request.POST['phone'] 
            errors=[]
            filterResult=User.objects.filter(username=username)
            if len(filterResult)>0:  
                errors.append("用户名已存在")  
                return render(request,'zhuce.html',{'errors':errors}) 
            if len(password1) < 6:
                errors.append("请输入大于6位数密码")
                return render(request,'zhuce.html',{'errors':errors})  
            if password1!=password2:  
                errors.append("两次输入的密码不一致!")  
                return render(request,'zhuce.html',{'errors':errors}) 
            if len(email) < 9:
                errors.append("请输入有效邮箱")
                return render(request,'zhuce.html',{'errors':errors})
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = settings.SERVER_EMAIL
            user=User()
            user.username=username  
            user.set_password(password1)  
            user.email=email  
            user.save()
            user.is_active=False
            newUser=authenticate(username=username,password=password1)
            message = "nasi"
            send_mail(u'注册用户验证信息',message, from_email,[email])
            if newUser is not None: 
                send_mail('用户注册', '注册成功',from_email,[to_email], fail_silently=False) 
                login(request, newUser)
                request.session['username'] = username
                return redirect("http://127.0.0.1:8000/list/")  
    except Exception as e:  
        errors.append(str(e))  
        return render(request,'zhuce.html',{'errors':errors}) 
    return render(request,'zhuce.html') 

#博客系统及评论系统及搜索系统
def blog_page(request):
    if request.method == "POST":
    	keywords = request.POST['q']
    	sform = SearchForm(request.POST)
    	posts = sform.search()
    	return render(request, 'search_list.html',
                  {'posts': posts, 'list_header': '关键字 \'{}\' 搜索结果'.format(keywords)})
    blogs = Blog.objects.all().order_by('-created')
    paginator = Paginator(blogs, 10)
    page = 1
    try:
    	contacts = paginator.page(page)
    except PageNotAnInteger:
    	contacts = paginator.page(1)
    except EmptyPage:
    	contacts = paginator.page(paginator.num_pages)
    return render(request,'blog.html', {"blogs": contacts})
def detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        blog.look = blog.look + 1
        blog.save()
    except Blog.DoesNotExist:
        raise Http404
 
    if request.method == 'GET':
        form = CommentForm()
        if request.GET.get('dianzan') :
        	blog.dianzan = blog.dianzan + 1
        	blog.save()
        if request.GET.get('chapin') :
        	blog.chapin = blog.chapin + 1
        	blog.save()
    else:   	
        form = CommentForm(request.POST)
        if form.is_valid():
            blog.commen = blog.commen + 1
            blog.save()
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html',ctx)

