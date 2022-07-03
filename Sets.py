import logging

logging.basicConfig(filename='Sets.log', level=logging.DEBUG,
                    format='[%(levelname)s]: %(asctime)s : %(name)s : %(message)s')


class Sets:

    def __init__(self,s):
        logging.info('Class initialization started. data added to constructor')
        self.sets = s

    def get_set(self):
        try:
            logging.info('Enter the function which gives set from given list')
            logging.debug('Result of the function given below')
            for i in self.sets:
                if type(i) == set:
                    logging.info(i)
                    return i
        except Exception as e:
            logging.error(e)

    def get_unique(self):
        try:
            logging.info('Enter the function which gives unique elements')
            logging.debug('Result of the function given below')
            if type(self.sets) == list or type(self.sets) == str :
                logging.info(set(self.sets))
                return set(self.sets)
        except Exception as e:
            logging.error(e)


l1 = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]
t_set1 = Sets(l1)
print(t_set1.get_set())

l2= [2,2,2,2,4,4]
t_set2 = Sets(l2)
print(t_set2.get_unique())