from catalog.models import CategoryBook


def category(request):
    """
    Return all category in each template
    :param request:
    :return: dict with category
    """
    category_list = CategoryBook.objects.all()
    return {"category_list": category_list}


def basket_with_goods(request):
    goods = request.session.get('goods')
    return {"goods": sum(goods.values())}
