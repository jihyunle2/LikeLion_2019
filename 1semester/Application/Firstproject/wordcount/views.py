from django.shortcuts import render

# Create your views here.

#요청이 오면 home을 보여줘라
def home(request):
    return render(request, 'home.html')

def about(request):

    #학교공지사항
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen("http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=37080&siteId=hufs&menuType=T&uId=4&sortChar=AB&linkUrl=04_0202.html&mainFrame=right")
    bsObject = BeautifulSoup(html,"html.parser")

    table = bsObject.find("table")
    titles = table.find_all(class_="title")
    
    notices = {}

    for title in titles:
        x=title.get_text()
        x=x.replace("\t",'')
        x=x.replace("\n",'')
        x=x.strip()
        link = title.a.get('href')
        url = 'http://www.hufs.ac.kr/user/' + link
        notices[x]=url

    #end 학교공지사항

    return render(request, 'about.html',{'notices': notices.items()})

def result(request):
    input_text = request.GET['fulltext']
    word_list = input_text.split()
    
    word_dic = {}
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    return render(request, 'result.html', {'fulltext': input_text, 'total': len(word_list), 'dictionary': word_dic.items()})