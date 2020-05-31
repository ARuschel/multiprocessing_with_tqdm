import tqdm
import multiprocessing as mp

class FANCY_MP(object):
    '''The goal of this class is to provide a way of paralelize processes
    in Python while monitoring progress using tqdm.

    '''

    def __init__(self):
        
        self.pipeline = Queue()
        #this is a queue where we will pass the activities to be performed

        self.counter = Queue()
        #this queue will be used to manage tqdm counter

    def build_queue(self, cases_to_process):
        '''
        This method loads the cases to be processed into the queue
        '''
        count = 1
        for case in cases_to_process:
            self.pipeline.put(case)
            count += 1

        print('The queue was initialized with {} cases.'.format(count))

    def run_counter(self, cases):
        '''This method listens to the counter queue and whenever something
        is put in the counter, the loop runs once to update de tqdm bar
        '''

        print('Counter started with {} cases.'.format(len(cases)))

        for _ in tqdm.tqdm(cases):
            _ = self.counter.get(True)

        print('Counter Ended.')

    def infinite_function(self, process, return_dict, ...your_parameters_here):
        '''This method is an infinite loop getting items from the pipeline
        '''
        
        while True:

            try:
                query = self.pipeline.get(True, timeout = 2)
                #we set a 2 seconds timeout to avoid breaking the process
                #if some collision in getting from queue occurs

                self.your_function here(query)
                #calling the actual function you want to paralelize

                self.counter.put('1', True, timeout = 10)
                #after the function is sucessfully executed, a 1 is sent to 
                #the counter to update tqdm bar

            except:

                #If the queue reaches 2 seconds the queue is empty, so the process
                #finishes
                return

    def main_function(self):
        '''This method is the main controler, handling the multiprocessing and
        gathering the results (if something is returned)

        '''

        #loading the multiprocessing manager 
        manager = mp.Manager()

        #creating the dict that will return the results
        return_dict = manager.dict()

        #building the queue           
        self.build_queue( ... your parameters here...)

        #process and counter inicialzation
        processes = []
        cases = [1] * ( xxx ) #update here with queue size

        #initializing counter and appending process
        p = mp.Process(target = self.run_counter, args=(cases,))
        processes.append(p)

        #initializing all paralel process
        for i in range(mp.cpu_count()):
            p = mp.Process(target = self.infinite_function, args=(i, return_dict))
            processes.append(p)
        
        [x.start() for x in processes]
        [x.join() for x in processes]


        return return_dict

    def your_function_here(self, your args )
        '''Function that will perform the actual activity

        '''
        return
