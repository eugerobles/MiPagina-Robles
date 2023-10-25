from django.urls import path
from inicio.views import inicio, crear_curso


    
urlpatterns= [   
    path ('', inicio, name='inicio'),
    path (crear_blogcafe/<str.nombre>/<str.apellido>, blog_cafe),
    path ('cursoscafe/crear', crear_curso, name=crearcurso)
]
