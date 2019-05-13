# import unittest  # Importing the unittest module
# from user import User  # Importing User class
# from credential import Credential  # Importing Credential class
#
#
# class TestUser(unittest.TestCase):
#     '''
#     Test class that defines test cases for the user class behaviours
#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''
#
#     def setUp(self):
#         '''
#         Set up method to run before each test cases
#         '''
#         self.new_user = User("Faith", "2019")  # create user object
#
#     def test_init(self):
#         '''
#         test_init test case to test if the object is instantiated properly
#         '''
#
#         self.assertEqual(self.new_user.name, "Faith")
#         self.assertEqual(self.new_user.password, "2019")
#
#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run
#         '''
#         User.user_list = []
#
#     def return_user(self):
#         self.new_user.return_user()
#
#
# class TestCredential(unittest.TestCase):
#     '''
#     Test class that defines test cases for the credential class behavious
#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''
#
#     def setUp(self):
#         '''
#         Set up method to run before each test cases
#         '''
#         self.new_credential = Credential(
#             "Faceb", "Faith", "2019")  # create credential object
#
#     def test_init(self):
#         '''
#         test_init test case to test if the object is instantiated properly
#         '''
#
#         self.assertEqual(self.new_credential.account, "Faceb")
#         self.assertEqual(self.new_credential.username, "Faith")
#         self.assertEqual(self.new_credential.password, "2019")
#
#     def test_save_account(self):
#         '''
#         test_save_account test case to test if the credential object is saved into the credential list
#         '''
#         self.new_credential.save_account()  # saving new account
#         self.assertEqual(len(Credential.credential_list), 5)
#
#     # def test_view_account(self):
#     #     '''
#     #     test to check if we can view accounts created and display innformation
#     #     '''
#     #     self.assertEqual(Credential.view_account(), Credential.credential_list)
#
#     def test_delete_account(self):
#         '''
#         test_delete_account to test if we can remove a user from our credential list
#         '''
#         self.new_credential.delete_account(self)
#         test_credential = Credential("Faceb", "Faith", "2019")
#
#         test_credential.delete_account(self)
#
#         self.new_credential.delete_account(self)  # Deleting a account object
#         self.assertEqual(len(Credential.credential_list), 2)
#
#
# if __name__ == '__main__':
#     unittest.main()
