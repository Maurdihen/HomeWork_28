import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from HomeWork_28 import settings
from ads.models import Ads, Category
from users.models import User


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related('author').order_by('-price')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        all_ads = []
        for ads in page_obj:
            all_ads.append({
                "id": ads.id,
                "name": ads.name,
                "author_id": ads.author_id,
                "author": ads.author.first_name,
                "price": ads.price,
                "description": ads.description,
                "is_published": ads.is_published,
                "image": str(ads.image) if ads.image else None,
                "category": ads.category.name,
                "category_id": ads.category_id,
            })

        response = {
            "items": all_ads,
            "num_pages": page_obj.paginator.num_pages,
            "total": page_obj.paginator.count,
        }

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category']

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)

        ads_data['author'] = get_object_or_404(User, pk=ads_data['author'])
        ads_data['category'] = get_object_or_404(Category, pk=ads_data['category'])
        ads = Ads.objects.create(**ads_data)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author.first_name,
            "author_id": ads.author_id,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": str(ads.image) if ads.image else None,
            "category": ads.category.name,
            "category_id": ads.category_id,
        })


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except:
            return JsonResponse({"error": "not found"}, status=404)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author_id": ads.author_id,
            "author": ads.author.first_name,
            "price": ads.price,
            "description": ads.description,
            "is_published": ads.is_published,
            "image": str(ads.image) if ads.image else None,
            "category_id": ads.category_id,
            "category": ads.category.name,
        })

@method_decorator(csrf_exempt, name="dispatch")
class AdsUpdateView(UpdateView):
    model = Ads
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ads_data = json.loads(request.body)

        if ads_data["name"] is not None:
            self.object.name = ads_data["name"]
        if ads_data["price"] is not None:
            self.object.price = ads_data["price"]
        if ads_data["description"] is not None:
            self.object.description = ads_data["description"]
        if ads_data["is_published"] is not None:
            self.object.is_published = ads_data["is_published"]

        self.object.author = get_object_or_404(User, pk=ads_data["author"])
        self.object.category = get_object_or_404(Category, pk=ads_data["category"])

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "category": self.object.category.name,
            "image": str(self.object.image.url) if self.object.image else None,
        })

@method_decorator(csrf_exempt, name="dispatch")
class AdsUploadImageView(UpdateView):
    model = Ads
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get("image", None)
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.first_name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "category": self.object.category.name,
            "image": str(self.object.image.url) if self.object.image else None,
        })

@method_decorator(csrf_exempt, name="dispatch")
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

