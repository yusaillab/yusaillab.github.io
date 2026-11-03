# SAIL — 영남대학교 AI안전연구소 홈페이지

sail.yu.ac.kr 에서 서비스되는 정적 홈페이지입니다. 서버 프로그램 없이 HTML/CSS/JS만으로 동작합니다.

## 자주 하는 수정
- 공지 올리기: `notices.js` 맨 위에 항목 추가 (파일 안 주석 참고)
- 구성원 수정: `members.js`
- 사진: 저장소에 사진 파일을 올리고 members.js 의 photo 에 파일 이름 적기
- 글·메뉴 수정: `build.py` 안의 내용을 고친 뒤 `python3 build.py` 실행 (HTML이 다시 생성됨)

## 배포
GitHub Pages 로 배포됩니다. main 브랜치에 파일을 올리면(커밋) 1~2분 안에 자동 반영됩니다.
`CNAME` 파일(내용: sail.yu.ac.kr)은 지우지 마세요. 지우면 학교 주소 연결이 풀립니다.
