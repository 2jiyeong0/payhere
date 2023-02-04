from rest_framework.test import APITestCase
from django.urls import reverse

from users.models import User
from accountbooks.models import Accountbook

class AccountbookViewAPIViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {"email": "test@test.com", "password": "password"}
        cls.user = User.objects.create_user("test@test.com", "password")
        cls.accountbook_data = {"amount": "10000", "content": "some content"}
    def setUp(self):
        self.access_token = self.client.post(reverse("token_obtain_pair"), self.user_data).data["access"]

    ### 가계부 리스트 조회 ###

    # 가계부 리스트 조회 성공
    def test_accountbook_list_success(self):
        response = self.client.get(
            path=reverse("accountbook_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEqual(response.status_code, 200)

    # 가계부 리스트 조회 실패(비로그인)
    def test_accountbook_list_login_fail(self):
        response = self.client.get(
            path=reverse("accountbook_view"),
        )
        self.assertEqual(response.status_code, 401)

    ### 가계부 작성 ###

    # 가계부 작성 성공
    def test_create_accountbook_success(self):
        response = self.client.post(
            path=reverse("accountbook_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.accountbook_data,
        )
        self.assertEqual(response.status_code, 201)
    
    # 가계부 작성 실패(비로그인)
    def test_create_accountbook_login_fail(self):
        response = self.client.post(
            path=reverse("accountbook_view"),
            data=self.accountbook_data,
        )
        self.assertEqual(response.status_code, 401)

    # 가계부 작성 실패(금액 빈칸)
    def test_create_accountbook_amount_fail(self):
        response = self.client.post(
            path=reverse("accountbook_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data={"amount": "", "content": "some content"},
        )
        self.assertEqual(response.status_code, 400)

    # 가계부 작성 실패(메모 빈칸)
    def test_create_accountbook_content_fail(self):
        response = self.client.post(
            path=reverse("accountbook_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data={"amount": "10000", "content": ""},
        )
        self.assertEqual(response.status_code, 400)

    # 가계부 작성 실패(accountbook_data 빈칸)
    def test_create_accountbook_fail(self):
        response = self.client.post(
            path=reverse("accountbook_view"),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data={"amount": "", "content": ""},
        )
        self.assertEqual(response.status_code, 400)   
    
class AccountbookDetailViewAPIViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1_data = {"email": "test1@test.com", "password": "password"}
        cls.user2_data = {"email": "test2@test.com", "password": "password"}
        cls.user1 = User.objects.create_user("test1@test.com", "password")
        cls.user2 = User.objects.create_user("test2@test.com", "password")
        cls.accountbook_data = {"amount": "10000", "content": "some content"}
        cls.accountbook = Accountbook.objects.create(amount="10000", content="some content", author=cls.user1)
    def setUp(self):
        self.access_token_1 = self.client.post(reverse("token_obtain_pair"), self.user1_data).data["access"]
        self.access_token_2 = self.client.post(reverse("token_obtain_pair"), self.user2_data).data["access"]
    
    ### 가계부 상세 조회 ###

    # 가계부 상세 조회 성공
    def test_accountbook_detail_success(self):
        response = self.client.get(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_1}",
        )
        self.assertEqual(response.status_code, 200)

    # 가계부 상세 조회 실패(비로그인)
    def test_accountbook_detail_loign_fail(self):
        response = self.client.get(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1})
        )
        self.assertEqual(response.status_code, 401)

    # 가계부 상세 조회 실패(본인이 아닐시)
    def test_accountbook_detail_loign1_fail(self):
        response = self.client.get(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_2}",
        )
        self.assertEqual(response.status_code, 403)

    ### 가계부 수정 ###

    # 가계부 수정 성공
    def test_edit_accountbook_success(self):
        response = self.client.put(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_1}",
            data={"amount": "10000", "content": "edit content"},
        )
        self.assertEqual(response.status_code, 200)

    # 가계부 수정 실패(비로그인)
    def test_edit_accountbook_login_fail(self):
        response = self.client.put(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            data={"amount": "10000", "content": "edit content"},
        )
        self.assertEqual(response.status_code, 401)

    # 가계부 수정 실패(작성자와 수정고객 불일치)
    def test_edit_accountbook_author_fail(self):
        response = self.client.put(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_2}",
            data={"amount": "10000", "content": "edit content"},
        )
        self.assertEqual(response.status_code, 403)
    
    # 가계부 수정 실패(금액 빈칸)
    def test_edit_accountbook_amount_fail(self):
        response = self.client.put(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_1}",
            data={"amount": "", "content": "edit content"},
        )
        self.assertEqual(response.status_code, 400)

    # 가계부 수정 실패(메모 빈칸)
    def test_edit_accountbook_content_fail(self):
        response = self.client.put(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_1}",
            data={"amount": "10000", "content": ""},
        )
        self.assertEqual(response.status_code, 400)

    # 가계부 수정 실패(accountbook data 빈칸)
    def test_edit_accountbook_data_fail(self):
        response = self.client.put(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_1}",
            data={"amount": "", "content": ""},
        )
        self.assertEqual(response.status_code, 400)

    ### 가계부 삭제 ###

    # 가계부 삭제 성공
    def test_delete_accountbook_success(self):
        response = self.client.delete(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_1}",
            data=self.accountbook_data,
        )
        self.assertEqual(response.status_code, 200)

    # 가계부 삭제 실패(비로그인)
    def test_delete_accountbook_login_fail(self):
        response = self.client.delete(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            data=self.accountbook_data,
        )
        self.assertEqual(response.status_code, 401)

    # 가계부 삭제 실패(작성자와 삭제고객 불일치)
    def test_delete_accountbook_author_fail(self):
        response = self.client.delete(
            path=reverse("accountbook_detail_view", kwargs={"accountbook_id": 1}),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token_2}",
            data=self.accountbook_data,
        )
        self.assertEqual(response.status_code, 403)
