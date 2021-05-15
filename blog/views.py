from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .models import Post, Contact
from .forms import ContactForm

def index(request):
    articles = Post.objects.filter(status=1).order_by("-date")
    page = request.GET.get('page', 1)

    paginator = Paginator(articles, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "index.html", {"posts": posts})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "detail.html", {"post": post})

def apropos(request):
    return render(request, "apropos.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            content = form.cleaned_data.get("content")

            new_contact = Contact(
                name=name,
                email=email,
                content=content
            )
            new_contact.save()

            # Envoyer email de confirmation
            body = f"""
                    Bonjour {name},
                    Vous avons bien reçu votre message.
                    Nous mettons tout en oeuvre pour vous répondre dans les meilleurs délais.
                """
            send_mail(
                "Confirmation réception de votre message",
                body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            messages.success(
                request,
                "Votre message a été envoyé avec succès",
                "success"
            )
            return redirect("contact")
        else:
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})