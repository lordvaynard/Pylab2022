from django.shortcuts import render

from datetime import datetime

from django.http import HttpResponse


def index(request):
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p><a href="home/empresa">Link</a></p>
        </body>
    </html>
    '''
    return HttpResponse(html)