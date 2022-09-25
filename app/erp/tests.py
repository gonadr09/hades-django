from config.wsgi import *
from .models import Type

# Create your tests here.

# Listar
query = Type.objects.all()
print(query)

# Insertar
i = Type()
i.name = "Accionista"
i.save()

# Editar
e = Type.objects.get(id=1)
e.name = "Presidente"
e.save()

# Eliminar
d = Type.objects.get(id=1)
d.delete()

# Otros
obj1 = Type.objects.filter(name__contains='terry')
obj2 = Type.objects.filter(name_endswith='a').exclude(id=5)
obj3 = Type.objects.filter(name_startwith='a').count()