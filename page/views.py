from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# TODO: change to class-based views


fake_posts = [
    {
        'title': 'Why I made this site?',
        'content': '''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vel tincidunt nisl. Vestibulum et nulla massa. Fusce molestie sed nunc in efficitur. Donec posuere vulputate tempus. Cras nec imperdiet leo. Pellentesque facilisis mauris quis nunc aliquet ultricies. Phasellus vel eleifend ligula, id laoreet neque. Morbi consectetur ante tellus, in placerat enim porta vitae. Nullam convallis, tortor sit amet semper maximus, tortor est tempus lacus, et sodales felis purus non felis. Phasellus non luctus dui.
        Nam diam felis, elementum eu justo vitae, ornare elementum dui. Nulla mattis vehicula mi sed tincidunt. Ut fringilla semper massa at rhoncus. Phasellus turpis ante, egestas sed cursus sit amet, placerat nec est. Nulla nec odio in turpis tempus fermentum. Cras et metus velit. Ut eget accumsan urna, vitae tempor arcu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        ''',
        'author': 'Igor Kuivjogi Fernandes',
        'date': date(2021, 5, 2),
        'tags': ['personal', 'lifestyle']
    },
    {
        'title': 'How to create calculated fields in Django Models',
        'content': '''
        Proin hendrerit justo ac facilisis egestas. Donec convallis turpis eu eros hendrerit, ut commodo lorem luctus. Vivamus malesuada auctor sapien, et faucibus dui malesuada ac. In a purus eget lorem porttitor commodo. Suspendisse convallis velit lacinia ante facilisis lacinia.
        Proin ultricies lorem ut fringilla tincidunt. Donec congue accumsan tortor, vel luctus nibh scelerisque vel. Aliquam congue dictum tellus faucibus ullamcorper. Proin efficitur, ante eu ornare ornare, mi elit eleifend enim, et cursus purus neque quis quam..
        ''',
        'author': 'Igor Kuivjogi Fernandes',
        'date': date(2021, 6, 14),
        'tags': ['django', 'python', 'web']
    },
    {
        'title': 'Have you ever heard of the EAFP principle?',
        'content': '''
        Etiam felis, elementum eu justo vitae, ornare elementum dui. Nulla mattis vehicula mi sed tincidunt. Ut fringilla semper massa at rhoncus. Phasellus turpis ante, egestas sed cursus sit amet, placerat nec est. Nulla nec odio in turpis tempus fermentum. Cras et metus velit. Ut eget accumsan urna, vitae tempor arcu.
        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        ''',
        'author': 'Igor Kuivjogi Fernandes',
        'date': date(2021, 7, 15),
        'tags': ['coding style', 'python']
    }
]


def index(request):
    return render(request, 'page/index.html')


def who_am_i(request):
    return HttpResponse('Who am I?')


def posts(request):
    context = {'posts': fake_posts}
    return render(request, 'page/posts.html', context)


def projects(requests):
    return HttpResponse('Projects')
