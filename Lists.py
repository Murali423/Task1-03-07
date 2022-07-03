import logging

logging.basicConfig(filename='Lists.log', level=logging.DEBUG,
                    format='[%(levelname)s]: %(asctime)s : %(name)s : %(message)s')


class Lists:

    def __init__(self, lists):
        logging.info('Class initialization started. data added to constructor')
        self.lists = lists

    def reverse(self):
        try:
            logging.info('Enter the function which reverse list')
            logging.debug('Result of the function given below')
            logging.info(self.lists[::-1])
            return self.lists[::-1]
        except Exception as e:
            logging.error(e)

    def sum(self):
        try:
            logging.info('Enter the function which gives sum of list elements')
            logging.debug('Result of the function given below')
            logging.info(sum(self.lists))
            return sum(self.lists)
        except Exception as e:
            logging.error(e)

    def extract_list(self):
        try:
            logging.info('Enter the function which extract only lists')
            logging.debug('Result of the function given below')
            m = []
            for i in self.lists:
                if type(i) == list:
                    m.append(i)
                    logging.debug(m)
            return m
        except Exception as e:
            logging.error(e)

    def extract_element(self, element):
        try:
            logging.info('Enter the function which extract elements from list')
            logging.debug('Result of the function given below')
            for i in self.lists:
                if i == element:
                    logging.debug('Given element present in the list'+str(i))
                    return 'Given element present in list'
                elif type(i) == list:
                    for j in i:
                        if j == element:
                            logging.debug('Given element present in the list'+str(i))
                            return 'Given element present in list of list'
        except Exception as e:
            logging.error(e)



l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
t_lst = Lists(l)
print(t_lst.reverse())
print(t_lst.extract_list())
l1 = [6, 78, 90, 35, 6]
t_lst1 = Lists(l1)
print(t_lst1.sum())
print(t_lst.extract_element(456))

l2 = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]
t_lst2 = Lists(l2)
print(t_lst2.extract_list())