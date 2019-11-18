# 0. 사전준비

## 0.1 `Node.js` 설치

- node.js : javascript를 백엔드에서도 활용할 수 있게 만든것
- Node.js 발표와 동시에 JavaScript가 브라우저 종속적인 언어가 아니라 서버 구축까지 가능해지면서 핫한 언어로 급부상
- Express.js(서버), React.js(프론트), Vue.js(프론트) 등 JavaScript 기반의 수많은 프레임워크, 라이브러리들이 현대 웹 개발 트렌드를 주도하고 있음

- [node.js 공식 홈페이지](https://nodejs.org/ko/)

  - **LTS** Version(안정적)
  - **Windows installer(.msi) 64bit**

- 설치 확인

  ```bash
  $ node -v
  v12.13.0
  ```

<br>

<br>

## 0.2 VSCode Python & JavaScript 인덴팅 설정

- 설정에서 바꿔준 설정속성들이 settings파일에 반영됨

- Preference : Open Settings(JSON)

  ```python
  {
      ...
      "editor.tabSize":2,
      "[python]":{
          "editor.tabSize":4,
      },
      ...
  }
  ```



<br>

<br>

## 0.3 Naming convention

- `lowerCamelCase`
  - 단봉낙타 표기법
  - JavaScript의 기본 표기법
- `UpperCamelCase`
  - 쌍봉낙타 표기법
- `snake_case`
- `kebob-case`



<br>

<br>

## 0.4 Extensions(추천)

- `auto close tag` : 태그를 자동으로 닫아줌
- `rainbow brackets` : 괄호의 색을 mapping
- `indent-rainbow` : 들여쓰기를 색으로 표시

<br>

<br>

<br>

# 1. Variable

### 1.0 var

- hoisting 문제때문에 안씀

<br>

<br>

### 1.1 let(변수)

- 값을 재할당 할 수 있는 변수를 선언하는 키워드

- 변수 선언은 한 번만 할 수 있다

  - 하지만. 할당은 여러번 할 수 있다

    ```python
    
    ```

- 블록 유효 범위(`Block Scope`)를 갖는 지역 변수

<br>

<br>

### 1.2 Const

- 값이 변하지 않는 상수를 선언하는 키워드
  - 상수의 값은 재할당을 통해 바뀔 수 없고, 재선언도 불가능하다
- let과 동일하게 `Block Scope` 을 가진다
- 웬만하면 모든 선언에서 상수를 써야 한다
  - 일단 상수를 사용하고, 값이 바뀌는게 자연스러운 상황이면 그때 변수(let) 로 바꿔서 사용하는 것을 권장한다.