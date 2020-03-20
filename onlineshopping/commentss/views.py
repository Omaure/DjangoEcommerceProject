from django.shortcuts import render
from myshopping.models import Product
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

def post_detail(request, product_name):
    template_name = 'post_detail.html'
    post = get_object_or_404(Product, slug=product_name)
    comments = post.comments.filter(product_name=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})