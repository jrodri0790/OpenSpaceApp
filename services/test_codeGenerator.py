from unittest import TestCase

from services.code_service import CodeGenerator


class TestCodeGenerator(TestCase):
    def test_code_generation(self):
        code_gen = CodeGenerator()
        code_gen.generate_codes(200)
