# CRUD_practice
It's a simple CRUD app using Django framework for Python. For practice DRF and CRUD with Django



| 번호          | 할 일                                                        |
| ------------- | ------------------------------------------------------------ |
| backend - 001 | 장고 생성 및 사용할 앱 생성(account, community)              |
| backend - 002 | 데이터베이스 모델 작성                                       |
| backend - 003 | 유저 기능 테스트 작성                                        |
| backend - 004 | 유저 기능 작성 (로그인, 로그아웃, 회원가입)                  |
| backend - 005 | 커뮤니티 기능 테스트 작성                                    |
| backend - 006 | 커뮤니티 기능 작성 (글 조회, 작성, 수정, 삭제)               |
| backend - 007 | 글 수정 및 삭제에 대한 권한 확인 코드 작성 (작성자만 수정 삭제가 가능하도록) |
| backend - 008 | 일반적인 게시글에 필요한 추가 기능 삽입 (페이지네이션, 검색) |

### API 목록
  ##### (POST) account/login   | 로그인
  ##### (POST) account/signup  | 회원가입
  ##### (GET) community        | 게시판 조회
  ##### (POST) community       | 게시글 작성
  ##### (GET) community/<pk>   | 게시글 디테일 조회
  ##### (PUT) community/<pk>   | 게시글 수정
  ##### (DELETE) community/<pk>| 게시글 삭제
  

### 기능 TEST
  python manage.py test
  - 로그인, 회원가입
  - 게시글 조회 수정 삭제
