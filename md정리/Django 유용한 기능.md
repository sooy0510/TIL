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

## 2. Django - extensions

 https://caesiumy.github.io/2019/04/02/vscode-recommended-extensions/ 