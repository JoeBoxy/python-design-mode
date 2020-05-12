# Singleton Mode

class MySingleton:

    __obj = None  # To deposit the singleton generated
    __birth_flag = True  # we use it to mark down the birth of singleton

    def __new__(cls, *args, **kwargs):
        # As we just want to generate only one object
        # so we are using the magic func to control it 
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        """
        print("init...")
        self.name = name
        """

        if self.__birth_flag:
            print("init...")
            self.name = name
            
            self.__birth_flag = False
        

a = MySingleton("boy")
b = MySingleton("girl")
print(a)
print(b)


# Now we finish the job