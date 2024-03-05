from vacancies.models import Vacancy
from .forms import VacancyForm
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages


class VacancyHome(ListView):
    model = Vacancy
    template_name = "vacancies/index.html"
    context_object_name = "vacancies"

    def get_queryset(self):
        return Vacancy.objects.filter(visibility=True)


def vacancy_detail_view(request, pk):
    context = {}
    context["vacancy"] = Vacancy.objects.get(id=pk)
    return render(request, "vacancies/detail.html", context)


class MyVacancies(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "vacancies/my_vacancies.html"

    def get_queryset(self):
        qs = Vacancy.objects.filter(owner=self.request.user)
        return qs

    def vacancies_exisist(self, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            messages.info(self.request, "you have no vacancies")

            return redirect("vacancies:send_vacancy")
        return super().get(self.request, *args, **kwargs)


class VacancySearch(VacancyHome):
    template_name = "vacancies/search.html"

    def get_queryset(self):
        qs = Vacancy.objects.filter(visibility=True)

        search = self.request.GET.get("search")
        occupation = self.request.GET.get("occupation")
        state = self.request.GET.get("state")

        if occupation and search and state:
            qs = qs.filter(
                Q(occupation_area__name=occupation)
                & Q(search__icontains=search)
                & Q(state__name=state)
            )
            return qs

        if occupation and search:
            qs = qs.filter(
                Q(occupation_area__name=occupation) & Q(name__icontains=search)
            )
            return qs

        if state and search:
            qs = qs.filter(Q(state__name=state) & Q(name__icontains=search))
            return qs

        if occupation and state:
            qs = qs.filter(Q(occupation_area__name=occupation) & Q(state__name=state))
            return qs

        if occupation:
            qs = qs.filter(Q(occupation_area__name=occupation))
            return qs

        if state:
            qs = qs.filter(Q(state__name=state))
            return qs

        if search:
            qs = qs.filter(Q(name__icontains=search))
            return qs
        return qs


class VacancyCategory(VacancyHome):
    template_name = "vacancies/vacancy_category.html"

    def get_queryset(self):
        category = self.kwargs.get("category", None)

        qs = Vacancy.objects.filter(category__name=category)
        return qs


class VacancyStateFilter(VacancyHome):
    template_name = "vacancies/state_filter.html"

    def get_queryset(self):
        state = self.kwargs.get("state", None)

        qs = Vacancy.objects.filter(state__name=state)
        return qs


def send_vacancy(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.owner = request.user
            vacancy.save()
            messages.success(request, "Vacancy sent")
            return redirect("vacancies:home")
    else:
        form = VacancyForm(user=request.user)
        return render(request, "vacancies/send_vacancy.html", {"form": form})


def delete_vacancy(request, pk):
    obj = Vacancy.objects.get(id=pk)
    obj.delete()
    messages.warning(request, "Vacancy deleted")
    return redirect("vacancies:my_vacancies")
