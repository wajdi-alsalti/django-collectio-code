from django.shortcuts import redirect, render
from . models import Cards
from django.core.paginator import Paginator
from .form import AddCode,EditCode
from django.urls import reverse
from .filters import CardFilter
from django.db.models.query_utils import Q


# Create your views here.

# will browse all the cards in data base
def allCards(request):
    all_cards = Cards.objects.all()

    paginator = Paginator(all_cards, 3) # Show 1 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'allCard':all_cards,
                'page_obj':page_obj,
                }

    return render(request,'allCards/cards.html',context)

# make filter to the user for his added cards and can edit
def userCard(request):
    cards = Cards.objects.all().filter(owner=request.user.username)
    print(cards)

    paginator = Paginator(cards, 3) # Show 1 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'allCards/userCards.html',{'cards':cards,'page_obj':page_obj})

# will open a single page for the card with the title of the card
def singelCard(request,slug):
    card = Cards.objects.get(slug=slug)
    image = card.image
    header = card.header
    description = card.description
    category = card.category 
    code = card.code_blog
    date = card.publish_at
    writer = card.owner
    categoryImage = category.image

    # use sluge to be argument to editCard path to link the same blog 
    sluge = card.slug

    
    # the class name is language-css (example) so we take the name from catgorey and pass in languageStyle
    # and render in html then the code colored in the blog cause we use prism.css 
    # show in the style code blog for which languages
    languageStyle = f'language-{category}'

    context = {
            'cardTitle':card,
            'cardImage':categoryImage,
            'header':header,
            'description':description,
            'lType':languageStyle,
            'code':code,
            'date':date,
            'writer':writer,
            'sluge':sluge,
            }

    return render(request,'allCards/cardDetail.html', context)


# will filter data base for the name of category number (muster function for all languages)
# languageListcategory : 1 - python, 2 - javaScript, 3 - html, 4 - css, 5 - django
def languageListcategory(name,category,request):
    language = Cards.objects.filter(category=category)
    # language will print all cards related to the category then used list 0 to access first item and bring image
    image = language[0].image

    paginator = Paginator(language, 3) # Show contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'allCards/cards.html',{f'{name}':language,'page_obj':page_obj,'Image':image})


# for python cards
def pythonList(request):
    return languageListcategory('python',1,request)

# for django
def djangoList(request):
    return languageListcategory('django',5,request)

#for java script
def jscriptList(request):
    return languageListcategory('java script',2,request)
    
# for html
def htmlList(request):
    return languageListcategory('html',3,request)

# for css
def cssList(request):
    return languageListcategory('Css',4,request)



# render the home page cause have another section it is not include in another pages
def homePage(request):
    return render(request,'allCards/home1.html',{})

# to search the cards that contain the words in input field search
def search(request):
    # request from the search field in home page or search bar from base
    if request.method == 'GET':
        # this will get the name of the input we named search in base.html and home.html and will look for this name
        query = request.GET.get('search')
        # filter the cards that header and description contin the text from the input
        result = Cards.objects.filter(Q(header__icontains=query) | Q(description__icontains=query))

    return render(request,'allCards/search_page.html',{'query':query,'result':result})

"""
    we can use user User class built in django and all attribute in the html files
    user.profile.image.url direct in html file will show us the image of the user hade been login

"""
########################################################################
# this how can we get the photo of user from profile class same for the other
# def img(request):
#     userImage = request.user.profile.image
#     # print( type(userImage) )
#     return render(request,'',{'userImage':userImage})
########################################################################

# for adding new cards in data base
def addNewCode(request):
    if request.method == 'POST':
        form = AddCode(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.owner = request.user

            myForm.language_type = myForm.category
            # cause image field is not exist and empty in form and category related the image, before we save we access the image from category image
            myForm.image = myForm.category.image

            myForm.save()
            return redirect(reverse('cardsShow:allCards'))
    else:
        form = AddCode()

    return render(request,'allCards/addCode.html',{'form':form})

# editing the description and the code block
def editCard(request,slug):
    edit = None
    card = Cards.objects.get(slug=slug)
    if request.method == 'POST':
        edit = EditCode(request.POST, instance=card)
        if edit.is_valid():
            editForm = edit.save(commit=False)
            editForm.user = request.user
            editForm.save()
            # pass the argument like this slug=slug to return to the same page after edit
            # because cardDetail need argument and is the slug 
            return redirect('cardsShow:cardDetail', slug=slug)
    else:
        edit = EditCode(instance=card)
    return render(request,'allCards/edit_card.html',{'form':edit})