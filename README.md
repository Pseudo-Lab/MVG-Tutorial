# MVG-Tutorial

- 빌드 페이지 : https://pseudo-lab.github.io/MVG-Tutorial
- reference1: https://github.com/Pseudo-Lab/Jupyter-Book-Template
- reference2: https://github.com/Pseudo-Lab/pytorch-guide
- reference3: https://github.com/Pseudo-Lab/SegCrew-Book

## jupyter book build

- init
  - 페이지 작성은 `.md`, `.ipynb` 형식으로 작성

- git clone 

  - ```
    git clone https://github.com/Pseudo-Lab/MVG-Tutorial.git
    ```

- 페이지 작성 파일 이동

  - `MVG-Tutorial/book/docs` 에 위치시킬 것
  - `ch%2d` 형식의 폴더 내에 작성

- `_toc.yml` 변경

  - `MVG-Tutorial/book` 내 `_toc.yml` 파일 변경

  - ```yaml
	format: jb-book
	root: docs/index
	sections:
	- file: docs/ch1/Introduction
	- file: docs/ch2/projective...
    ```

  - 위 코드 참조하여 추가한 페이지 이름 변경

- git commit & push
  - ```
    cd MVG-Tutorial
    git add .
    git commit -a
    git push
    ```
- Jupyter book 설치

  - ```
    pip install -U jupyter-book
    ```

- Jupyter book build

  - ```
    jupyter-book build book/
    ```

  - 변경 내용 push 할 것

  - ```python
    pip install ghp-import
    ghp-import -n -p -f book/_build/html -m "chapter X publishing"
    ```

  - https://pseudo-lab.github.io/pytorch-guide/ 링크 접속
