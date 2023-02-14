from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from .forms import postForm

# Create your views here.
class index(View):
	template_name = 'blogging/index.html'

	def queryset(self):
		return Post.objects.all()

	def get(self, request, *args, **kwargs):
		context = {"blogs":self.queryset()}
		return render(request, self.template_name, context)


class create(View):
	template_name = "blogging/update_blog.html"


	def get(self, request, *args, **kwargs):
		form = postForm()
		context = {"form":form}

		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = postForm(request.POST or None)
		if form.is_valid():
			form.save()
			form = postForm()

		context = {
			"form":form
			}
		return render(request, self.template_name, context)


class read(View):
	template_name = "blogging/read.html"

	def get(self, request, id=None, *args, **kwargs):
		obj = get_object_or_404(Post, id=id)
		context = {
			"object" : obj
		}

		return render(request, self.template_name, context)