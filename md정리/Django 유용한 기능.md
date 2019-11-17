# Django 유용한 기능

## 1. 코드 들여쓰기

- `Alt+Shift+F`

- `Ctrl+Shift+P` => Open Settings(JSON)

  - 다음 코드 추가

  ```python
  # settings.json
  
  ...
  "editor.fontLigatures": true,
  "beautify.language": {  
      "js": {
          "type": ["javascript", "json"],
          "filename": [".jshintrc", ".jsbeautifyrc"]
          // "ext": ["js", "json"]  
          // ^^ to set extensions to be beautified using the javascript beautifier
      },
      "css": ["css", "scss"],
      "html": ["htm", "html", "django-html"]
  },
  ...
  ```




<br>

<br>

## 2. github 이미지 업로드

- 상대경로로 설정(`./images`)  

![1572416700647](../md%EC%A0%95%EB%A6%AC/images/1572416700647.png)

