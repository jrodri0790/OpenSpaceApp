import rstr


class CodeGenerator:

    @classmethod
    def generate_codes(cls, number_of_codes):
        codes = []
        for i in range(0, number_of_codes):
            generated_code = rstr.xeger(r'XC[A-Z]{3}-[\d]{3}')
            codes.append(generated_code)
        print(codes)
        return codes
