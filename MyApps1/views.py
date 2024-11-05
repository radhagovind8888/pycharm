from django.shortcuts import render
from MyApps1.models import Company
from django.views.generic import CreateView
from django.views.generic import DetailView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class CompanyCreateView(CreateView):
		model=Company
		fields = ('name', 'location','ceo')

	#default template_name is company_list.html
	#defult context_object_name is company_list var

class CompanyDetailView(DetailView):
	model=Company
	#default template_name is company_detail.html
	#defult context_object_name is "company"o r given-object for company_list, which is in usage for company_list.html
class CompanyListView(ListView):
	model=Company

class CompanyUpdateView(UpdateView):
	model=Company
	fields=('name','ceo');

class CompanyDeleteView(DeleteView):
	model=Company
	success_url = reverse_lazy('list')