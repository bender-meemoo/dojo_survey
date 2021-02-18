from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    loc_from_form = request.POST['location']
    lang_from_form = request.POST['language']
    comm_from_form = request.POST['comment']
    context = {
        "coding_dojo_name" : name_from_form,
        "coding_dogo_loc" : loc_from_form,
        "coding_dogo_lang" : lang_from_form,
        "coding_dogo_comment" : comm_from_form
    }
    return render(request,"show.html",context)