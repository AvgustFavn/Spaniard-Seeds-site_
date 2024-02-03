from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from weed_site.models import *
from weed_site.models import User
from weed_site.back import LoginForm, insert_values
from weed_proj.settings import BASE_DIR
from weed_site.back import handle_uploaded_file
from weed_site.back import get_user_id_from_session
from weed_site.back import is_admin
from django.db.models import Q


def home(request):
    # insert_values()
    if request.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    prods = Products.objects.all()[:3]
    revs = Reviews.objects.all()[:10]
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    arts = Article.objects.all()[:2]
    for art in arts:
        art.text = art.text[:300]

    return render(request, 'index.html',
                  context={'prods': prods, 'revs': revs, 'inn': inn, 'admin': admin, "arts": arts})


def search(request, word, page=None):
    if page and page > 1:
        page -= 1
        prods = Products.objects.filter(Q(name__contains=word) | Q(description__contains=word)).all()[
                page * 10:page * 10 + 10]
        count_rows = prods.count()
        range_ = range(1, int(count_rows / 10) + 2)
        return render(request, 'page1.html',
                      context={'prods': prods, 'count_rows': count_rows, 'range_': range_})
    else:
        prods = Products.objects.filter(Q(name__contains=word) | Q(description__contains=word)).all()[:10]
        count_rows = prods.count()
        range_ = range(1, int(count_rows / 10) + 2)
        return render(request, 'page1.html',
                      context={'prods': prods, 'count_rows': count_rows, 'range_': range_})


def catalog(request, page=None, word=None):
    if request.COOKIES.get('sessionid', None):
        inn = True
        user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
        admin = is_admin(user_id)
    else:
        admin = None
        inn = False
    if request.method == 'GET':
        if word:
            if word == 'auto':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Автоцветущие').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods,
                                           'category': f'Автоцветущие сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Автоцветущие').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Автоцветущие сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})

            elif word == 'photo':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Фотопериодные').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods,
                                           'category': f'Фотопериодные сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Фотопериодные').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Фотопериодные сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})

            elif word == 'sativa':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Сатива').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Сативы сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Сатива').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Сативы сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})

            elif word == 'indicka':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Индика').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Индика сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Индика').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Индика сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
            elif word == 'medical':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Медицинские').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods,
                                           'category': f'Медицинские сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Медицинские').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Медицинские сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})

            elif word == 'beginners':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Для новичков').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods,
                                           'category': f'Для новичков сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Для новичков').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Для новичков сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
            elif word == 'short':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Невысокие').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods,
                                           'category': f'Невысокие сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Невысокие').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Невысокие сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})

            elif word == 'nosense':
                if page and page > 1:
                    page -= 1
                    cat = Category.objects.filter(name='Слабопахнущие').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[page * 10:page * 10 + 10]
                    count_rows = Products.objects.all().count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods,
                                           'category': f'Слабопахнущие сорта, страница # {page}',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})
                else:
                    cat = Category.objects.filter(name='Слабопахнущие').first()
                    prods = Products.objects.filter(category__contains=[cat.id]).all()[:10]
                    count_rows = prods.count()
                    range_ = range(1, int(count_rows / 10) + 2)
                    return render(request, 'page1.html',
                                  context={'inn': inn, 'prods': prods, 'category': f'Слабопахнущие сорта',
                                           'count_rows': count_rows, 'range_': range_, 'admin': admin})

        elif page and page > 1:
            page -= 1
            prods = Products.objects.all()[page * 10:page * 10 + 10]
            count_rows = Products.objects.all().count()
            range_ = range(1, int(count_rows / 10) + 2)
            print(range_)
            return render(request, 'page1.html',
                          context={'inn': inn, 'prods': prods, 'category': f'Все товары, страница # {page}',
                                   'count_rows': count_rows, 'range_': range_, 'admin': admin})

        else:
            prods = Products.objects.all()[:10]
            count_rows = Products.objects.all().count()
            range_ = range(1, int(count_rows / 10) + 2)
            print(range_, ' страниц', f'{count_rows} товаров')
            return render(request, 'page1.html',
                          context={'inn': inn, "prods": prods, 'category': 'Все товары', 'count_rows': count_rows,
                                   'range_': range_, 'admin': admin})

    else:
        word = request.POST.get('text')
        prods = Products.objects.filter(Q(name__icontains=word) | Q(description__icontains=word)).all()
        return render(request, 'page1.html',
                      context={'prods': prods, "category": 'По поиску...'})


def sales_delivery(request):
    if request.COOKIES.get('sessionid', None):
        inn = True
        user_id = get_user_id_from_session(request.COOKIES['sessionid'])
        admin = is_admin(user_id)
    else:
        inn = False
        admin = None
    return render(request, 'page3.html', context={'inn': inn, 'admin': admin})


def legal(request):
    if request.COOKIES.get('sessionid', None):
        inn = True
        user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
        admin = is_admin(user_id)
    else:
        inn = False
        admin = None
    return render(request, 'page4.html', context={'inn': inn, 'admin': admin})


def reviews(request):
    revs = Reviews.objects.all()
    if request.COOKIES.get('sessionid', None):
        inn = True
        user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
        admin = is_admin(user_id)
    else:
        inn = False
        admin = None
    return render(request, 'page5.html', context={'revs': revs, 'inn': inn, 'admin': admin})


def del_review(request, rev_id):
    if request.COOKIES.get('sessionid', None):
        inn = True
        user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
        admin = is_admin(user_id)
        if admin:
            rev = Reviews.objects.get(id=rev_id)
            rev.delete()
            return redirect('/reviews')
    return redirect('/reviews')


def admin(request):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    print(user_id)
    admin = is_admin(int(user_id))
    if admin:
        if request.COOKIES.get('sessionid', None):
            inn = True
        else:
            inn = False
        return render(request, 'page11.html', context={'inn': inn})
    else:
        return redirect('/')


def basket(request):
    if request.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    if request.method == 'GET':
        session_id = request.COOKIES.get('sessionid', None)
        user_id = get_user_id_from_session(session_id)
        products = Basket.objects.filter(user_id=user_id)
        full_price = 0.0
        prods = []
        for b in products:
            prod = Products.objects.get(id=b.prod_id)
            prod.ccount = b.count
            prods.append(prod)
            full_price += prod.price * b.count

        return render(request, 'page6.html', context={'prods': prods, 'full_price': full_price, 'inn': inn})
    elif request.method == 'POST':
        session_id = request.COOKIES.get('sessionid', None)
        user_id = get_user_id_from_session(session_id)
        if user_id:
            user = User.objects.get(id=user_id)
            products = Basket.objects.filter(user_id=user_id)
            full_price = 0.0
            prods = {}
            for b in products:
                prod = Products.objects.get(id=b.prod_id)
                full_price += prod.price * b.count
                prods[b.prod_id] = b.count

            products.delete()
            order = Orders.objects.create(user_id=user_id, email=user.email, prods_id=prods, final_price=full_price)
            order.save()
            return redirect(f'/confirm_order/{order.id}')
        else:
            return redirect('/login')


def confirm_order(request, order_id):
    if request.method == 'GET':
        if request.COOKIES.get('sessionid', None):
            inn = True
        else:
            inn = False
        return render(request, 'page7.html', context={'order_id': order_id, 'inn': inn})
    elif request.method == 'POST':
        order = Orders.objects.get(id=order_id)
        name = request.POST.get('name')
        city = request.POST.get('city')
        tg = request.POST.get('tg')
        message = request.POST.get('message')
        pay = request.POST.get('pay')
        post = request.POST.get('post')
        phone = request.POST.get('phone')
        addres = request.POST.get('addres')

        for prod_id, co in order.prods_id.items():
            product = Products.objects.get(id=prod_id)
            product.count -= co
            product.save()

        order.name = name
        order.city = city
        order.pay = pay
        order.post = post
        order.phone = phone
        order.address = addres
        order.tg = tg
        order.message = message
        order.status = 'Ожидание'
        order.save()
        return redirect(f'/profile')  # Пересылка на страницу юзера


def reg_view(request):
    if request.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('name')
        user = User.objects.filter(email=email).first()
        if not user:
            hash_password = make_password(password)
            login = email[:email.find('@')]
            user = User.objects.create(email=email, login=login, password_hash=hash_password)
            user.save()
            return redirect(reverse_lazy('login'))
        else:
            return render(request, 'page9.html', context={'error': 'Пользователь с таким email уже существует'})
    elif request.method == 'GET':
        if request.COOKIES.get('sessionid', None):
            return redirect(reverse_lazy('profile'))
        else:
            return render(request, 'page9.html', context={'inn': inn})


def login_view(request):
    if request.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if not user:
            return redirect(reverse_lazy('reg'))
        else:
            if check_password(password, user.password_hash):
                login(request, user)
                return redirect(reverse_lazy('profile'))
            else:
                return render(request, 'page8.html', context={'inn': inn, 'error': 'Пароль не совпадает'})
    elif request.method == 'GET':
        if request.COOKIES.get('sessionid', None):
            return redirect(reverse_lazy('profile'))
        else:
            return render(request, 'page8.html', context={'inn': inn})


def profile(request):
    if request.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    if request.COOKIES.get('sessionid', None):
        session_id = request.COOKIES.get('sessionid', None)
        user_id = get_user_id_from_session(session_id)
        orders = Orders.objects.filter(user_id=user_id)

        for o in orders:
            prods_dict = {}
            if o.prods_dict:
                continue
            else:
                for p in o.prods_id:
                    try:
                        prod = Products.objects.get(id=int(p))
                        prods_dict[p] = prod.name
                    except:
                        pass
                o.prods_dict = prods_dict
                o.save()
        return render(request, 'page10.html', context={'orders': orders, 'inn': True})
    else:
        return redirect(reverse_lazy('login'))


def add_product(request):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        inn = True
        if request.COOKIES.get('sessionid', None):  # Проверка на админ добавить!!
            if request.method == 'GET':
                cats = Category.objects.all()
                print(cats)
                return render(request, 'page12.html', context={'cats': cats, 'inn': inn})
            elif request.method == 'POST':
                name = request.POST.get('name')
                price = request.POST.get('price')
                files = request.FILES.getlist('files')
                files_arr = []
                for uploaded_file in files:
                    # try:
                    saved_file_name = handle_uploaded_file(uploaded_file, f'{BASE_DIR}/static/assets/images')
                    files_arr.append(f'/assets/images/{saved_file_name}')
                # except:
                #     pass
                cat_id = int(request.POST.get('select'))
                cat_id_sec = int(request.POST.get('select2'))
                cat_id_thr = int(request.POST.get('select3'))
                cats = []
                if cat_id != 0:
                    cats.append(cat_id)
                if cat_id_sec != 0:
                    cats.append(cat_id_sec)
                if cat_id_thr != 0:
                    cats.append(cat_id_thr)
                descr = request.POST.get('descr')
                count = request.POST.get('count')
                count_pack = request.POST.get('count_pack')
                if count_pack:
                    prod = Products.objects.create(name=name, price=float(price), description=descr, pics=files_arr,
                                                   category=cats, count=int(count), count_pack=int(count_pack))
                else:
                    prod = Products.objects.create(name=name, price=float(price), description=descr, pics=files_arr,
                                                   category=cats, count=int(count), count_pack=None)
                prod.save()
                return redirect(reverse_lazy('catalog'))
        else:
            return redirect(reverse_lazy('catalog'))


def add_basket(request, prod_id):
    if request.method == 'POST':
        session_id = request.COOKIES.get('sessionid', None)
        user_id = get_user_id_from_session(session_id)
        try:
            count = int(request.POST.get("select", None))
        except:
            count = 1

        if user_id:
            bas = Basket.objects.filter(user_id=user_id, prod_id=prod_id).first()
            if bas:
                bas.count += count
                bas.save()
            else:
                Basket.objects.create(user_id=user_id, prod_id=prod_id, count=count)
            return redirect(f'/product/{prod_id}')

        else:
            return redirect(reverse_lazy('login'))


def product(request, prod_id):
    if request.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    if request.method == 'GET':
        try:
            prod = Products.objects.get(id=prod_id)
            rait = Reviews.objects.filter(prod_id=prod_id).all()
            middle_rait = 0
            for r in rait:
                middle_rait += r.rating
            if len(rait) == 0 or middle_rait == 0:
                middle_rait = 0
            else:
                middle_rait = int(middle_rait / len(rait))

            session_id = request.COOKIES.get('sessionid', None)
            user_id = get_user_id_from_session(session_id)
            orders = Orders.objects.filter(user_id=user_id).all()
            ok = False
            for o in orders:
                for k in o.prods_id.keys():
                    if int(k) == int(prod_id):
                        ok = True
                        break

            print(ok)
            user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
            admin = is_admin(user_id)
            return render(request, 'page13.html',
                          context={'prod': prod, 'rait': rait, 'middle_rait': range(middle_rait), 'ok': ok, 'inn': inn,
                                   "admin": admin, "count": range(1, 20)})
        except:
            return redirect(reverse_lazy('catalog'))

    elif request.method == 'POST':
        session_id = request.COOKIES.get('sessionid', None)
        user_id = get_user_id_from_session(session_id)
        user = User.objects.get(id=user_id)
        orders = Orders.objects.filter(user_id=user_id).all()
        ok = False
        for o in orders:
            for k in o.prods_id.keys():
                if int(k) == int(prod_id):
                    ok = True
                    break
        print(ok)
        if ok:
            prod = Products.objects.get(id=prod_id)
            text = request.POST.get('text')
            rating = request.POST.get('rating')
            print(text)
            print(rating)
            rev = Reviews.objects.create(user_id=user_id, user_name=user.login, prod_id=prod_id, prod_name=prod.name,
                                         comment=text, rating=rating)
            rev.save()
            return redirect(f'/product/{prod_id}')
        else:
            return redirect(reverse_lazy('login'))


def del_basket(request, prod_id):
    if request.method == 'GET':
        session_id = request.COOKIES.get('sessionid', None)
        user_id = get_user_id_from_session(session_id)
        if user_id:
            bas = Basket.objects.filter(user_id=user_id, prod_id=prod_id).first()
            if bas:
                if bas.count > 1:
                    bas.count -= 1
                    bas.save()
                else:
                    bas.delete()
                    bas.save()

            return redirect('/catalog')
        else:
            return redirect(reverse_lazy('login'))


def del_order(request, prod_id):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        order = Orders.objects.filter(id=int(prod_id)).first()
        order.delete()
        return redirect('/all_orders')
    else:
        return redirect(reverse_lazy('login'))


def update_product(request, prod_id):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        if request.method == 'GET':
            prod = Products.objects.get(id=prod_id)
            cats = Category.objects.all()
            return render(request, 'update.html', {'p': prod, "cats": cats})
        else:
            prod = Products.objects.get(id=prod_id)
            name = request.POST.get('name')
            if name != prod.name:
                prod.name = name
            price = request.POST.get('price')
            if float(price) != prod.price:
                prod.price = float(price)

            files = request.FILES.getlist('files')
            files_arr = []
            for uploaded_file in files:
                try:
                    saved_file_name = handle_uploaded_file(uploaded_file, f'{BASE_DIR}/static/assets/images')
                    files_arr.append(f'/assets/images/{saved_file_name}')
                except:
                    pass

            if files_arr:
                prod.pics = files_arr
            cat_id = int(request.POST.get('select'))
            cat_id_sec = int(request.POST.get('select2'))
            cat_id_thr = int(request.POST.get('select3'))
            cats = []
            if cat_id != 0:
                cats.append(cat_id)
            if cat_id_sec != 0:
                cats.append(cat_id_sec)
            if cat_id_thr != 0:
                cats.append(cat_id_thr)

            if cats != prod.category:
                prod.category = cats

            descr = request.POST.get('descr')
            if descr != prod.description:
                prod.description = descr
            count = request.POST.get('count')
            if count != prod.count:
                prod.count = int(count)
            count_pack = request.POST.get('count_pack')
            if count_pack != prod.count_pack:
                prod.count_pack = int(count_pack)

            prod.save()
            return redirect(f'/product/{prod_id}')
    else:
        return redirect(f'/product/{prod_id}')


def delete_product(request, prod_id):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        product = Products.objects.get(id=prod_id)
        product.delete()
        return redirect(reverse_lazy('catalog'))


def admins_list(request):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        inn = True
        if request.COOKIES.get('sessionid', None):
            if request.method == 'GET':
                session_id = request.COOKIES.get('sessionid', None)
                user_id = get_user_id_from_session(session_id)
                admins = Admins.objects.all()
                adm = {}
                for a in admins:
                    user = User.objects.get(id=a.user_id)
                    adm[user.email] = a.user_id
                return render(request, 'page14.html', context={'admins': adm, 'inn': inn})
            else:
                email = request.POST.get('email')
                try:
                    user = User.objects.get(email=email)
                    adm = Admins.objects.create(user_id=user.id)
                    adm.save()
                except:
                    pass
                return redirect('/admins_list')

        else:
            return redirect(reverse_lazy('login'))
    else:
        return redirect(reverse_lazy('login'))


def delete_admin(request, adm_id):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        if request.method == 'GET':
            session_id = request.COOKIES.get('sessionid', None)
            user_id = get_user_id_from_session(session_id)
            adm = Admins.objects.filter(user_id=int(adm_id)).first()
            adm.delete()
            return redirect('/admins_list')
    else:
        return redirect(reverse_lazy('login'))


def all_orders(request):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        orders = Orders.objects.all()
        for o in orders:
            prods_dict = {}
            if o.prods_dict:
                continue
            else:
                for p in o.prods_id:
                    try:
                        prod = Products.objects.get(id=int(p))
                        prods_dict[p] = prod.name
                    except:
                        pass
                o.prods_dict = prods_dict
                o.save()
        return render(request, 'page15.html', context={'orders': orders})
    else:
        return redirect(reverse_lazy('login'))


def change_order(request, order_id):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        if request.method == 'GET':
            order = Orders.objects.get(id=order_id)
            return render(request, 'page16.html', context={'order': order})
        else:
            order = Orders.objects.get(id=order_id)
            status = request.POST.get('status')
            message = request.POST.get('message')
            order.status = status
            if order.admin_mess != message:
                order.admin_mess = message
            order.save()
            return redirect('/all_orders')
    else:
        return redirect(reverse_lazy('login'))


def create_article(request):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        if request.method == 'GET':
            return render(request, 'page18.html')
        else:
            title = request.POST.get('title')
            text = request.POST.get('article')
            files = request.FILES.getlist('files')
            print(files)
            files_arr = []
            if files:
                for uploaded_file in files:
                    saved_file_name = handle_uploaded_file(uploaded_file, f'{BASE_DIR}/static/assets/images')
                    files_arr.append(f'/assets/images/{saved_file_name}')

            article = Article.objects.create(title=title, text=text, pics=files_arr)
            article.save()
            return redirect('/all_articles')
    else:
        return redirect('/all_articles')


def all_articles(requests, page=None):
    if requests.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    if page and page > 1:
        arts = Article.objects.all()[page * 10: page * 10 + 10]
        for a in arts:
            try:
                a.text = a.text[:350]
            except:
                pass
        count_rows = Article.objects.all().count()
        range_ = range(1, count_rows)
        return render(requests, 'page17.html',
                      context={'arts': arts, 'count_rows': int(count_rows), "range_": range_, 'inn': inn})
    else:
        arts = Article.objects.all()[:11]
        for a in arts:
            try:
                a.text = a.text[:350]
            except:
                pass
        count_rows = Article.objects.all().count()
        range_ = range(1, count_rows)
        return render(requests, 'page17.html',
                      context={'arts': arts, 'count_rows': count_rows, "range_": range_, 'inn': inn})


def article(requests, art_id):
    if requests.COOKIES.get('sessionid', None):
        inn = True
    else:
        inn = False
    art = Article.objects.filter(id=art_id).first()
    user_id = get_user_id_from_session(requests.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if art:
        print(art.pics)
        if art.pics:
            art.first = art.pics[0]
            del art.pics[0]
        else:
            art.first = None
        return render(requests, 'page19.html',
                      context={'art': art, 'range_': range(1, len(art.pics) + 1), "admin": admin, 'inn': inn})
    else:
        return redirect('/all_articles')


def del_article(requests, art_id):
    user_id = get_user_id_from_session(requests.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        art = Article.objects.filter(id=art_id).first()
        art.delete()
        return redirect('/all_articles')

    else:
        return redirect(reverse_lazy('login'))


def change_article(request, art_id):
    user_id = get_user_id_from_session(request.COOKIES.get('sessionid', None))
    admin = is_admin(user_id)
    if admin:
        if request.method == 'GET':
            article = Article.objects.filter(id=art_id).first()
            return render(request, 'page18.html', context={'art': article})
        else:
            title = request.POST.get('title')
            text = request.POST.get('article')
            files = request.FILES.getlist('files')
            files_arr = []
            if files:
                for uploaded_file in files:
                    saved_file_name = handle_uploaded_file(uploaded_file, f'{BASE_DIR}/static/assets/images')
                    files_arr.append(f'/assets/images/{saved_file_name}')

                article = Article.objects.filter(id=art_id).first()
                article.title = title
                article.text = text
                article.pics = files_arr
            else:
                article = Article.objects.filter(id=art_id).first()
                article.title = title
                article.text = text
            article.save()
            return redirect('/all_articles')
    else:
        return redirect('/all_articles')
