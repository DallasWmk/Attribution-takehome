# README

_preface: I have flavored the assignment with a harry potter theme to make the project fun to review and more fun to develop. However, I do my best to not let the theme obscure what is being assessed_

## Introduction
---
Harry Potter and friends have been studying for their O.W.Ls but, as has been expected, the defense against the dark arts teacher this year has hardly taught anything useful for the exam. One student Dallas Womack developed a spell that would allow students to use a charm to get books from the restricted section to study from! 

The code in this repository was developed in response to a take-home technical assessment. In the root directory are two folders containing the application code for the Librarian (test client) and the RestrictedSection (Key-Value store)

## The Restricted Section (Key-Value Store)
---
The key value store in this environment is a containerized application that is able to:
- store a value for a given key
- will attempt to retrieve the value
- delete a key

In the event that a store operation is made against a key that already exists, the KV store will overwrite the previously stored value at that key with the new value per the instructions provided.

## The Librarian Charm (Test Client)
---
Per the instructions provided, the test client is a containerized application implementing two test methods against the Restricted Section KV Store:
- `test_deletion`
	This method deletes a key:value from the store and verifies that the new key has been deleted from the store
- `test_overwrite`
	This method overwrites a key:value pair and verifies that the new value is returned when querying the key.

## Instructions:
---
- To get started once having cloned the repo to a local machine, run the `build-docker-images.sh` script located in the root dir of the project to generate the images.
- After the images have been built, simply run `docker-compose up` to bring the images up and immediately start the tests. The server running the key-value store will come up first and display some start up logs, then shortly after the tests will run and display the results.
