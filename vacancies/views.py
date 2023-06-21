from vacancies.models import Vacancy
from .forms import VacancyForm
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.db.models import Q, Case, When
from choices.occupation_choices import OCCUPATION_AREA_CHOICES
from choices.stt_choices import STATE_CHOICES


class VacancyHome(ListView):
    model = Vacancy
    template_name = 'vacancies/index.html'
    context_object_name = 'vacancies'


def vacancy_detail_view(request, pk):
    context ={}
    context['vacancy'] = Vacancy.objects.get(id=pk)
    return render(request, "vacancies/detail.html", context)


class VacancySearch(VacancyHome):
    template_name = 'vacancies/search.html'
    
    def get_queryset(self):
        qs = Vacancy.objects.all()


        search = self.request.GET.get('search')
        occupation = self.request.GET.get('occupation')
        state = self.request.GET.get('state')

        if occupation and search and state:
            for k, v in OCCUPATION_AREA_CHOICES:
                if v == occupation:
                    occupation = k
            
            for k, v in STATE_CHOICES:
                if v == state:
                    state = k
                    
                    qs = qs.filter(
                        Q(occupation_area__iexact=occupation) &
                        Q(name__icontains=search) &
                        Q(state__iexact=state) 
                    )
                    return qs
        
        if occupation and search:
            for k, v in OCCUPATION_AREA_CHOICES:
                if v == occupation:
                    occupation = k
                    
                    qs = qs.filter(
                        Q(occupation_area__iexact=occupation) &
                        Q(name__icontains=search)
                    )
                    return qs
                
        if state and search:
            for k, v in STATE_CHOICES:
                if v == state:
                    state = k
                    
                    qs = qs.filter(
                        Q(state__iexact=state) &
                        Q(name__icontains=search)
                    )
                    return qs
                
        if occupation and state:
            for k, v in OCCUPATION_AREA_CHOICES:
                if v == occupation:
                    occupation = k
            
            for k, v in STATE_CHOICES:
                if v == state:
                    state = k
                    
                    qs = qs.filter(
                        Q(occupation_area__iexact=occupation) &
                        Q(state__iexact=state) 
                    )
                    return qs
                
        if occupation:
            for k, v in OCCUPATION_AREA_CHOICES:
                if v == occupation:
                    occupation = k
                    
                    qs = qs.filter(
                        Q(occupation_area__iexact=occupation)
                    )
                    return qs
                
        if state:
            for k, v in STATE_CHOICES:
                if v == state:
                    state = k
                    
                    qs = qs.filter(
                        Q(state__iexact=state)
                    )
                    return qs
        
        if search:
            qs = qs.filter(
                Q(name__icontains=search)
            )
            return qs
        return qs


class VacancyCategory(VacancyHome):
    template_name = 'vacancies/vacancy_category.html'
    
    def get_queryset(self):
        category = self.kwargs.get('category', None)

        qs = Vacancy.objects.filter(category__name=category)        
        return qs


def send_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('vacancies:home')
    else:
        form = VacancyForm()
        return render(request, 'vacancies/send_vacancy.html', {'form': form})
