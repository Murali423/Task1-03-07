import logging

logging.basicConfig(filename='String.log', level=logging.DEBUG,
                    format='[%(levelname)s]: %(asctime)s: %(name)s:%(message)s')


class Strings:

    def __init__(self, string):
        self.string = string

    def slice_with_3(self):
        try:
            logging.info('Enter the slicing operation for 0 to 300 with step size 3')
            logging.debug('Result of the function is: '+ self.string[0:300:3])
            return self.string[0:300:3]
        except Exception as e:
            logging.error(e)

    def reverse(self):
        try:
            logging.info('Enter into the reverse of string function')
            logging.debug('Result of the function is: ' + self.string[::-1])
            return self.string[::-1]
        except Exception as e:
            logging.error(e)

    def split_upper(self):
        try:
            logging.info('Enter into the split with upper of string function')
            logging.info('Result of Function given below ')
            logging.debug(self.string.upper().split(' '))
            return self.string.upper().split(' ')
        except Exception as e:
            logging.error(e)

    def lower_case(self):
        try:
            logging.info('Enter into the lower of string function')
            logging.info('Result of Function given below ')
            logging.debug(self.string.lower())
            return self.string.lower()
        except Exception as e:
            logging.error(e)

    def capitalize(self):
        try:
            logging.info('Enter into the  capitalize of string function')
            logging.info('Result of Function given below ')
            logging.debug(self.string.capitalize())
            return self.string.capitalize()
        except Exception as e:
            logging.error(e)

    def strip(self):
        try:
            logging.info('Enter into the strip of string function')
            logging.info('Result of Function given below ')
            logging.debug(self.string.strip())
            return self.string.strip()
        except Exception as e:
            logging.error(e)

    def lstrip(self):
        try:
            logging.info('Enter into the lstrip of string function')
            logging.info('Result of Function given below ')
            logging.debug(self.string.lstrip())
            return self.string.lstrip()
        except Exception as e:
            logging.error(e)

    def rstrip(self):
        try:
            logging.info('Enter into the rstrip of string function')
            logging.info('Result of Function given below ')
            logging.debug(self.string.rstrip())
            return self.string.rstrip()
        except Exception as e:
            logging.error(e)

    def center(self, width, symbol):
        try:
            logging.info('Enter into the centering of string function')
            logging.info('Result of Function given below ')
            logging.debug(self.string.center(width, symbol))
            return self.string.center(width, symbol)
        except Exception as e:
            logging.error(e)



s1 = 'this is My First Python programming class and i am learNING python string and its function'
s2 = 'This is iNeuron Task'
t_str1 = Strings(s1)
t_str2 = Strings(s2)
print(t_str1.slice_with_3())
print(t_str2.slice_with_3())
print(t_str1.reverse())
print(t_str2.reverse())
print(t_str1.split_upper())
print(t_str2.split_upper())
print(t_str1.lower_case())
print(t_str2.lower_case())
print(t_str1.capitalize())
print(t_str2.capitalize())

s3 = '     This is iNeuron Platform we build our career    '
t_str3 = Strings(s3)
print(t_str3.strip())
print(t_str3.lstrip())
print(t_str3.rstrip())
print(t_str2.center(50, '*'))