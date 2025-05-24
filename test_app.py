import unittest
from unittest import mock

import app

class TestEmail(unittest.TestCase):
    @mock.patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        app.send_email('user@example.com')
        mock_smtp.assert_called_with(app.SMTP_SERVER, app.SMTP_PORT)
        instance = mock_smtp.return_value.__enter__.return_value
        instance.sendmail.assert_called()

if __name__ == '__main__':
    unittest.main()
