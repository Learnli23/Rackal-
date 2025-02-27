from django.shortcuts import render,get_object_or_404, redirect
from .models import Dummies,vidoes
from .forms import DummiesForm
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import CommentForm,BlogForm
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
# Create your views here.
# home
def home(request):
    images = Dummies.objects.all()
    videos = vidoes.objects.all()
    return render(request, 'home.html' , {
        'images': images,
        'videos':videos,
         })

#gallery view
def gallery(request):
    # Query the database for all pictures
    gallery_pictures = Dummies.objects.all()
    paginator = Paginator(gallery_pictures, 20)  # 20 images per page
     # Implement pagination
    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'gallery.html', {'page_obj': page_obj})

#kids view
def kids(request): 
    # Query the database for all pictures
    kids_pictures = Dummies.objects     .filter(category='kids')
    paginator = Paginator(kids_pictures, 20)  # 20 images per page
     # Implement pagination
    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'kids.html', {'page_obj': page_obj})


#men view
def men(request): 
    # Query the database for all pictures
    men_pictures = Dummies.objects.filter(category='men')
    paginator = Paginator(men_pictures, 20)  # 20 images per page
     # Implement pagination
    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'men.html', {'page_obj': page_obj})

#women view view
def women(request): 
    # Query the database for all pictures
    women_pictures = Dummies.objects.filter(category='women')
    paginator = Paginator(women_pictures, 20)  # 20 images per page
     # Implement pagination
    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'women.html', {'page_obj': page_obj})

# customizable
def customizable(request): 
    # Query the database for all pictures
    customizable_pictures = Dummies.objects.filter(category='customizable')
    paginator = Paginator(customizable_pictures, 20)  # 20 images per page
     # Implement pagination
    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'customizable.html', {'page_obj': page_obj}) 


#gallery view
def fashion(request): 
    # Query the database for all pictures
    fashion_pictures = Dummies.objects.filter(category='fashion')
    paginator = Paginator(fashion_pictures, 20)  # 20 images per page
     # Implement pagination
    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'fashion.html', {'page_obj': page_obj})   

#gallery view
def store(request): 
    # Query the database for all pictures
    store_pictures = Dummies.objects.filter(category='store_display')
    paginator = Paginator(store_pictures, 20)  # 20 images per page
     # Implement pagination
    page_number = request.GET.get('page')  # Get the current page number from query parameters
    page_obj = paginator.get_page(page_number)  # Get the corresponding page object
    return render(request, 'store.html', {'page_obj': page_obj})  





# Create your views here.


@login_required
def create_blog(request): 
    submitted = False
    if request.method == 'POST':
        form =BlogForm(request.POST, request.FILES)
        if form.is_valid():
              BlogPost = form.save(commit=False)
              BlogPost.author = request.user 
              BlogPost.save()
              form.save() 
              return redirect('blog_list')
               

    else:
         form = BlogForm()
         if 'submitted' in request.GET:
            submitted = True

    return render(request,'create_blog.html' ,{'form':form, 'submitted':submitted})



def blog_list(request):
    posts = BlogPost.objects.filter(is_hiden = False).order_by('-created_at')
    blog_content_type = ContentType.objects.get_for_model(BlogPost)  # Get ContentType for Blog mode
    return render(request, 'blog_list.html',
                   {
                        'posts': posts,
                        'blog_content_type': blog_content_type,  # Pass the ContentType instance to the template
                        })

@login_required
def blog_detail(request, post_id):
       post = get_object_or_404(BlogPost, id=post_id)
       comments = post.comments.all()
       if request.method == 'POST':
           form = CommentForm(request.POST)
           if form.is_valid():
               comment = form.save(commit=False)
               comment.author = request.user
               comment.post = post
               comment.save()
               return redirect('blog_detail', post_id=post.id)
       else:
           form = CommentForm()
       return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'form': form})  


@login_required
def edit_post(request,  post_id):
    post = BlogPost.objects.get(pk = post_id)
    form = BlogForm( request.POST or None, request.FILES or None, instance= post)
    if form.is_valid():
           form.save()
           return redirect('blog_list')
    

    return render(request, 'edit_post.html', {
        "post": post,
        'form':form,
    })




@login_required
def delete_post(request, post_id):
        post = BlogPost.objects.get(pk = post_id)
        post.delete()
        messages.success(request,('post deleted!!'))
        return redirect('blog_list')        

 
@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('blog_detail', post_id=post.id)

@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
    return redirect('blog_detail', post_id=post.id)      
    
       

'''
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ebook, Section,myvideo
from .forms import EbookForm, SectionForm,VideoForm
 
from django.forms import modelformset_factory

# Create your views here.


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = myvideo.objects.all()
    return render(request, 'video_list.html', {'videos': videos})
+

    


def book_list(request):
    books = Ebook.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_details(request, pk):
    book = get_object_or_404(Ebook, pk=pk)
    sections = book.sections.all()
    return render(request, 'book_details.html', {'book': book, 'sections': sections})

def add_book(request):
    if request.method == 'POST':
        form = EbookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()

            return redirect('book_list', pk=book.pk)
    else:
        form = EbookForm()
    return render(request, 'add_book.html', {'form': form})


def add_section(request, book_pk):
    book = get_object_or_404(Ebook, pk=book_pk)
    SectionFormSet = modelformset_factory(Section, form=SectionForm, extra=1, can_delete=True)

    if request.method == 'POST':
        formset = SectionFormSet(request.POST, request.FILES, queryset=book.sections.all())
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.ebook = book
                instance.save()
            return redirect('book_details', pk=book.pk)
    else:
        formset = SectionFormSet(queryset=book.sections.all())

    return render(request, 'add_section.html', {'book': book, 'formset': formset})


'''
