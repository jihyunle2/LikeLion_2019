---
layout: session
title: 18. Error Page ( CRUD / M:N )
category: 7th
---
세션 18 - prod. 이태훈

## Session Preview

* 본 세션은 한 학기 동안 배웠던 Django Stack을 활용하여 Error가 존재하는 Django Project를 정상적으로 Error-Free 상태로 만들어 가동시키는 것을 목적으로 합니다.

* Error 들은 MTV에 모두 존재하며, 추가적으로 Settings에도 존재합니다.

* 제공된 Error 상태의 Project는 원래 간단한 블로그 형태의 기능을 수행하는 Project 입니다.
사용자는 Home 화면에서 현재까지 작성된 모든 글들을 볼 수 있고, 글쓰기 화면에서 글을 작성할 경우 Home 화면에서 띄워지는 모든 글 리스트에 작성한 글이 추가됩니다.
Home 화면에서 특정 글을 클릭할 경우 해당 글의 자세한 내용이 담긴 화면으로 넘어가며, 글에 달린 댓글들을 확인할 수 있습니다. 또한 해당 화면에서 댓글을 작성할 수도 있습니다. 글에 대한 삭제, 혹은 댓글에 대한 삭제도 이 화면에서 가능합니다.

* 추가 Module은 없습니다. (Ex: Paginator, Text-Cut)

* Error-Free의 조건은 다음과 같습니다.

### 1. Local Server가 제대로 작동해야 한다.

### 2. Home 화면에서 작성된 모든 글의 리스트가 보여야 한다.

### 3. Navigation Bar에서 Write를 클릭하여 글을 작성하고 제대로 Home 화면에 작성된 글이 추가되어야 한다.

### 4. Home 화면에서 특정 글의 제목을 클릭했을 경우 글의 Detail 화면으로 전환되어야 한다.

### 5. Detail 화면에선 클릭했던 글의 제목과 본문이 제대로 출력되어야 한다.

### 6. Detail 화면 하단부에서 작성된 모든 Comment의 리스트가 보여야 한다.

### 7. Detail 화면 하단부에서 Comment를 작성하고 Comment의 리스트에 작성된 Comment가 추가되어야 한다.

### 8. Detail 화면에서 Comment가 정상적으로 삭제되어야 한다. 또한 Comment가 있는 상태에서 정상적으로 글의 수정과 삭제가 가능해야 한다. 글 삭제시 Comment도 함께 삭제되어야 한다.

### 9. Detail 화면에서 클릭했던 글의 삭제가 정상적으로 이루어져야 한다. 또한 글이 삭제될 경우 해당 글에 달려있던 Comment들도 함께 삭제되어야 한다.


## 필요 사항

* MTV + Settings에 모두 Error가 존재하므로 Error-Free 진행의 Test를 진행할 경우 Database와 충돌이 일어날 확률이 높습니다.

* 따라서 Model의 수정을 먼저 할 것을 권유드립니다. Model의 Error를 찾아 수정했다면 꼭 makemigrations와 migrate를 통해 Database와 동기화 해주십시오.

* 혹시 Test 도중 Database와 충돌이 일어났다면 App 폴더 안에 위치해있는 migrations 폴더에서 __init__ 파일을 제외하고 모두 삭제하신 뒤 db.sqlite3 파일을 삭제해 주십시오. 이후 다시 makemigrations와 migrate를 통해 Database 생성 및 동기화를 진행하시면 됩니다.

## Hint

* 15분에 한번씩 각 세션 참가자에게 Error에 대해 질문할 수 있는 기회를 드립니다. Error 이외의 Project 그 자체에 대한 질문은 상시 가능합니다.