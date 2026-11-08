from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from .content import SUBJECTS, YEAR_CONTENT, year_band


def home(request):
    subjects = [
        {
            'name': 'Science',
            'slug': 'science',
            'description': 'Explore the solar system and the world around you.',
            'available': True,
            'url_name': 'science',
            'number': '01',
        },
        {
            'name': 'Maths',
            'slug': 'maths',
            'description': 'A space for numbers, patterns, and problem solving.',
            'available': True,
            'url_name': 'maths',
            'number': '02',
        },
        {
            'name': 'English',
            'slug': 'english',
            'description': 'A place for reading, writing, and new ideas.',
            'available': True,
            'url_name': 'english',
            'number': '03',
        },
        {
            'name': 'Django',
            'slug': 'django',
            'description': 'Learn how Python helps build websites and web apps.',
            'available': True,
            'url_name': 'django',
            'number': '04',
        },
        {
            'name': 'Coding',
            'slug': 'coding',
            'description': 'Discover how instructions turn ideas into digital projects.',
            'available': True,
            'url_name': 'coding',
            'number': '05',
        },
    ]
    ready_count = sum(subject['available'] for subject in subjects)
    return render(request, 'learning/home.html', {
        'subjects': subjects,
        'ready_count': ready_count,
    })


def science(request):
    return render(request, 'learning/science.html')


def maths(request):
    return render(request, 'learning/maths.html')


def english(request):
    return render(request, 'learning/english.html')


def django(request):
    return render(request, 'learning/django.html')


def coding(request):
    return render(request, 'learning/coding.html')


def learning_library(request):
    years = [
        {'number': year, 'band': year_band(year)}
        for year in YEAR_CONTENT
    ]
    return render(request, 'learning/year_index.html', {'years': years})


def year_dashboard(request, year):
    if year not in YEAR_CONTENT:
        raise Http404('That school year is not in the library.')

    subjects = []
    for subject in SUBJECTS:
        lesson_data = YEAR_CONTENT[year][subject['slug']]
        subjects.append({
            **subject,
            'topic': lesson_data['topic'],
            'url': reverse('year_subject', args=[year, subject['slug']]),
        })

    return render(request, 'learning/year_dashboard.html', {
        'year': year,
        'band': year_band(year),
        'subjects': subjects,
    })


def year_subject(request, year, subject_slug):
    if year not in YEAR_CONTENT:
        raise Http404('That school year is not in the library.')

    subject = next(
        (subject for subject in SUBJECTS if subject['slug'] == subject_slug),
        None,
    )
    if subject is None:
        raise Http404('That subject is not in the library.')

    return render(request, 'learning/year_subject.html', {
        'year': year,
        'band': year_band(year),
        'subject': subject,
        'resource': YEAR_CONTENT[year][subject_slug],
    })


def solar_system(request):
    # Send the original simulation file without copying or changing it.
    simulation_file = (settings.BASE_DIR / 'index.html').open('rb')
    return FileResponse(simulation_file, content_type='text/html')
