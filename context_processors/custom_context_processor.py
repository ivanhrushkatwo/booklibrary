from catalog.models import CategoryBook, Book


def category(request):
    category_list = CategoryBook.objects.all()
    return {"category_list": category_list}


def basket_with_goods(request):

    goods = request.session.get('goods')

    return {"goods": goods, "t": str(type(goods))}
