# payhere

### 가계부 관리
### 구현 기능
1. 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다. 
2. 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다. 
3. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다. 
    1. 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다. 
    2. 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
    3. 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다. 
    4. 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다. 
    5. 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
    
로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리

### branch 
* main
    *  feature/users
    *  feature/accountbooks
### 테스트케이스
<details>
<summary>users</summary>
<div markdown="1">       

1. 회원가입 성공
2. 회원가입 실패(이메일 중복)
3. 회원가입 실패(이메일 빈칸)
4. 회원가입 실패(이메일 형식)

</div>
</details>

<details>
<summary>accountbook</summary>
<div markdown="1">       

<details>
<summary>1. 가계부 리스트 조회</summary>
<div markdown="1">       

1. 가계부 리스트 조회 성공
2. 가계부 리스트 조회 실패(비로그인)

</div>
</details>

<details>
<summary>2. 가계부 작성</summary>
<div markdown="1">       

1. 가계부 작성 성공
2. 가계부 작성 실패(비로그인)
3. 가계부 작성 실패(금액 빈칸)
4. 가계부 작성 실패(메모 빈칸)
5. 가계부 작성 실패(accountbook_data 빈칸)

</div>
</details>
<details>
<summary>3. 가계부 상세 조회</summary>
<div markdown="1">       

1. 가계부 상세 조회 성공
2. 가계부 상세 조회 실패(비로그인)
3. 가계부 상세 조회 실패(본인이 아닐시)

</div>
</details>

<details>
<summary>4. 가계부 수정</summary>
<div markdown="1">       

1. 가계부 수정 성공
2. 가계부 수정 실패(비로그인)
3. 가계부 수정 실패(작성자와 수정고객 불일치)
4. 가계부 수정 실패(금액 빈칸)
5. 가계부 수정 실패(메모 빈칸)
6. 가계부 수정 실패(accountbook data 빈칸)
</div>
</details>

<details>
<summary>5. 가계부 삭제</summary>
<div markdown="1">       

1. 가계부 삭제 성공
2. 가계부 삭제 실패(비로그인)
3. 가계부 삭제 실패(작성자와 수정고객 불일치)

</div>
</details>

</div>
</details>

### API
![캡처](https://user-images.githubusercontent.com/96408893/216773467-875f71d0-cc10-4e0c-8498-a70c9f018575.PNG)
![dddd](https://user-images.githubusercontent.com/96408893/216773518-5ff0d517-422e-473a-9e4b-b24f9cc82a87.PNG)

