from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Question, Result
from .forms import RegisterForm


def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("/quiz/")

    return render(request, "login.html")


@login_required
def quiz(request):

    questions = list(Question.objects.all().order_by("question_no"))

    if "question_index" not in request.session:
        request.session["question_index"] = 0

    if "answers" not in request.session:
        request.session["answers"] = {}

    index = request.session["question_index"]
    answers = request.session["answers"]

    if request.method == "POST":

        action = request.POST.get("action")
        selected = request.POST.get("answer")

        if selected:
            answers[str(index)] = selected
            request.session["answers"] = answers

        if action == "next":

            if index < len(questions) - 1:
                index += 1

        elif action == "back":

            if index > 0:
                index -= 1

        elif action == "submit":

            score = 0

            for i, q in enumerate(questions):
                if answers.get(str(i)) == q.answer:
                    score += 1

            total = len(questions)
            correct = score
            answered = len(answers)
            wrong = answered - correct
            not_answered = total - answered
            percentage = (score / total) * 100

            Result.objects.create(
                user=request.user,
                score=score
            )

            request.session["question_index"] = 0
            request.session["answers"] = {}

            return render(
                request,
                "result.html",
                {
                    "score": score,
                    "total": total,
                    "correct": correct,
                    "wrong": wrong,
                    "not_answered": not_answered,
                    "percentage": round(percentage, 2)
                }
            )

        request.session["question_index"] = index

    question = questions[request.session["question_index"]]

    return render(
    request,
    "quiz.html",
    {
        "question": question,
        "current": request.session["question_index"] + 1,
        "total": len(questions),
        
    }
)


@login_required
def user_logout(request):

    logout(request)
    return redirect("/")