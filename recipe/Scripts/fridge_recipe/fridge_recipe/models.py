from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient) 
    instructions = models.TextField()  # 조리 방법
    cooking_time = models.IntegerField()  # 조리 시간 (분)
    category = models.CharField(max_length=100)  # 카테고리 (예: 한식, 양식 등)
    views = models.IntegerField(default=0)  # 조회 수
    
class Ingredient(models.Model): # 식재료
    name = models.CharField(max_length=100) # 식자재 이름
    quantity = models.FloatField() # 양
    unit = models.CharField(max_length=50) # 단위(g, ml 등)

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 수정된 부분
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 리뷰 작성 날짜