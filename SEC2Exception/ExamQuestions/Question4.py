# - - - - - - - UDEMY: PCAP CERTIFIED ASSOCIATE W/PYTHON PROGRAMMING CERTIFICATION- - - - - - -
# - - - - - - - Practice Test 2: Exam Block #2 Exceptions  - - - - - - -
"""
Question 4:
Select which option will call the __init__ method of Exception based on the code below.

class SpamException(Exception):
  def __init__(self, message):
    <<< INSERT CODE HERE >>>
    self.message = message
raise SpamException("Spam")W
"""


class SpamException(Exception):
    def __init__(self, message):
        #Exception.__init__(self, message)
        #super(SpamException, self).__init__(message)
        #super.__init__message()
        #super().__init__message()
        self.message = message
raise SpamException("Spam")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -