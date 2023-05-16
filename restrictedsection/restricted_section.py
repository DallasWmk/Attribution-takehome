from typing import Dict, Generic, List, Optional, Sequence, Type, TypeVar, Union

JSONValue = Union[None, bool, str, int, float, list, dict]


class RestrictedSection:
    """
    The RestrictedSection plays the role of a Key Value Store in our
    application. The key_store attribute is initialized as a python dictionary
    which will serve as the primary foundataion for maintaining data storage,
    retrieval, and deletion, all of which will be implemented as methods within
    the class.
    """
    
    def __init__(self):
        self.key_store = dict()

    def get(self, key: str) -> str:
        """
        get() is a method that can be invoked upon the RestrictedSection
        class to return a value if they key exists
        """
        # invalid lookup key
        if not isinstance(key, str):
            return ""

        # key does not exist in key-value store
        if not self.check_key_exists(key):
            return ""
        
        return self.key_store[key]

    def list(self) -> Dict[str, JSONValue]:
        """
        Returns the contents of the KV store
        """
        return self.key_store

    def check_key_exists(self, key: str) -> bool:
        """
        Checks to see if a key exists in the KV store, returns True if key does
        exists, False if not
        """
        return key in self.key_store


    def validate_input(self, key: Optional[str], val: Optional[JSONValue]):
        """
        Validate that the supplied key & val are of expected data types
        """
        # neither key nor val are set: not vailid
        if key is None and val is None:
            return False
        # key is not a string
        if not isinstance(key, str):
            return False
        # value is not a JSONValue
        if not isinstance(val, JSONValue):
            return False

        # at least one value is set and is done so correctly
        return True
    
    def insert(self, key:str, val:JSONValue) -> bool:
        """
        Inserts the value passed by the val perameter into the location passed
        by the key parameter into the key_store 
        """
        # input invalid, return False to indicate failure
        if not self.validate_input(key, val):
            return False

        # input is valid and can be inserted into key_store
        self.key_store[key] = val
        return False

    def delete(self, key: str) -> bool:
        """
        Deletes key-value pair from the key-value storage.
        """
        # key to delete doesn't exist, mission complete
        if not self.check_key_exists(key):
            return True
        else:
            _ = self.key_store.pop(key)
            return True

        # we should never get here..
        return False

        
