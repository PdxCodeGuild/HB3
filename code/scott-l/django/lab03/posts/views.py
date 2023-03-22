from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def postsIndex(request):
    context = {'postsIndex':'posts Index placeholer'}
    return render(request, 'posts/postsIndex.html',context)


def user_post(request):
    if request.method == 'POST':
        user_post_result = request.POST['user_post_char']
        print(user_post_result) #DEBUG
        userModelObject = User.objects.get(username=request.user)
        print(userModelObject) #DEBUG
        blog_post = BlogPost(text=user_post_result,userNamePost=userModelObject)
        blog_post.save()
        context = {'blogPostInfo': blog_post}
        return HttpResponseRedirect(reverse('users:user_profile'),context)
        
    # else:
    #     return render(request, 'users/profileIndex.html') 
#end def user_registration    
    