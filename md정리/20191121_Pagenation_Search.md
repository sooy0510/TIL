# Pagination & Search

## 1. Pagination

### 1.1. View

- `dir(articles)`

  ['__abstractmethods__', '__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', 'count', 'end_index', '`has_next`', 'has_other_pages', '`has_previous`', 'index', 'next_page_number', 'number', 'object_list', 'paginator', 'previous_page_number', 'start_index']

- `articles.paginator`

  ['__class__', '__delattr__', '__dict__', '`dir`', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_object_list_is_ordered', '_`get_page`', 'allow_empty_first_page', 'count', 'get_page',
  'num_pages', 'object_list', 'orphans', 'page', '`page_range`', 'per_page', 'validate_number']

<br>

- `Paginator(전체 리스트, 보여줄 갯수)` : 한 페이지에 보여줄 게시물 갯수를 설정

- `paginator.get_page(page) ` : index.html에서 페이지 숫자를 클릭했을 때 , 해당하는 페이지 숫자를 인자로 받고 해당 page에 해당하는 article만 가져온다

  ```python
  # articles/views.py
  
  from django.core.paginator import Paginator
  
  def index(request):
    articles = Article.objects.all()
  
    # 1. articles를 Paginator에 넣기
    # - Paginator(전체 리스트, 보여줄 갯수)
    paginator = Paginator(articles, 2)
    # 2. 사용자가 요청한 page 가져오기
    page = request.GET.get('page')
    # 3. 해당하는 page의 article만 가져오기
    articles = paginator.get_page(page)
      
    print(dir(articles))
    print(dir(articles.paginator))
  
    context = {
      'articles':articles,
    }
    return render(request, 'articles/index.html',context)
  ```

<br>

<br>

### 1.2 Template

- dfd

  ```django
  <!-- articles/index.html -->
  
  <nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
    <!-- 이전 페이지가 있을 경우 -->
      {% if articles.has_previous %}
      <li class="page-item">
        <a class="page-link" href="{% url 'articles:index' %}?page={{ articles.previous_page_number }}" tabindex="-1" aria-disabled="true">◀</a>
      </li>
      {% endif %}
  
      <!-- 페이지 버튼 -->
      {% for num in articles.paginator.page_range %}
      <li class="page-item">
        <a class="page-link" href="{% url 'articles:index' %}?page={{ num }}">{{ num }}</a>
      </li>
      {% endfor %}
      <!-- 다음 페이지 있으면 Next 버튼 출력 -->
      {% if articles.has_next %}
      <li class="page-item">
        <a class="page-link" href="{% url 'articles:index' %}?page={{ articles.next_page_number }}">▶</a>
      </li>
      {% endif %}
    </ul>
  </nav>
  ```

  







<br>

<br>

<br>

## 2. Search

