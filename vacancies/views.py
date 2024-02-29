from vacancies.models import Vacancy
from .forms import VacancyForm
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.db.models import Q
from choices.stt_choices import STATE_CHOICES
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


class VacancySearch(VacancyHome):
    template_name = "vacancies/search.html"

    def get_queryset(self):
        qs = Vacancy.objects.filter(visibility=True)

        search = self.request.GET.get("search")
        occupation = self.request.GET.get("occupation")
        state = self.request.GET.get("state")

        if occupation and search and state:
            for key, value in STATE_CHOICES:
                if key == state:
                    state = value
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
            for key, value in STATE_CHOICES:
                if value == state:
                    state = key
                    qs = qs.filter(Q(state__name=state) & Q(name__icontains=search))
                    return qs

        if occupation and state:
            for key, value in STATE_CHOICES:
                if value == state:
                    state = key
                    qs = qs.filter(
                        Q(occupation_area__name=occupation) & Q(state__name=state)
                    )
                    return qs

        if occupation:
            qs = qs.filter(Q(occupation_area__name=occupation))
            return qs

        if state:
            for key, value in STATE_CHOICES:
                if value == state:
                    state = key
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
            form.save()
            messages.success(request, "Vacancy sent")
            return redirect("vacancies:home")
    else:
        form = VacancyForm()
        return render(request, "vacancies/send_vacancy.html", {"form": form})
