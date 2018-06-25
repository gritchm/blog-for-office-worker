from django.db import models

# Create your models here.

class HashTag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )
    title= models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
        )
    def __str__(self):
        return self.title


    hashtag = models.ManyToManyField(HashTag)

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name="article_comments",
        on_delete=models.CASCADE
        )
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

# Article 제목이랑 content 을 쓰는게 좋을 것으로 보임
# 함수는 format 사용
# self.article.title 은 아티클 클래스에 먼저들어가서 그다음 title 접근

    def __str__(self):
        return "{}에 댓글: {}".format(self.article.title, self.content)




# class ArticleHasHashTag(models.Model):
#     article = models.ForeignKey(Article)
#     hashtag = models.ForeignKey(HashTag)
