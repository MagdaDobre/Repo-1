import unittest
import HtmlTestRunner

from tema_9 import Login
from cod_intalnirea_10.auth import Authentication
from cod_intalnirea_10.alerts import Alerts
from cod_intalnirea_10.context_menu import ContextMenu
from cod_intalnirea_10.key_press import Keyboard


class TestSuite(unittest.TestCase):

    def test_suite(self):

        test_to_run = unittest.TestSuite()
        test_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Report tema_10_ex1',
            report_title='Report Title tema_10_ex1'
        )

        runner.run(test_to_run)


