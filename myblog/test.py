from django import template
from django.conf import settings
settings.configure()
from django.template import Template,Context

person={'name':'coderwood','age':'32'}
t=Template('{{ person.name}} is {{ person.age }} years old.')
c=Context({'person':person})    
print t.render(c)
