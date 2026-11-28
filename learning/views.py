import json
import random
import ssl
import urllib.error
import urllib.request
import uuid

import certifi
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import FileResponse, Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from .content import SUBJECTS, YEAR_CONTENT, year_band
from .models import LearnerPet, LearnerProfile, StudyProgress


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


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'learning/signup.html', {'form': form})


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


def downtime(request):
    return render(request, 'learning/downtime.html')


def dot(request):
    return render(request, 'learning/dot.html', {
        'dot_configured': bool(settings.OPENAI_API_KEY),
    })


@require_POST
def dot_chat(request):
    api_key = settings.OPENAI_API_KEY
    if not api_key:
        return JsonResponse({
            'error': 'Dot needs an OpenAI API key before it can chat. Add OPENAI_API_KEY to the server environment and try again.'
        }, status=503)

    if len(request.body) > 16000:
        return JsonResponse({'error': 'That message is a bit too long. Try shortening it.'}, status=413)

    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({'error': 'I couldn’t read that message. Please try again.'}, status=400)

    messages = payload.get('messages') if isinstance(payload, dict) else None
    if not isinstance(messages, list) or not messages or len(messages) > 12:
        return JsonResponse({'error': 'Send a message to get started.'}, status=400)

    clean_messages = []
    for message in messages:
        if not isinstance(message, dict):
            return JsonResponse({'error': 'That conversation could not be read.'}, status=400)
        role = message.get('role')
        content = message.get('content')
        if role not in {'user', 'assistant'} or not isinstance(content, str) or not content.strip() or len(content) > 2000:
            return JsonResponse({'error': 'Messages must be under 2,000 characters.'}, status=400)
        clean_messages.append({'role': role, 'content': content.strip()})

    request_data = json.dumps({
        'model': settings.OPENAI_MODEL,
        'instructions': (
            'You are Dot, a friendly and patient study helper in a school Study Hub. '
            'If the student has not named a topic yet, ask what they want to study today. '
            'Otherwise, respond to their question directly. Explain ideas clearly '
            'at the student’s level, ask their year level when it would help, use short '
            'steps and examples, and encourage them to think rather than simply doing '
            'their homework for them. You can explain topics, make practice questions, '
            'check understanding, and help plan revision. Keep replies warm and concise. '
            'Do not ask students to share personal or identifying information.'
        ),
        'input': clean_messages,
        'max_output_tokens': 600,
        'store': False,
    }).encode('utf-8')
    upstream_request = urllib.request.Request(
        'https://api.openai.com/v1/responses',
        data=request_data,
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json',
        },
        method='POST',
    )

    try:
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        with urllib.request.urlopen(upstream_request, timeout=45, context=ssl_context) as response:
            result = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        if exc.code == 401:
            message = 'OpenAI rejected the API key. Check that OPENAI_API_KEY contains a valid API key.'
        elif exc.code == 403:
            message = 'This API key does not have permission to use the selected model. Check your OpenAI project access.'
        elif exc.code == 429:
            message = 'The OpenAI API usage limit has been reached or billing is not enabled for this account.'
        elif exc.code == 400:
            message = 'OpenAI rejected the request. Check the OPENAI_MODEL setting and try again.'
        else:
            message = f'OpenAI returned an error (HTTP {exc.code}). Please try again in a moment.'
        return JsonResponse({'error': message}, status=502)
    except (urllib.error.URLError, TimeoutError):
        return JsonResponse({'error': 'Dot couldn’t connect just now. Check your connection and try again.'}, status=502)
    except (json.JSONDecodeError, OSError):
        return JsonResponse({'error': 'Dot received an unreadable reply. Please try again.'}, status=502)

    reply = ''.join(
        item.get('text') or item.get('refusal', '')
        for output_item in result.get('output', [])
        if output_item.get('type') == 'message'
        for item in output_item.get('content', [])
        if item.get('type') in {'output_text', 'refusal'}
    ).strip()
    if not reply:
        return JsonResponse({'error': 'Dot didn’t have a reply ready. Please try again.'}, status=502)
    return JsonResponse({'reply': reply})


def learning_library(request):
    years = [
        {'number': year, 'band': year_band(year)}
        for year in YEAR_CONTENT
    ]
    return render(request, 'learning/year_index.html', {'years': years})


def year_dashboard(request, year):
    if year not in YEAR_CONTENT:
        raise Http404('That school year is not in the library.')

    progress_by_subject = {}
    if request.user.is_authenticated:
        progress_by_subject = {
            row.subject_slug: row
            for row in StudyProgress.objects.filter(user=request.user, year=year)
        }

    subjects = []
    for subject in SUBJECTS:
        lesson_data = YEAR_CONTENT[year][subject['slug']]
        unit_slug = slugify(lesson_data['topic']) or 'core'
        subjects.append({
            **subject,
            'topic': lesson_data['topic'],
            'url': reverse('year_subject', args=[year, subject['slug']]),
            'progress': progress_by_subject.get(subject['slug']),
            'unit_slug': unit_slug,
        })

    completed_count = sum(subject['progress'] is not None for subject in subjects)
    profile = LearnerProfile.objects.filter(user=request.user).first() if request.user.is_authenticated else None

    return render(request, 'learning/year_dashboard.html', {
        'year': year,
        'band': year_band(year),
        'subjects': subjects,
        'completed_count': completed_count,
        'subject_count': len(subjects),
        'year_percent': round(completed_count * 100 / len(subjects)) if subjects else 0,
        'profile': profile,
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

    resource = YEAR_CONTENT[year][subject_slug]
    resource = {
        **resource,
        'questions': random.sample(resource['questions'], k=5),
    }

    unit_slug = slugify(resource['topic']) or 'core'
    quiz_id = uuid.uuid4().hex
    request.session[f'study_quiz_{quiz_id}'] = {
        'user_id': request.user.pk if request.user.is_authenticated else None,
        'year': year,
        'subject_slug': subject_slug,
        'unit_slug': unit_slug,
        'questions': [
            {
                'answer': item['answer'],
                'answer_text': item['options'][item['answer']],
                'explanation': item['explanation'],
            }
            for item in resource['questions']
        ],
    }
    progress = None
    if request.user.is_authenticated:
        progress = StudyProgress.objects.filter(
            user=request.user, year=year, subject_slug=subject_slug, unit_slug=unit_slug,
        ).first()

    return render(request, 'learning/year_subject.html', {
        'year': year,
        'band': year_band(year),
        'subject': subject,
        'resource': resource,
        'quiz_id': quiz_id,
        'progress': progress,
    })


@require_POST
def submit_quiz(request):
    if len(request.body) > 4000:
        return JsonResponse({'error': 'That quiz response is too long.'}, status=413)
    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({'error': 'That quiz response could not be read.'}, status=400)

    quiz_id = payload.get('quiz_id') if isinstance(payload, dict) else None
    selected_answers = payload.get('answers') if isinstance(payload, dict) else None
    if not isinstance(quiz_id, str) or len(quiz_id) != 32 or not isinstance(selected_answers, list):
        return JsonResponse({'error': 'Please reload the lesson and try the quiz again.'}, status=400)

    session_key = f'study_quiz_{quiz_id}'
    quiz = request.session.get(session_key)
    if not isinstance(quiz, dict):
        return JsonResponse({'error': 'This quiz has expired. Reload the lesson to try a new one.'}, status=400)
    if quiz.get('user_id') != (request.user.pk if request.user.is_authenticated else None):
        return JsonResponse({'error': 'Your sign-in changed. Reload this lesson before submitting.'}, status=403)

    questions = quiz.get('questions', [])
    if len(selected_answers) != len(questions) or not questions:
        return JsonResponse({'error': 'Answer every question, then try again.'}, status=400)
    try:
        selected_answers = [int(answer) for answer in selected_answers]
    except (TypeError, ValueError):
        return JsonResponse({'error': 'One of those answers could not be read.'}, status=400)
    if any(answer < 0 or answer > 2 for answer in selected_answers):
        return JsonResponse({'error': 'One of those answers is not available.'}, status=400)

    score = sum(
        selected == question['answer']
        for selected, question in zip(selected_answers, questions)
    )
    feedback = [
        {
            'correct': selected == question['answer'],
            'answer_index': question['answer'],
            'answer_text': question['answer_text'],
            'explanation': question['explanation'],
        }
        for selected, question in zip(selected_answers, questions)
    ]
    request.session.pop(session_key, None)

    coins_earned = 0
    best_score = score
    saved = False
    if request.user.is_authenticated:
        total = len(questions)
        with transaction.atomic():
            profile, _ = LearnerProfile.objects.select_for_update().get_or_create(user=request.user)
            progress, _ = StudyProgress.objects.select_for_update().get_or_create(
                user=request.user,
                year=quiz['year'],
                subject_slug=quiz['subject_slug'],
                unit_slug=quiz['unit_slug'],
                defaults={'question_count': total},
            )
            previous_best = progress.best_score if progress.question_count == total else 0
            previous_coins = progress.coins_awarded if progress.question_count == total else 0
            best_score = max(previous_best, score)
            total_coins = max(previous_coins, best_score * 100 // total)
            coins_earned = total_coins - previous_coins
            if progress.question_count != total or score > previous_best:
                progress.question_count = total
                progress.best_score = best_score
                progress.coins_awarded = total_coins
                progress.completed_at = timezone.now()
                progress.save()
                saved = True
            if coins_earned:
                profile.coins += coins_earned
                profile.save(update_fields=['coins', 'updated_at'])

    return JsonResponse({
        'score': score,
        'total': len(questions),
        'best_score': best_score,
        'coins_earned': coins_earned,
        'saved': saved,
        'logged_in': request.user.is_authenticated,
        'feedback': feedback,
    })


@login_required
def progress_dashboard(request):
    profile, _ = LearnerProfile.objects.get_or_create(user=request.user)
    progress_rows = list(StudyProgress.objects.filter(user=request.user))
    progress_map = {(row.year, row.subject_slug): row for row in progress_rows}
    subjects_by_year = len(SUBJECTS)
    total_units = len(YEAR_CONTENT) * subjects_by_year
    completed_units = len(progress_rows)
    year_summaries = []
    for year in sorted(YEAR_CONTENT):
        done = sum((year, subject['slug']) in progress_map for subject in SUBJECTS)
        year_summaries.append({
            'year': year,
            'completed': done,
            'total': subjects_by_year,
            'percent': round(done * 100 / subjects_by_year) if subjects_by_year else 0,
            'url': reverse('year_dashboard', args=[year]),
        })
    pets = list(LearnerPet.objects.filter(user=request.user))
    for pet in pets:
        pet.label = pet.get_species_display() if pet.species else 'Unhatched egg'

    return render(request, 'learning/progress.html', {
        'profile': profile,
        'year_summaries': year_summaries,
        'completed_units': completed_units,
        'total_units': total_units,
        'overall_percent': round(completed_units * 100 / total_units) if total_units else 0,
        'pets': pets,
        'egg_cost': 100,
    })


@login_required
@require_POST
def buy_egg(request):
    with transaction.atomic():
        profile, _ = LearnerProfile.objects.select_for_update().get_or_create(user=request.user)
        if profile.coins < 100:
            messages.error(request, 'You need 100 coins to buy an egg. Finish a quiz to earn more.')
        else:
            profile.coins -= 100
            profile.save(update_fields=['coins', 'updated_at'])
            LearnerPet.objects.create(user=request.user)
            messages.success(request, 'Egg purchased! Hatch it when you’re ready to meet your pet.')
    return redirect('progress')


@login_required
@require_POST
def hatch_egg(request, pet_id):
    pet = get_object_or_404(LearnerPet, pk=pet_id, user=request.user, species='')
    pet.species = random.choice([key for key, _label in LearnerPet.PET_CHOICES])
    pet.name = dict(LearnerPet.PET_CHOICES)[pet.species]
    pet.hatched_at = timezone.now()
    pet.save(update_fields=['species', 'name', 'hatched_at'])
    messages.success(request, f'Your egg hatched into a {pet.get_species_display()}!')
    return redirect('progress')


def solar_system(request):
    # Send the original simulation file without copying or changing it.
    simulation_file = (settings.BASE_DIR / 'index.html').open('rb')
    return FileResponse(simulation_file, content_type='text/html')
