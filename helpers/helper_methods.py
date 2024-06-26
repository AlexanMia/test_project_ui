
class HelperMethods:
    @staticmethod
    def split_string(text: str, separator: str) -> list:
        """
        This method split sting according to the specified separator

        :param text: some string
        :param separator: some separator, for example, ":"
        :return:
        """
        return text.split(separator)
