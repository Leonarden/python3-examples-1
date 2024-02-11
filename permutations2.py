'''
Computes Permutations or Combinations from given collection of different elements

'''
import itertools


class Computation():
    """
    Abstract class for Permutation and Combination
    """
    def compute(self,N,R):
        'By default returns str '
        '" " + str(N) + "taken by" + str(R) + ""'
        return -1

    def m_factorial(self,N):
        if (N==0):
            return 1
        elif (N==1):
            return 1
        else:
            return (self.m_factorial(N-1) * N)

    def gen_result(self,collection,R):
        """
        """
        return collection

class Permutation(Computation) :
    """
    """
    def compute(self,N,R):
        """
        applies formula: Result = N! / (N-R)!
        """
        if(R>0):
            return (self.m_factorial(N) / self.m_factorial(N-R))
        else:
            return 1

def gen_result(self, collection, R):
    """
    Generates a resulting collection from applying permutations between elements
    """
    permcol = itertools.permutations([collection],R)

    return permcol


class Combination(Computation):
    """

    """
    def compute(self,N,R):
        """
        applies formula: Result = N!  / ((N-R)! * R!)
        """
        if(R>0):
            return ( self.m_factorial(N) / ( self.m_factorial(N-R) * self.m_factorial(R)))
        else:
            return 1

    def gen_result(self,collection,R):
        """
        Generates a resulting collection from applying permutations between elements
        """
        permcol = itertools.combinations(collection,R)
        return permcol

class Executor():
    """
    """

    filters = ["wrongitem1","wrongitem2","wrongitem3"]

    def __init__(self,collection = [],operation_type = "Permutation"):

        self.operation_type = operation_type
        self.N = -1
        self.R = -1
        self.computation = None
        self.op_result = -1
        self.collection = None
        self.col_result = None
        self.operation = Permutation()

        if(len(collection)>0):
            'filter elements?'
            self.collection = collection
            self.N = len(self.collection)
            self.initialset = True

    def filter(self,elem):
        if( not elem  in self.filters ):
            return elem
        else:
            return None

    def prompt_input(self):
        """
        """
        optype = "P"
        to_set = False

        while(True):
            optype = input("Which operation do you want to perform? (P) Permutation, (C) Combination: ")
            if (optype in ["P","C"]):
                break
        self.collection = list()
        if(optype=="P"):
            self.operation_type = "Permutation"
        else:
            self.operation_type = "Combination"
            to_set = True

        print("Input a elements to work with:")
        print("Press \"E\" for exit.")
        sc = "#"
        i = 0
        while ( True ):
            sc = input(f"Input element # {i+1} (E=Exit): ")
            'casting element?'
            if( ( sc == "E" ) or (sc =="e")):
                break
            sc = self.filter(sc)
            if ((sc != None)):
                if(to_set and (not sc in self.collection)):
                    'Avoid repetitions'
                    self.collection.append(sc)
                    i = i + 1
                elif (not to_set):
                    'Normal insertion'
                    self.collection.append(sc)
                    i = i + 1

        self.N = len(self.collection)
        print(f"You have input {self.N} elements to perform  {self.operation_type} ")
        print("How much of the total of elements do you want to take to perform the computation ?")
        sr = ""
        while(True):
            sr = input(f"input number R  (lower than {self.N} ) ")
            if(sr.isnumeric()):
                break

        self.R = int(sr)


    def display(self):
        """
        """
        print(f"Initial collection:  {str(self.collection)}")
        if(self.op_result>=0):
            print(f"Resulting {self.operation_type} of {self.N} elements taken by {self.R}  is: {self.op_result} ")
        else:
            print(f"Resulting {self.operation_type} of {self.N} elements taken by {self.R}  couldn\'t be performed !")

    def display_full(self):
        """
        """
        print(f"Initial collection:  {str(self.collection)}")
        if(self.op_result>=0):
            print(f"Resulting {self.operation_type} of {self.N} elements taken by {self.R}  is: {self.op_result} ")
            """
            if(len(self.col_result)>0):
            """
            print(f" {list(self.col_result)} ")
            '''
            for I in range(0,len(self.col_result)):
            print(f"{I+1}#: {self.col_result[I]}")
            '''
        else:
            print(f"Resulting {self.operation_type} of {self.N} elements taken by {self.R}  couldn\'t be performed !")


    def execute(self,flag=0):
        """
        """
        if(self.operation_type=="Permutation"):
            self.operation = Permutation()
        elif(self.operation_type=="Combination"):
            self.operation = Combination()
            self.collection = set(self.collection)
        self.N = len(self.collection)

        self.op_result = self.operation.compute(self.N,self.R)
        if(flag>0):
            self.col_result = self.operation.gen_result(self.collection,self.R)


if  __name__ == '__main__' :

    icollection = []

    executor = Executor(icollection)

    executor.prompt_input()

    executor.execute(1)

    executor.display_full()

    print ("End of program.")
