from typing import Any
from django.shortcuts import render, redirect
from .import forms,models
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from carshop.models import Car    
from django.contrib import messages
from django.utils import timezone
from .models import Purchase

class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'detail_car.html'

    def post(self, request, *args,**kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args,**kwargs)




    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


# def buy(request, post_id):
#     if request.user.is_authenticated:
#         try:
#             post = Car.objects.get(id=post_id)
#         except Car.DoesNotExist:
#             return redirect('home')

#         if post.quantity > 0:
#             post.quantity -= 1
#             post.save()
#             return redirect('home')
#         else:
#             return redirect('home')
#     else:
#         return redirect('user_login')
    



# def buy(request, post_id):
#     if request.user.is_authenticated:
#         try:
#             post = Car.objects.get(id=post_id)
#         except Car.DoesNotExist:
#             return redirect('home')

#         if post.quantity > 0:
#             post.quantity -= 1
#             post.save()
            
#             # Create a new Purchase object
#             purchase = Purchase(user=request.user, car=post)
#             purchase.save()
            
#             return redirect('home')
#         else:
#             return redirect('home')
#     else:
#         return redirect('user_login')

@login_required
def buy(request, post_id):
    if request.method == 'POST':
        car = Car.objects.get(id=post_id)
        if car.quantity != 0:
            car.quantity -= 1
            car.save()
            purchase = Purchase(user=request.user, car=car, brand=car.brand)
            purchase.save()
            messages.success(request, f'Thank you for purchasing {car.name}')
            return redirect('profile')
        else:
            messages.error(request,"sorry not available")
            return render(request, 'buy.html', {'car': car})
            
            
    else:
        return render(request, 'buy.html', {'car': Car.objects.get(id=post_id)})