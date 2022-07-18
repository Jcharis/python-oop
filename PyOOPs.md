### Object Oriented Programming in Python
+ Error Based Learning
By Jesse E.Agbemabiase (JCharis)
* Jesus Saves @JCharisTech

#### Outline
+ Ways to Create Objects
+ OOP Principles
    - Inheritance (Multiple Inheritance,Multi-Level,Supervised Inheritance)
    - Encapsulation
    - Polymorphism
    - Abstraction
    - Composition
+ Gotchas

#### Structure using UML
+ Person(fname,lastname,age)
+ Pupil(p..,16yrs,p1-p9)
+ Student(p.17yrs,f1.4,major)
+ Teacher(Full Time.Part time,visiting,TA)
+ HeadMaster
+ Counselor
+ Manager (HR,
+ Accountant
+ 

#### Everything in python is a type and an object
+ it is an object of the base class `type`

##### What is an object and what is a class?
+ A class is a blueprint (like a questionaire that you have to fill with data or information
* classes are just pieces of code that describe how to produce an object.
+ An instance is a copy of the class with actual values (your specific copy is an instance of the class; it contains actual information relevant to you)


```python
a = "hello python"
b = 1
c = [1,2,4]
d = (1,3,5)
print("Type of a string",type(a))
print("Type of an integer",type(b))
print("Type of a list",type(c))
print("Type of a tuple",type(d))
```

    Type of a string <class 'str'>
    Type of an integer <class 'int'>
    Type of a list <class 'list'>
    Type of a tuple <class 'tuple'>


+ str, the class that creates strings objects, and 
+ int the class that creates integer objects. 
+ type is just the class that creates class objects.


```python
print(type(str))
print(type(int))
print(type(list))
print(type(tuple))
print(type(object))
```

    <class 'type'>
    <class 'type'>
    <class 'type'>
    <class 'type'>
    <class 'type'>



```python
# what is the type of any class/object in python?ans type
type(type(str))
```




    type



##### Hence the hierarchy is 
object => class => type 


```python
# the type of an object is a type
print(type(object))
```

    <class 'type'>


#### Narrative
+ Everything, and I mean everything, is an object in Python. That includes integers, strings, functions and classes. 
+ All of them are objects. And all of them have been created from a class

#### Metaclass
+ a metaclass is just the stuff that creates class objects.
+ type is a function 
+ type is a metaclass that python use to create class object
+ type is the built-in metaclass Python uses
A metaclass is the class of a class. A class defines how an instance of the class (i.e. an object) behaves while a metaclass defines how a class behaves. A class is an instance of a metaclass.
The main purpose of a metaclass is to change the class automatically, when it's created.

You usually do this for APIs, where you want to create classes matching the current context.They are simply used for:
 + intercept a class creation
 + modify the class
 + return the modified class
 
The main use case for a metaclass is creating an API. A typical example of this is the Django ORM.
https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

Their use for alteration of a class can be done with monkeypatching or with class decorators




```python
# using the .__class__ to check for the fact that everything in python is an object and has been created from a class 
# same as doing type()
print(a.__class__)
```

    <class 'str'>



```python
# What is the type of any type or what is the class of any .__class__
print(a.__class__.__class__)
```

    <class 'type'>


#### Creating a Class in Python
+ A Class is a blueprint or cookiecutter for creating an object
+ An object is anything that has state(data coming from attributes of something) and behavior(methods)


```python
# Method 1: Using the constructor approach
# the __init__() initializes the arguments when the class is used to create an object
class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

```


```python
p = Person("Jesse","JCharis")
print(p)
print("Check the type",type(p))
```

    <__main__.Person object at 0x7f8848a52c80>
    Check the type <class '__main__.Person'>


##### Narrative
+ we have got the same results as the initial types (<class 'type'> === <class '__main__.Person'>)
# Method 2: Using __new__()
__new__() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) 
to customize instance creation
__new__ is static class method, while __init__ is instance method.
__new__ has to create the instance first, so __init__ can initialize it. 
Note that __init__ takes self as parameter. Until you create instance there is no self.
Use __new__ when you need to control the creation of a new instance.

Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.

In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str, int, unicode or tuple.
https://stackoverflow.com/questions/674304/why-is-init-always-called-after-new


```python
# Why __new__?: for creating a new instance
# Why __init__?: for initializing a new instance
class Person2:
    def __new__(cls):
        print("Creating instance")
  
    # It is not called
    def __init__(self):
        print("Init is called")
```


```python
print(Person2())
```

    Creating instance
    None


#### Narrative
+ When you usee `__new__`, without Super(), the instance are created but not initialized


```python
class Person2:
    def __new__(cls):
        print("Creating instance")
        return super(Person2, cls).__new__(cls)
  
    # It is called and hence an instance is initialized as you can see below
    def __init__(self):
        print("Init is called")
```


```python
print(Person2())
```

    Creating instance
    Init is called
    <__main__.Person2 object at 0x7f8848a53850>


#### Components of a Class
+ instance of an object = state + behavior
+ object = attributes + methods
* state: It is represented by the attributes of an object. It also reflects the properties of an object.
* behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.



```python
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
```


```python
##### Creating an Object
p = Person("Jesse","JCharis",25)
print(p)
```

    <__main__.Person object at 0x7f8848a51a80>


##### Narrative
+ An object of Person class was created at 0x7f4808d5aec0 
+ What does the 0x7f4808d5aec0 mean?
  - It is a hexdecimal number
  - That is the Memory address allocated for that object to identify(id) it hence when we
    use id() on that object we must get the same value
+ The id is assigned to the object when it is created.
+ The id is the object's memory address, and will be different for each time you run the program. (except for some object that has a constant unique id, like integers from -5 to 256)


```python
# Convert the hex to decimal
# ast.literal_eval('0x7f4808d5aec0')
int(0x7f8848a51a80)
```




    140223311059584




```python
# Get the memory address or identification of that object
id(p)
```




    140223311059584




```python
#### Getting the attributes
#### the attributes stores data or state these are the variables
p.first_name
```




    'Jesse'




```python
#### How to get all attributes or instance variables of an object created 
vars(p)
```




    {'first_name': 'Jesse', 'last_name': 'JCharis', 'age': 25}




```python
#### How to get all attributes or instance variables of an object created 
dir(p)
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'age',
     'first_name',
     'last_name']



#### Narrative: Difference between var() and dir()
`vars()` Function: 
+ It displays the attribute of an instance in the form of a dictionary.
+ Only works for object that implement __dict__ function

`dir()` Function: 
+ It displays the instance attributes and the class attributes as well. 
+ It also displays the attributes of its ancestor classes.
+ It is not limited to an instance.




```python
#### How to get all attributes or instance variables of an object created  var() == object.__dict__
p.__dict__
```




    {'first_name': 'Jesse', 'last_name': 'JCharis', 'age': 25}



#### User Experience(UX and UI) of Class 
+ Developer: `__repr__()`
+ Regular User:`__str__()`


```python
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"Person({self.first_name!r},{self.last_name},{self.age})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"Person(first_name={self.first_name},last_name={self.last_name},age={self.age})"
```


```python
p = Person("Jesse","JCharis",25)
print(p)
```

    Person(first_name=Jesse,last_name=JCharis,age=25)



```python
# For Developers
# Notice the quotation marks on the first this is because of !r without it you will not see the quotation marks
p
```




    Person('Jesse',JCharis,25)



#### Creating Methods For a Class
+ A Method is a function for a class that controls the behavior of the object
+ instance method: fxns that takes self as first param and controls the behavior of the object instance hence it can
access the instance attributes or variables
+ class method: fxn that takes cls as first param and have access to the class itself
    - A class method can access or modify the class state while a static method can’t access or modify it.
    - convention is to use `_from_`
    - uses @classmethod
+ static method: fxns that doesnt take either self or cls as first params and they are used as utility functions
    - they can actually live outside the class but we keep them here
    - uses @staticmethod
    

#### Instance Methods


```python
# Instance Methods
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"Person({self.first_name!r},{self.last_name},{self.age})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"Person(first_name={self.first_name},last_name={self.last_name},age={self.age})"
    
    def create_email(self):
        return "{}@gmail.com".format(self.first_name)
    
    def create_pin(self):
        return f"{self.last_name}{self.age}"
        
```


```python
p = Person("Mark","Twain",57)
print(p)
```

    Person(first_name=Mark,last_name=Twain,age=57)



```python
p.create_email()
```




    'Mark@gmail.com'



#### Static Methods: utility fxns


```python
### Static Method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"Person({self.first_name!r},{self.last_name},{self.age})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"Person(first_name={self.first_name},last_name={self.last_name},age={self.age})"
    
    def create_email(self):
        return "{}@gmail.com".format(self.first_name)
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    # utility fxn that we can use outside
    @staticmethod
    def get_age_group(value):
        age = value
        if age <= 12:
            return 'child'
        elif age >= 13 and age < 20:
            return 'teenager'
        elif age >= 20:
            return 'adult'
        else:
            return "None" 
        
```


```python
Person.get_age_group(43)
```




    'adult'



#### Class Methods


```python
### Static Method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"Person({self.first_name!r},{self.last_name},{self.age})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"Person(first_name={self.first_name},last_name={self.last_name},age={self.age})"
    
    def create_email(self):
        return "{}@gmail.com".format(self.first_name)
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    # utility fxn that we can use outside
    @staticmethod
    def get_age_group(value):
        age = value
        if age <= 12:
            return 'child'
        elif age >= 13 and age < 20:
            return 'teenager'
        elif age >= 20:
            return 'adult'
        else:
            return "None" 
    
    # Fxns to create the birthday and age
    @classmethod
    def from_Birth_Year(cls,first_name,last_name, year):
        from datetime import date
        return cls(first_name,last_name,date.today().year - year)
    
    @classmethod
    def to_Birth_Year(cls,first_name,last_name, age):
        from datetime import date
        return cls(first_name,last_name,date.today().year - age)
        
        
```


```python
Person.to_Birth_Year("Jesse","J",25)
```




    Person('Jesse',J,1997)




```python
Person.from_Birth_Year("Jesse","J",2000)
```




    Person('Jesse',J,22)




```python
# Bound method  occurs when you omit the () the fxn call
# What does this tells us?: it appears that we are accessing it like an attributes
# every method can be made to behave like an attribute via properties
p.create_email
```




    <bound method Person.create_email of Person('Mark',Twain,57)>



### OOP Principles
+ Encapsulation
+ Inheritance
+ Polymorphism
+ Abstraction
+ Aggregation
+ Composition
+ Association

### Inheritance
+ It allows a class to inherit or acquire all the features(methods,attributes) of its parents class
* Inheritance models what is called an is a relationship



#### Goals
+ Code reuse
+ Code readability
+ DRY


```python
### Static Method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"Person({self.first_name!r},{self.last_name},{self.age})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"Person(first_name={self.first_name},last_name={self.last_name},age={self.age})"
    
    def create_email(self):
        return "{}@gmail.com".format(self.first_name)
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    # utility fxn that we can use outside
    @staticmethod
    def get_age_group(value):
        age = value
        if age <= 12:
            return 'child'
        elif age >= 13 and age < 20:
            return 'teenager'
        elif age >= 20:
            return 'adult'
        else:
            return "None" 
    
    # Fxns to create the birthday and age
    @classmethod
    def from_Birth_Year(cls,first_name,last_name, year):
        from datetime import date
        return cls(first_name,last_name,date.today().year - year)
    
    @classmethod
    def to_Birth_Year(cls,first_name,last_name, age):
        from datetime import date
        return cls(first_name,last_name,date.today().year - age)
        
# Full Inheritance
class Pupil(Person):
    pass

# Inheritance that overide
# Will override the attributes of the Parent Class when initialize
class Student(Person):
    def __init__(self,first_name):
        self.first_name = first_name
        
        
# Inheritance that extends
class Graduate(Person):
    def __init__(self,first_name,last_name,age,year_of_study,specialization):
        self.year_of_study = year_of_study
        self.specialization = specialization
    
    def type_of_student(self):
        print(f"{year_of_study}{specialization} student")
        
```


```python
# Check Full Inheritance
pu = Pupil("Peter","Pan",12)
print(pu)
```

    Person(first_name=Peter,last_name=Pan,age=12)


#### Narrative
+ Notice the repr produce the same form as the base class
+ How do we fix that


```python
### Inheritance
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.first_name!r},{self.last_name},{self.age})" 
        # avoid bad naming when there are subclass hence it will use the current instance class name
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name},last_name={self.last_name},age={self.age})"
    
    def create_email(self):
        return "{}@gmail.com".format(self.first_name)
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    # utility fxn that we can use outside
    @staticmethod
    def get_age_group(value):
        age = value
        if age <= 12:
            return 'child'
        elif age >= 13 and age < 20:
            return 'teenager'
        elif age >= 20:
            return 'adult'
        else:
            return "None" 
    
    # Fxns to create the birthday and age
    @classmethod
    def from_Birth_Year(cls,first_name,last_name, year):
        from datetime import date
        return cls(first_name,last_name,date.today().year - year)
    
    @classmethod
    def to_Birth_Year(cls,first_name,last_name, age):
        from datetime import date
        return cls(first_name,last_name,date.today().year - age)
        
# Full Inheritance
class Pupil(Person):
    pass

# Inheritance that overide
class Student(Person):
    def __init__(self,first_name):
        self.first_name = first_name
        
        
# Inheritance that extends
class Graduate(Person):
    def __init__(self,first_name,last_name,age,year_of_study,specialization):
        self.year_of_study = year_of_study
        self.specialization = specialization
    
    def type_of_student(self):
        print(f"{year_of_study}{specialization} student")
        
```


```python
# Check Full Inheritance
pu = Pupil("Peter","Pan",12)
print(pu)
```

    Pupil(first_name=Peter,last_name=Pan,age=12)



```python
# Check Overiding
s = Student("Peter")

```


```python
print(s)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Input In [41], in <cell line: 1>()
    ----> 1 print(s)


    Input In [38], in Person.__str__(self)
         13 def __str__(self):
         14     "For Regular Users showing them what they need to know and what is contains"
    ---> 15     return f"{self.__class__.__name__}(first_name={self.first_name},last_name={self.last_name},age={self.age})"


    AttributeError: 'Student' object has no attribute 'last_name'


#### Narrtive
+ Why the AttributeError?
Because it is inheriting from the Parent class that has the last name hence we have to overide those methods too


```python
# Inheritance that overide
class Student(Person):
    def __init__(self,first_name):
        self.first_name = first_name
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.first_name!r})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name})"
```


```python
# Check Overiding of all
s = Student("Peter")
print(s)
```

    Student(first_name=Peter)


#### How do we get all the parents attributes as well as the child attributes according?
+ use of super()
+ Using super() allows it to inherit all the attributes of the parent class Person and initialize them too 
+ Without assigning it below it will use the attributes from the Parent class assigned above


```python
# Inheritance and the super()
class Student(Person):
    def __init__(self, first_name, student_id) -> None:
        super().__init__() # leave it empty will produce an error
        self.student_id = student_id #access the new extended attrib
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.first_name!r})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name})"
```


```python
# Check Overiding of all
s = Student("Peter",1)
print(s)
print(s.create_email())
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [47], in <cell line: 2>()
          1 # Check Overiding of al
    ----> 2 s = Student("Peter",1)
          3 print(s)
          4 print(s.create_email())


    Input In [45], in Student.__init__(self, first_name, student_id)
          3 def __init__(self, first_name, student_id) -> None:
    ----> 4     super().__init__() # leave it empty will produce an error
          5     self.student_id = student_id


    TypeError: Person.__init__() missing 3 required positional arguments: 'first_name', 'last_name', and 'age'



```python
# Inheritance and the super()
class Student(Person):
    def __init__(self, first_name, student_id) -> None:
        super().__init__(first_name,last_name,age) # place in here the attributes of the parent class this will initialize them also
        self.student_id = student_id
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.first_name!r})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name})"
```


```python
# Check Overiding of al
s = Student("Peter",1)
print(s)

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [49], in <cell line: 2>()
          1 # Check Overiding of al
    ----> 2 s = Student("Peter",1)
          3 print(s)


    Input In [48], in Student.__init__(self, first_name, student_id)
          3 def __init__(self, first_name, student_id) -> None:
    ----> 4     super().__init__(first_name,last_name,age) # place in here the attributes of the parent class this will initialize them also
          5     self.student_id = student_id


    NameError: name 'last_name' is not defined



```python
# Inheritance and the super()
# fix by using none
class Student(Person):
    def __init__(self, first_name, student_id) -> None:
        super().__init__(first_name,last_name=None,age=None) # place in here the attributes of the parent class this will initialize them also
        self.student_id = student_id
      
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.first_name!r})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name})"
```


```python
# Check Inheritance
s = Student("Peter",1)
print(s)

```

    Student(first_name=Peter)



```python
print(s.last_name)
```

    None



```python
# Inherit all the methods too
s.create_email()
```




    'Peter@gmail.com'



##### How to check if a class is subclass of another?
Python provides a function issubclass() that directly tells us if a class is subclass of another class.


```python
issubclass(Student,Person)
```




    True




```python
### Multiple Inheritance

```


```python
class Person:
    def __init__(self,first_name=None,last_name=None,age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.first_name!r},{self.last_name},{self.age})" 
        # avoid bad naming when there are subclass hence it will use the current instance class name
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name},last_name={self.last_name},age={self.age})"
    
    def create_email(self):
        return "{}@gmail.com".format(self.first_name)
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    # utility fxn that we can use outside
    @staticmethod
    def get_age_group(value):
        age = value
        if age <= 12:
            return 'child'
        elif age >= 13 and age < 20:
            return 'teenager'
        elif age >= 20:
            return 'adult'
        else:
            return "None" 
    
    # Fxns to create the birthday and age
    @classmethod
    def from_Birth_Year(cls,first_name,last_name, year):
        from datetime import date
        return cls(first_name,last_name,date.today().year - year)
    
    @classmethod
    def to_Birth_Year(cls,first_name,last_name, age):
        from datetime import date
        return cls(first_name,last_name,date.today().year - age)

class Student(Person):
    def __init__(self, first_name, student_id) -> None:
        super().__init__(first_name) # place in here the attributes of the parent class this will initialize them also
        self.student_id = student_id
      
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.first_name!r})"
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name})"

class Teacher(Person):
    def __init__(self,first_name,subject,department):
        super().__init__(first_name)
        self.subject = subject
        self.department = department
        

class TeachingAssistant(Student,Teacher):
    pass
```


```python
ta = TeachingAssistant("John","Maths",12)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [116], in <cell line: 1>()
    ----> 1 ta = TeachingAssistant("John","Maths",12)


    TypeError: Student.__init__() takes 3 positional arguments but 4 were given



```python
TeachingAssistant.__mro__
```




    (__main__.TeachingAssistant,
     __main__.Student,
     __main__.Teacher,
     __main__.Person,
     object)




```python
### Let reverse it maybe it will fix the TypeError which occurs because it does-nt know which to use first
class TeachingAssistant(Teacher,Student):
    pass
ta = TeachingAssistant("John","Maths",12)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [118], in <cell line: 4>()
          2 class TeachingAssistant(Teacher,Student):
          3     pass
    ----> 4 ta = TeachingAssistant("John","Maths",12)


    Input In [115], in Teacher.__init__(self, first_name, subject, department)
         61 def __init__(self,first_name,subject,department):
    ---> 62     super().__init__(first_name)
         63     self.subject = subject
         64     self.department = department


    TypeError: Student.__init__() missing 1 required positional argument: 'student_id'



```python
TeachingAssistant.__mro__
```




    (__main__.TeachingAssistant,
     __main__.Teacher,
     __main__.Student,
     __main__.Person,
     object)




```python
# Solution is to specify one first and overide it and assign them
class TeachingAssistant(Teacher,Student):
    def __init__(self,first_name,subject,department):
        Student.__init__(self,first_name,student_id=None) # make id as none
        self.subject = subject
        self.department = department
        
```


```python
ta = TeachingAssistant("John","Maths",12)
```


```python
ta
```




    TeachingAssistant('John')




```python
ta.subject
```




    'Maths'




```python
ta.department
```




    12




```python
ta.student_id = 34
```


```python
ta.student_id
```




    34




```python
TeachingAssistant
```

### Method Resolution Order
+ MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy 
+ It is useful in Python because Python supports multiple inheritance.
The MRO satisfies 3 properties:

+ Children of a class come before their parents
+ Left parents come before right parents
+ A class only appears once in the MRO



```python
### MR0
s.__class__.__mro__
```




    (__main__.Student, __main__.Person, object)



the Liskov substitution principle. 
The principle states that “in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties of the program”.

### Encapsulation
+ En + capsule
+ It describes the idea of wrapping data and the methods that work on data within one unit. 
+ This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
+ To prevent accidental change, an object’s variable can only be changed by an object’s method
Encapsulation helps with data security, allowing you to protect the data stored in a class from system-wide access. 
As the name suggests, it safeguards the internal contents of a class like a capsule.

##### Summary
+ capsule
+ data security and restriction
    - private: _
    - protected:__
    - public:
    - @property
+ use getters and setters to access data
+ getter methods return the field or attribute
+ getter methods let us change the value of the field

#### Goals
+ Data security/protection
+ Code readability

_foo: Only a convention. A way for the programmer to indicate that the variable is private (whatever that means in Python).

__foo: This has real meaning. The interpreter replaces this name with _classname__foo as a way to ensure that the name will not overlap with a similar name in another class.

`__foo__`: Only a convention. A way for the Python system to use names that won't conflict with user names.

##### Name mangling
Name mangling is intended to give classes an easy way to define “private” instance variables and methods, without having to worry about instance variables defined by derived classes, or mucking with instance variables by code outside the class. Note that the mangling rules are designed mostly to avoid accidents; it still is possible for a determined soul to access or modify a variable that is considered private.


```python
# Encapsulation 
# No Data is Protected or Private
class Human:
    def __init__(self,name=None,email=None,age=None):
        self.name = name
        self.email = email
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.name!r},{self.email},{self.age})" 
        
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(name={self.name},email={self.email},age={self.age})"
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
```


```python
h = Human("Markus","markus@gmail.com",23)
print(h)
```

    Human(name=Markus,email=markus@gmail.com,age=23)



```python
#### Can we access the attribute?
h.name
```




    'Markus'




```python
#### Can we access and modify the attribute?
print(h)
h.name = "Mathew"
print(h)
```

    Human(name=Markus,email=markus@gmail.com,age=23)
    Human(name=Mathew,email=markus@gmail.com,age=23)


#### Narrative
+ If the attribute is public we can access it(getter) and modify it(setter).
+ By default every attribute that is public has these features


```python
# Encapsulation 
# No Data is Protected or Private but using the property decorator
class Human:
    def __init__(self,name=None,email=None,age=None):
        self.name = name
        self.email = email
        self.age = age
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.name!r},{self.email},{self.age})" 
        
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(name={self.name},email={self.email},age={self.age})"
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    #Create a Property from an attribute by using the @property
    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self,value):
        self.email = value
        



```


```python
#### Can we  access and modify the attribute that is now a property but it is unprotected
h = Human("Markus","markus@gmail.com",23)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    Input In [91], in <cell line: 2>()
          1 #### Can we modify the attribute that is now a property but it is unprotected
    ----> 2 h = Human("Markus","markus@gmail.com",23)


    Input In [90], in Human.__init__(self, name, email, age)
          4 def __init__(self,name=None,email=None,age=None):
          5     self.name = name
    ----> 6     self.email = email
          7     self.age = age


    Input In [90], in Human.email(self, value)
         26 @email.setter
         27 def email(self,value):
    ---> 28     self.email = value


    Input In [90], in Human.email(self, value)
         26 @email.setter
         27 def email(self,value):
    ---> 28     self.email = value


        [... skipping similar frames: Human.email at line 28 (2968 times)]


    Input In [90], in Human.email(self, value)
         26 @email.setter
         27 def email(self,value):
    ---> 28     self.email = value


    RecursionError: maximum recursion depth exceeded



```python
h = Human("Markus","markus@gmail.com",23)
print(h)
print(h.email)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    Input In [85], in <cell line: 1>()
    ----> 1 h = Human("Markus","markus@gmail.com",23)
          2 print(h)
          3 print(h.email)


    Input In [81], in Human.__init__(self, name, email, age)
          4 def __init__(self,name=None,email=None,age=None):
          5     self.name = name
    ----> 6     self.email = email
          7     self.age = age


    Input In [81], in Human.email(self, value)
         26 @email.setter
         27 def email(self,value):
    ---> 28     self.email = value


    Input In [81], in Human.email(self, value)
         26 @email.setter
         27 def email(self,value):
    ---> 28     self.email = value


        [... skipping similar frames: Human.email at line 28 (2968 times)]


    Input In [81], in Human.email(self, value)
         26 @email.setter
         27 def email(self,value):
    ---> 28     self.email = value


    RecursionError: maximum recursion depth exceeded


#### Narrative
* Why the RecursionError?
+ Because when you tend to change a property that is public, it will continue to call it self
till the recursion limit is up and it will result in this error
+ Hence the need to make the attribute protected or private when you want to use the property decorator


```python
# Encapsulation
class HumanSecure:
    def __init__(self,name=None,email=None,age=None):
        self.name = name    # public
        self._email = email # protected
        self.age = age
        self.__locations = [] #private
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.name!r},{self.email},{self.age})" 
        
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(name={self.name},email={self.email},age={self.age})"
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    
    #Create a Property from an attribute by using the @property
    # the getter method: helps to access the protected or private attribute
    @property
    def email(self):
        return self._email #must be a protected attrib _email not email
    
    # the setter method: helps to modify or set the protected or private attribute
    @email.setter
    def email(self,value):
        self._email = value
        


    

```


```python
#### Can we access and modify the attribute that is now a property but it is protected
h = HumanSecure("Markus","markus@gmail.com",23)
print(h)
```

    HumanSecure(name=Markus,email=markus@gmail.com,age=23)



```python
#### Can we access and modify the attribute that is now a property but it is protected
print(h.email)
h.email = "mathew@gmail.com"
print(h.email)
```

    markus@gmail.com
    mathew@gmail.com


#### Narrative
+ One of the usefulness of encapsulation is data protection 
+ This prevent recursion error

### Creating Properties From Attributes in Class
+ An attribute can be converted into a property by two methods
  - @property
  - property(fget,fset,fdel,doc)



```python
### Using the Property() Function
class Human2:
    def __init__(self,name=None,email=None,age=None):
        self.name = name    # public
        self._email = email # protected
        self.age = age
        self.__locations = [] #private
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.name!r},{self._email},{self.age})" 
        
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(name={self.name},email={self._email},age={self.age})"
    
    def get_email(self):
        return self._email
    
    def set_email(self,value):
        self._email = value
        
    def del_email(self):
        del self._email
     
    # Create A property using the property() for email attribute
    email = property(get_email, set_email, del_email) 
```


```python
h2 = Human2("Matt","matthew@gmail.com",12)
print(h2)
```

    Human2(name=Matt,email=matthew@gmail.com,age=12)



```python
# Access and modifying the email
print(h2.email)
print(h2)
h2.email = "example@gmail.com"
print(h2)
```

    matthew@gmail.com
    Human2(name=Matt,email=matthew@gmail.com,age=12)
    Human2(name=Matt,email=example@gmail.com,age=12)



```python
h2 = Human2("Matt","matthew@gmail.com",12)
print(h2)
# Access and modifying the email
print(h2.get_email())

```

    Human2(name=Matt,email=matthew@gmail.com,age=12)
    matthew@gmail.com



```python
h2.get_email
```




    <bound method Human2.get_email of Human2('Matt',matthew@gmail.com,12)>




```python
### Using the @property decorator
# Encapsulation
class Human3:
    def __init__(self,name=None,email=None,age=None):
        self.name = name    # public
        self._email = email # protected
        self.age = age
        self.__locations = [] #private
        
    def __repr__(self):
        "For Developers showing them how to create this class object"
        return f"{self.__class__.__name__}({self.name!r},{self.email},{self.age})" 
        
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(name={self.name},email={self.email},age={self.age})"
    
    def create_password(self,value):
        return f"{self.last_name}{self.age}{value}"
    
    
    #Create a Property from an attribute by using the @property
    # the getter method: helps to access the protected or private attribute
    @property
    def email(self):
        return self._email #must be a protected attrib _email not email
    
    # the setter method: helps to modify or set the protected or private attribute
    @email.setter
    def email(self,value):
        self._email = value
        


    

```


```python
h3 = Human3("Matt","matthew@gmail.com",12)
print(h3)
# Access and modifying the email
print(h3.email)
print(h3)
h3.email = "example@gmail.com"
print(h3)
```

    Human3(name=Matt,email=matthew@gmail.com,age=12)
    matthew@gmail.com
    Human3(name=Matt,email=matthew@gmail.com,age=12)
    Human3(name=Matt,email=example@gmail.com,age=12)



```python

```


```python
### Association
Association means the act of establishing a relationship between two unrelated classes. 
```

### Composition
It defines a strong type of relationship. It can be defined as when a class can reference one or more objects of another class inside its instance variable.
Composition is a concept that models a `has a` relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component.

In composition, objects can not exist independently.
Composition is a stricter form of aggregation. It occurs when the two classes you associate are mutually dependent and can’t exist without each other.
+ For example, take a Car and an Engine class. A Car cannot run without an Engine, while an Engine also can’t function without being built into a Car. This kind of relationship between objects is also called a PART-OF relationship.
+ Composite
+ Component


Composition allows you to express that relationship by saying a Horse has a Tail.
Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes.
This provides better adaptability to change and allows applications to introduce new requirements without affecting existing code.
Composition:delegate the work


```python
# composite
class Student:
    def __init__(self,first_name,student_id):
        self.first_name = first_name
        self.student_id = student_id
        self.address = None
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(first_name={self.first_name},student_id={self.student_id},address={self.address})"

# component ( Address of Student : a Student HAS A Address)
class Address:
    def __init__(self,street, city):
        self.street = street
        self.city = city
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}(street={self.street},city={self.city})"
        
                     
```


```python
s1 = Student("Peter",234)
print(s1)
```

    Student(first_name=Peter,student_id=234,address=None)



```python
# Plugin the Address
addr1= Address("Wall Street","Manhattan")
print(addr1)
```

    Address(street=Wall Street,city=Manhattan)



```python
print(s1.address)
```

    None



```python
s1.address = addr1
```


```python
print(s1)
```

    Student(first_name=Peter,student_id=234,address=Address(street=Wall Street,city=Manhattan))


#### Narrative
+ The Address is initialized when the student is initialized because it is part of the Student Class
+ When you delete the student object the address is also deleted

#### Using Composition Instead of Inheritance
+ Implement a Stack: FILO


```python
class Stack(list):
    def push(self,item):
        self.append(item)
```


```python
s = Stack()
s.push(4)
s.push(1)
print(s)
```

    [4, 1]



```python
# Get the last out using pop (supposed to be  4)
s.pop()
print(s)
```

    [4]



```python
# Check out the side effect of inheritance
len(dir(s))
```




    51




```python
# Same as that of a list
len(dir(list))
```




    47




```python
s[0]
```




    4



#### Narrative
+ A stack doesnt allow insertion and slicing

#### Fixing Using Composition : a stack has a list instead of a stack is a type of list


```python
class Stack:
    def __init__(self,container=list()):
        self._items = container
    
    def __str__(self):
        "For Regular Users showing them what they need to know and what is contains"
        return f"{self.__class__.__name__}({self._items})"
        
        
    def push(self,item):
        self._items.append(item)
        
    def pop(self):
        return self._items.pop()
```


```python
s = Stack()
s.push(4)
s.push(1)
print(s)
```

    Stack([4, 1])



```python
# Now you cannot slice or index
s[0]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [188], in <cell line: 1>()
    ----> 1 s[0]


    TypeError: 'Stack' object is not subscriptable



```python
s.pop()
print(s)
```

    Stack([4])


### Abstraction

#### Goal of Abstraction
+ Code reusability
+ Flexibility of implementation
+ Multiple Inheritance


```python
# get the actual data of an attribute  of a class
getattr(p,'first_name')
```




    'Mark'



#### When to Use ABC in Python
abc: abstract base class


```python

```
