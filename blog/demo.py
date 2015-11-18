from crowix.models import artical

a = artical.objects.all()

for b in a:
    b.title
    