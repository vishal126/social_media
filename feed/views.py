from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed:home')
        else:
            return HttpResponse(form.errors)
            
    else:
        form = PostForm()
    return render(request,'post.html',{'form':form})
    
    

@login_required(login_url='accounts:login')
def home(request):
    posts = Post.objects.prefetch_related('likes').all().order_by('-created_at')
    commnets = Comment.objects.all()
    
    return render(request, 'hello.html', {'posts': posts,'comments':commnets})
    
@login_required(login_url ='accounts:login')
def delete_post(request,id):
    post = get_object_or_404(Post, id=id ,user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("feed:home")
    else:
        return render(request,"delete.html")
 
def update_post(request,id):
    post = get_object_or_404(Post, id=id,user=request.user)
    
    if request.method =="POST":
        form = PostForm(request.POST,request.FILES ,instance=post)
        if form.is_valid():
            data = form.cleaned_data
            post.caption = data.get('caption')
            post.image = data.get('image')
            print(post.image)
            print(data)
            post.save()
            return redirect("feed:home")
    else:
        form = PostForm(instance=post)
    return render(request,"update.html",{"form":form})



def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        # If like already exists, this will 'unlike' the post
        like.delete()
    
    return redirect('feed:home')

def comment_post(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
           
            comment.user = request.user
            comment.post = post
            print(f"User: {comment.user}, Post: {comment.post}") 
            comment.save()
            return redirect('feed:home')
    else:
        form = CommentForm()


    return render(request,"comment.html",{"form":form,'post':post})


def comment_list(request):
    comments = Comment.objects.all()
    return render(request,"comment_list.html",{"comments":comments})

@login_required
def profile_edit(request, username):
    # Fetch the user by username
    user = get_object_or_404(User, username=username)
    
    # Ensure a profile exists for the user
    profile, created = User_profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Redirect back to the user's profile after successful edit
            return redirect('feed:profile', username=user.username)
    else:
        form = ProfileForm(instance=profile)

    # Render the appropriate template for profile editing
    return render(request, 'profile.html', {'form': form, 'profile': profile})

@login_required
def profile_view(request, username):
    # Fetch the user by username using get_object_or_404 for better error handling
    user = get_object_or_404(User, username=username)
    
    # Get the user's profile, posts, likes, and comments
    profile = user.user_profile  # This will raise an error if the profile doesn't exist
    posts = Post.objects.filter(user=user)
    likes = Like.objects.filter(user=user)
    comments = Comment.objects.filter(user=user)

    # Pass all the data to the template
    context = {
        'profile': profile,
        'posts': posts,
        'likes': likes,
        'comments': comments,
        'user_profile': user,  # The user whose profile is being viewed
    }

    return render(request, 'user_profile.html', context)


def search_posts(request):
    query = request.GET.get('q')
    users = []
    
    if query:
        # First filter the posts based on the caption
        posts = Post.objects.filter(
            Q(caption__icontains=query)
        ).select_related('user')
        
        # Get distinct users from the filtered posts
        users = User.objects.filter(id__in=posts.values('user_id')).distinct()

    return render(request, 'search_results.html', {'users': users, 'query': query})