from my_framework.templater import render

class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


