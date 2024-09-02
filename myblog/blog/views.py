from django.shortcuts import render, get_object_or_404, redirect
from .models import blog, contact
from .forms import blogForm, userForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout



# Create your views here.

def index(request):
    return render(request,  'index.html')


def blog_list(request):
    
    Blogs = blog.objects.all().order_by('-created_at')
    return render(request, 'blogList.html', {'Blogs': Blogs})
@login_required
def blog_create(request):
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            finalBlog = form.save(commit=False)
            finalBlog.user = request.user
            finalBlog.save()
            return redirect('blog_list')
    else:
        form = blogForm()
    return render(request, 'blogForm.html', {'form':form})

@login_required
def blog_edit(request, blog_id):
    
    vlog = get_object_or_404(blog, pk=blog_id, user = request.user )
    if request.method == 'POST':
        form = blogForm(request.POST, request.FILES, instance=vlog)
        if form.is_valid():
            updated_blog = form.save(commit=False)
            updated_blog.user = request.user
            updated_blog.save()
            return redirect('blog_list')
    else:
        form = blogForm(instance=vlog)
    return render(request, 'blogForm.html', {'form':form})


@login_required
def blog_delete(request, blog_id):
    Blog = get_object_or_404(blog, pk=blog_id , user=request.user)
    if request.method == 'POST':
        Blog.delete()
        return redirect('blog_list')
    return render(request, 'blogDelete.html', {'Blog':Blog})

def register(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('blog_list')
    else:
        form = userForm()
    return render(request, 'registration/register.html', {'form': form})



def user_logout(request):
    if request.method == 'POST':
        print("Logout function called") 
        logout(request)
    return redirect('login')

def about(request):
    return render(request, 'about.html')

def contect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')

        Message = contact(name=name, message=message, phone=phone)

        Message.save()
        return redirect('blog_list')
    return render(request, 'contact.html')


