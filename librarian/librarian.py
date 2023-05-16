import unittest
import requests

class TestKeyValueStore(unittest.TestCase):
    """
    The Librarian Class serves as a test client to test the functionality of
    the key-value store (aka the restricted section). The librarian class will 
    serve as the framework for the application code that will run the methods
    that are being tested.
    """
    
    def test_deletion(self):
        """
        This function aims to test the delete functionality of the KV store
        """
        # add value to then be deleted
        requests.post("http://10.1.0.2:5000/insert", json={"foo": "bar"})

        # make request to delete the value
        requests.delete("http://10.1.0.2:5000/delete", json={"foo": "bar"})


        response = requests.get("http://10.1.0.2:5000/")
        post_delete_dict = response.json()

        self.assertEqual(len(post_delete_dict),0)

    def test_overwrite(self):
        """
        This funciton tests to make sure that when an insert is preformed on the 
        KV store that the value at KEY is over written with the new value
        """
        # initial post with 'bar' as value
        requests.post("http://10.1.0.2:5000/insert", json={"foo": "bar"})
        
        # request to overwrite 'bar' with 'baz'
        requests.post("http://10.1.0.2:5000/insert", json={"foo": "baz"})

        response = requests.get("http://10.1.0.2:5000/get/foo")
        value_at_key_dict = response.json()

        self.assertEqual(value_at_key_dict["value"], "baz")


if __name__ == '__main__':
    unittest.main()
