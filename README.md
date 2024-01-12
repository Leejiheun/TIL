# GIT

# GIT:분산 버전 관리
## (변화를 기록하고 추적하는 것)
- 코드의 버전 관리
- 개발되어 온 과정
- 변경이력을 기록
- 원본 누적해서 기록 X
- 협업을 원활하게 하는 도구(분산식이기 때문)

# GIT의 세가지 영역 부분
1. Working directory : 눈에 보이는 영역.
2. Staging area : 변경사항발생기록이됨. 눈으로 확인은 안됨. 다음 버전 포함 될 파일들을 선택적으로 저장하거나 제외하는 역할.
3. Repository : 최종 버전과 변경 이력이 기록됨.

- commit : 버전 이력 (과거로 부터 지금까지의 변경 사항, 원본은 기록 안됨)

# 명령
- git init : 내가 깃의 버전관리를 시작할 때 처음 영역 설정하는 것! 한 번만 하면 됨. 로컬 저장소 설정한다.(초기화)
  
- git status : 빨간거working dir 초 stage올렸고 working tree비었는지 확인(자주 확이해보기)
- git add : 변경사항 올리는거. 워킹디렉토리에서 스테이지로 올리는 명령
- git commit -m "": staging area에 있는거 최종 저장소에 등록하는거. 이력 남기게 됨.
- git log : commit을 두 번하게 되면 두번 쌓인게 나타남
- git config :
- git add . : 전체 변경사항을 스테이지로 올리는거 (new fule이 여러개일 때)
- q : 간혹 터미널창이 안될 때
- cd .. : 했는데 master이 뜨면 -> **git 저장소 안에 또 다른 git저장소는 존재할 수 없다.** -> git init을 진행한 하위 디렉토리의 하위 디렉토리 그 어디에서도 git init을 진행하면 안됨. git의 저장소를 나눠서 잘 관리해야함
- git log --oneline : commit당 한 줄 씩 보겠다
- git config --global = git config --list :

- ls -a : git init을 하는 순간 .git 숨김 폴더가 생김 -> 지우면 됨.
- rm -r .git : .git 파일이 없어짐 / 과거에 쌓아왔던 역사는 없어질 수 있음.

# 온라인(원격) <-> 로컬(지역) <-> 글로벌(전역)
로컬 저장소 하나당 원격 저장소 하나.

# 원격저장소(Remote Repository)
여러 개발자가 협업하고 공유할 수 있는 저장 공간 원격 저장소에는 commit을 올린다!
ex) 깃허브, 깃랩(기업이 계약해서 대규모로 프라이빗하게 사용), 비트버킷

git vs github : 각각의 서비스 이름이다.
깃헙 레퍼지토리와 로컬 레퍼지토리가 remote.
- **git remote** add origin remote_repo_url : 로컬 저장소에 원격 저장소 주소 추가. 등록과정이 필요하다. origin은 추가하는 원격 저장소 별칭이다.
- git remote -v : 별칭(오리진) 실제주소 두줄이 한 세트. 연결
원격저장소에 올리는 명령을 push
내려받는건 pull or clone(복제) : pull은 변경사항만큼만 내려받는거 clone은 전체다 받는거_새로운 컴퓨터에 받을 때
- **git push** -u origin master : **원격저장소에 commit이 업로드**
-> commit 이력이 없다면 push 할 수 없다
- git pull origin master : 원격 저자소의 변경사항만 받아옴(업데이트_복제가 아님)
- git clone remote_repo_url : 원격저장소 주소를 적어야함(다운로드 느낌) -> clone으로 받은 프로젝트는 이미 git init이 되어 있음 git remote add할 필요도 없음
- 
gitignore : 깃에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는데 사용되는 텍스트 파일, 공유하지 않아야하는 것들도 존재하기 때문
gitignore.io : 

깃허브 
: TIL(레퍼지토리를 TIL로)을 통해 내가 학습한 것을 기록
->