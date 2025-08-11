from django.shortcuts import redirect, render
from contact.models import Category, Contact
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('first_name')
    paginator = Paginator(contacts, 10)  # 20 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'contacts': page_obj
    }
    
    return render(request, 'contact/pages/index.html', context)

def search(request):
    search_query = request.GET.get('q', '').strip()
    error_message = None
    if search_query == '':       
        return redirect('contact:index')
    
    contacts = Contact.objects.filter(
        show=True
    ).filter(
        Q(first_name__icontains=search_query) |
        Q(last_name__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(phone_number__icontains=search_query)
    ).order_by('first_name')

    if contacts.count() == 0:
        error_message = 'Nenhum contato encontrado.'
        context = {
            'error_message': error_message,
            'contacts': []
        }
        return render(request, 'contact/pages/index.html', context)
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'contacts': page_obj
    }
    return render(request, 'contact/pages/index.html', context)

def contact_info(request, contact_id):
    if  not contact_id.isdigit():
        return render(request, 'contact/pages/contact_404.html', status=404)
    
    contact = Contact.objects.filter(code=contact_id,show=True).first()

    if not contact:
        return render(request, 'contact/pages/contact_404.html', status=404)
    
    context = {
        'contact': contact,
        'title': f'{contact.first_name} {contact.last_name}',
        'owner': request.user
    }
    return render(request, 'contact/pages/info.html', context)

def contact_create(request):
    categories = Category.objects.all()
    owner = request.user
    context = {
        'categories': categories,
        'owner': owner,
        'title': 'Criar Contato'
    }
    # Logic for creating a contact will go here
    return render(request, 'contact/pages/create.html',context)

def create(request):
    if not request.POST:
        return redirect('contact:index')
    first_name = request.POST.get('first_name', '').strip()
    last_name = request.POST.get('last_name', '').strip()
    email = request.POST.get('email', '').strip()
    phone_number = request.POST.get('phone_number', '').strip() 
    description = request.POST.get('description', '').strip()
    category_id = request.POST.get('category', '').strip()
    show = True

    contact = Contact(
        first_name=first_name,  
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        description=description,
        category_id=category_id,
        show=show,
        owner=request.user
    )
    contact.save()
    return redirect('contact:index')


