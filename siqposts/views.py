from .models import Comment
from django.http import HttpResponseRedirect
from django.urls import reverse

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            return HttpResponseRedirect(reverse('post_detail', args=[pk]))

    return render(request, 'siqposts/post_detail.html', {'post': post, 'comments': comments})
