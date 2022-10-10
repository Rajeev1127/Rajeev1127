from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import accesories
from django.urls import reverse


class latest_feed(Feed):
    title="Trends2022"
    link="/drcomments/"
    description="Geat website for trying new Trends"

    def items(self):
        return accesories.objects.all()[:4]

    def item_title(self,item):
        return item.name

    def item_description(self, item):
        return truncatewords (item.desc,20)

    def  item_link(self,items):
        return reverse("home")
