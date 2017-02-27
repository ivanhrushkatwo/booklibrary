from catalog.models import CategoryBook


def category(request):
    category_list = CategoryBook.objects.all()
    return {"category_list": category_list}
