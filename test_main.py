import unittest
from main import app

class TestMain(unittest.TestCase):

    #check for response 200
    def test_main(self):
        tester = app.test_client(self)
        response = tester.get()
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if content return is application/json
    def test_content(self):
        tester = app.test_client(self)
        response = tester.get()
        self.assertEqual(response.content_type, "application/json")

    #Check for returned data
    def test_returned_data(self):
        tester = app.test_client(self)
        response = tester.get()
        self.assertTrue(b"Aaron" in response.data)


if __name__=="main":
    unittest.main()

