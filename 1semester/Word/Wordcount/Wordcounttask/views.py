from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    input_text=request.GET['fulltext']
    word_list = input_text.split()
    
    word_dict={}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return render(request, 'result.html',{'fulltext':input_text,'total': len(word_list), 'dictionary':word_dict.items()})

