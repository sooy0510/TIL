# 우리가 만든 template tag
from django import template

register = template.Library()

@register.filter
def hashtag_link(article):
  content = article.content + ' '
  hashtags = article.hashtags.all()

  for hashtag in hashtags:
    # replace(바꿀거, 넣어줄거)
    # 마지막에 공백 안넣어주면 hashtag로 인식을 못함
    content = content.replace(
      hashtag.content+' ',
      f'<a href="/articles/{hashtag.pk}/hashtag/">{hashtag.content}</a> '
    )

  return content