__author__ = 'rizkivmaster'
import unittest
import telegram_controller

class ControllerTest(unittest.TestCase):

    def test_Handler(self):
        class MockBot:
            def __init__(self):
                pass

            def sendMessage(self, id, message):
                print('id: %d \nmessage : %s' % (id, message))
        telegram_controller.set_bot(MockBot())
        telegram_controller.handle({
            'from':
                {
                    'username':'rizkirank',
                    'id':123
                },
            'text': 'kirim ardi 20000'
        });




if __name__ == '__main__':
    unittest.main()