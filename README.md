# 데이터 분석 자동화 서비스
prompt enginering을 통해 주어진 데이터를 시각화해주는 프로그램입니다!

<h1>Installation</h1>

1. fe 폴더를 다운로드 합니다
2. 퐅더 루트에서 npm install 커멘드 입력을 통해 실행에 필요한 package를 다운도르 합니다
3. npm start로 프로그램을 실행시킵니다 (default port로 3000이 설정되어 있습니다. cors 문제 발생 방지를 위해 포트 변경은 하지 말아주세요)

<h1>How to use</h1>

<img width="491" alt="스크린샷 2023-12-09 오후 4 09 55" src="https://github.com/seo-seoungjun/term_project/assets/79730690/dc740ae6-ae88-4518-a79e-4b24e72c91e5">

1. 사이드 바 네이게이션을 통해 demo 페이지로 이동합니다
2. 원한다면 grammer과 settings 값들을 조정합니다
기본 세팅값은 아래와 같습니다 <br/>
<img width="254" alt="스크린샷 2023-12-09 오후 4 05 16" src="https://github.com/seo-seoungjun/term_project/assets/79730690/ca07548c-b0f2-478a-ba84-f18025318f5e"> <br/>
3. 시각화를 진행할 파일을 선택합니다 (json과 csv파일만 가능)
4. 마지막 칸에 user massage를 입력해줍니다 ex)데이터 시각화 예시 두가지 보여줘
5. 제출 버튼을 눌리면 파일이 제출되고 분석하여 시각화를 진행합니다 (최대 30초 정도 소요됩니다, 분석량에 따라 시간이 길어질 수 있습니다)

<h1>Example</h1>

1. 해당 레포지토리의 root에 있는 cars.csv 파일을 다운로드 합니다 <br/>
2. 아래와 같이 파일을 선택하고 유저 메세지에 데이터 시각화 예시 두가지 보여줘를 입력 후 제출합니다 <br/>
3. 웹페이지의 console에서 제출된 값들을 볼 수 있습니다 <br/>
<img width="384" alt="스크린샷 2023-12-09 오후 4 07 20" src="https://github.com/seo-seoungjun/term_project/assets/79730690/ad9a5700-9093-4b15-87cc-e7b780203b94"> <br/>
4. 분석이 완료 된 이후 console에서 응답 데이터를 볼 수 있습니다 <br/>
<img width="394" alt="스크린샷 2023-12-09 오후 4 07 51" src="https://github.com/seo-seoungjun/term_project/assets/79730690/0a4fedfa-912e-4889-94e7-742eed8973d4"> <br/>
5. console에서 응답 데이터 중 시각화 데이터가 포함된 부분만 따로 볼 수 있습니다 <br/>
<img width="394" alt="스크린샷 2023-12-09 오후 4 08 10" src="https://github.com/seo-seoungjun/term_project/assets/79730690/d7bf3e5f-cbd1-4a68-9663-11fee25252e6"> <br/>
6. 분석이 완료되면 /analytics로 리다이렉트 되며 분석이 완료된 데이터는 캐쉬와 브라우저의 로컬스토리지에 저장됩니다 <br/>
<img width="1071" alt="스크린샷 2023-12-09 오후 4 15 47" src="https://github.com/seo-seoungjun/term_project/assets/79730690/5e7e37fb-3df2-41e2-a73a-2ea1fc9f3624"> <br/>
<img width="1071" alt="스크린샷 2023-12-09 오후 4 16 01" src="https://github.com/seo-seoungjun/term_project/assets/79730690/3c2eb338-055b-48be-8c0b-4e1353d819a7"> <br/>

<h1>license</h1>

MIT license
