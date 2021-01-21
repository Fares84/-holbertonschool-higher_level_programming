#!/usr/bin/python3
""" class MyInt that inherits from int """


class MyInt(int):
    """ MyInt definition inherits from int

    Arguments:
    int {[object]} -- (int object)
    """
    def __eq__(self, number):
        """ method compairson equal but actually != (not equal)

        Arguments:
            number {[int]} -- (number to check)

        Returns:
            [int] -- [number]
        """
        return int(self) != int(number)

    def __ne__(self, number):
        """ method comparison not equal but actually == (equal)

        Arguments:
            number {[int]} -- (number to check)

        Returns:
            [int] -- [number]
        """
        return int(self) == int(number)
