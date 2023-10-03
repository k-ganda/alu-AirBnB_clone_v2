from tests.test_models.test_base_model import test_basemodel as Test_BaseModel
from models.user import User


class test_User(Test_BaseModel):
    def setUp(self):
        self.name = "User"
        self.value = User

    def test_first_name(self):
        new = self.value(first_name="John", password="password")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        new = self.value(last_name="Doe", password="password")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        new = self.value(email="example@example.com", password="password")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        new = self.value(password="password")
        self.assertEqual(type(new.password), str)