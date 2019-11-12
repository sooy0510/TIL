# Model Relationships

- 현재 User와 Article의 관계는 `User : Article = 1 : N` 이다
  - [참조] `article.user` : article입장에서 user 1은 보장
  - [역참조] `user.article_set` : user입장에서 article은 없을수도 있다
- 관점을 조금 바꿔서 `User : Article `



- 쿼리 실습

  - 실습데이터

    ```python
    user1 = User.objects.create(name='Kim')
    user2 = User.objects.create(name='Lee')
    article1 = Article.objects.create(title='1글', user=user1)
    article2 = Article.objects.create(title='2글', user=user1)
    article3 = Article.objects.create(title='3글', user=user2)
    c1 = Comment.objects.create(content='1글1댓글', user=user1, article=article1)
    c2 = Comment.objects.create(content='1글2댓글', user=user2, article=article1)
    c3 = Comment.objects.create(content='1글3댓글', user=user1, article=article1)
    c4 = Comment.objects.create(content='1글4댓글', user=user2, article=article1)
    c5 = Comment.objects.create(content='2글1댓글', user=user1, article=article2)
    c6 = Comment.objects.create(content='!1글5댓글', user=user2, article=article1)
    c7 = Comment.objects.create(content='!2글2댓글', user=user2, article=article2)
    ```

    

  1. 1번 사람이 작성한 게시글을 다 가져오기

     ```python
     user1.article_set.all()
     ```

     <br>

  2. 1번 사람이 작성한 모든 게시글에 달린 댓글 가져오기

     ```python
     for article in user1.article_set.all():
         for comment in article.comment_set.all():
             print(comment.content)
     ```

     <br>

     > ![1573537776666](images/1573537776666.png)

     <br>

  3. 2번 댓글을 작성한 사람

     ```python
     c2.user
     ```

     <br>

  4. 2번 댓글을 작성한 사람의 모든 게시글은?

     ```python
     c2.user.article_set.all()
     ```

     <br>

  5. 두번째부터 네번째 댓글 가져오기

     ```python
     article1.comment_set.all()[1:4]
     Out[42]: <QuerySet [<Comment: 1글2댓글>, <Comment: 1글3댓글>, <Comment: 1글4댓글>]>
     
     In [43]: article1.comment_set.all()[1:4].query
     Out[43]: <django.db.models.sql.query.Query at 0x5003630>
     
     In [44]: print(article1.comment_set.all()[1:4].query)
     SELECT "manytoone_comment"."id", "manytoone_comment"."content", "manytoone_comment"."article_id", "manytoone_comment"."user_id" FROM "manytoone_comment" WHERE "manytoone_comment"."article_id" = 1  LIMIT 3 OFFSET 1
     ```

     <br>

  6. 1번글의 두번째 댓글을 작성한 사람의 첫번째 게시물의 작성자의 이름은?

     ```python
     article1.comment_set.all()[1].user.article_set.first().user.name
     ```

     <br>

  7. 1번 댓글의 user 정보만 가져오면

     ```python
     In [49]: Comment.objects.values('user').get(pk=1)
     Out[49]: {'user': 1}
     ```

     <br>

  8. 2번 사람이 작성한 댓글은 pk 내림차순으로 가져오면?

     ```python
     In [54]: user2.comment_set.order_by('-pk')
     Out[54]: <QuerySet [<Comment: !2글2댓글>, <Comment: !1글5댓글>, <Comment: 1글4댓글>, <Comment: 1글2댓글>]>
     ```

     <br>

  9. 제목이 '1글'이라는 게시글을 전부 가져오면?

     - get : 아예 없거나 2개 이상이면 에러 - 유일한 값을 구분할 때 사용
     - filter : 없거나 여러개 있을 때 사용

     ```python
     In [55]: Article.objects.get(title='1글')
     Out[55]: <Article: 1글>
             
     In [56]: Article.objects.filter(title='1글')
     Out[56]: <QuerySet [<Article: 1글>]>
     ```

     

