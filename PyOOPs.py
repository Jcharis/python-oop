#!/usr/bin/env python
# coding: utf-8

# ### Object Oriented Programming in Python
# + Error Based Learning
# By Jesse E.Agbemabiase (JCharis)
# * Jesus Saves @JCharisTech

# #### Outline
# + Ways to Create Objects
# + OOP Principles
#     - Inheritance (Multiple Inheritance,Multi-Level,Supervised Inheritance)
#     - Encapsulation
#     - Polymorphism
#     - Abstraction
#     - Composition
# + Gotchas

# #### Structure using UML
# + Person(fname,lastname,age)
# + Pupil(p..,16yrs,p1-p9)
# + Student(p.17yrs,f1.4,major)
# + Teacher(Full Time.Part time,visiting,TA)
# + HeadMaster
# + Counselor
# + Manager (HR,
# + Accountant
# + 

# #### Everything in python is a type and an object
# + it is an object of the base class `type`
# 
# ##### What is an object and what is a class?
# + A class is a blueprint (like a questionaire that you have to fill with data or information
# + An instance is a copy of the class with actual values (your specific copy is an instance of the class; it contains actual information relevant to you)

# In[2]:


a = "hello python"
b = 1
c = [1,2,4]
d = (1,3,5)
print("Type of a string",type(a))
print("Type of an integer",type(b))
print("Type of a list",type(c))
print("Type of a tuple",type(d))


# In[3]:


print(type(str))
print(type(int))
print(type(list))
print(type(tuple))
print(type(object))


# In[4]:


# what is the type of any class/object in python?ans type
type(type(str))


# ##### Hence the hierarchy is 
# object => class => type 

# In[5]:


# the type of an object is a type
print(type(object))


# #### Creating a Class in Python
# + A Class is a blueprint or cookiecutter for creating an object
# + An object is anything that has state(data coming from attributes of something) and behavior(methods)

# In[6]:


# Method 1: Using the constructor approach
# the __init__() initializes the arguments when the class is used to create an object
class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name


# In[7]:


p = Person("Jesse","JCharis")
print(p)
print("Check the type",type(p))


# ##### Narrative
# + we have got the same results as the initial types (<class 'type'> === <class '__main__.Person'>)
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

# In[8]:


# Why __new__?: for creating a new instance
# Why __init__?: for initializing a new instance
class Person2:
    def __new__(cls):
        print("Creating instance")
  
    # It is not called
    def __init__(self):
        print("Init is called")


# In[9]:


print(Person2())


# #### Narrative
# + When you usee `__new__`, without Super(), the instance are created but not initialized

# In[10]:


class Person2:
    def __new__(cls):
        print("Creating instance")
        return super(Person2, cls).__new__(cls)
  
    # It is called and hence an instance is initialized as you can see below
    def __init__(self):
        print("Init is called")


# In[11]:


print(Person2())


# #### Components of a Class
# + instance of an object = state + behavior
# + object = attributes + methods
# * state: It is represented by the attributes of an object. It also reflects the properties of an object.
# * behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
# 

# In[12]:


class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# In[13]:


##### Creating an Object
p = Person("Jesse","JCharis",25)
print(p)


# ##### Narrative
# + An object of Person class was created at 0x7f4808d5aec0 
# + What does the 0x7f4808d5aec0 mean?
#   - It is a hexdecimal number
#   - That is the Memory address allocated for that object to identify(id) it hence when we
#     use id() on that object we must get the same value
# + The id is assigned to the object when it is created.
# + The id is the object's memory address, and will be different for each time you run the program. (except for some object that has a constant unique id, like integers from -5 to 256)

# In[17]:


# Convert the hex to decimal
# ast.literal_eval('0x7f4808d5aec0')
int(0x7f8848a51a80)


# In[15]:


# Get the memory address or identification of that object
id(p)


# In[16]:


#### Getting the attributes
#### the attributes stores data or state these are the variables
p.first_name


# In[18]:


#### How to get all attributes or instance variables of an object created 
vars(p)


# In[19]:


#### How to get all attributes or instance variables of an object created 
dir(p)


# #### Narrative: Difference between var() and dir()
# `vars()` Function: 
# + It displays the attribute of an instance in the form of a dictionary.
# + Only works for object that implement __dict__ function
# 
# `dir()` Function: 
# + It displays the instance attributes and the class attributes as well. 
# + It also displays the attributes of its ancestor classes.
# + It is not limited to an instance.
# 
# 

# In[20]:


#### How to get all attributes or instance variables of an object created  var() == object.__dict__
p.__dict__


# #### User Experience(UX and UI) of Class 
# + Developer: `__repr__()`
# + Regular User:`__str__()`

# In[21]:


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


# In[22]:


p = Person("Jesse","JCharis",25)
print(p)


# In[23]:


# For Developers
# Notice the quotation marks on the first this is because of !r without it you will not see the quotation marks
p


# #### Creating Methods For a Class
# + A Method is a function for a class that controls the behavior of the object
# + instance method: fxns that takes self as first param and controls the behavior of the object instance hence it can
# access the instance attributes or variables
# + class method: fxn that takes cls as first param and have access to the class itself
#     - A class method can access or modify the class state while a static method can’t access or modify it.
#     - convention is to use `_from_`
#     - uses @classmethod
# + static method: fxns that doesnt take either self or cls as first params and they are used as utility functions
#     - they can actually live outside the class but we keep them here
#     - uses @staticmethod
#     

# #### Instance Methods

# In[24]:


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
        


# In[25]:


p = Person("Mark","Twain",57)
print(p)


# In[26]:


p.create_email()


# #### Static Methods: utility fxns

# In[27]:


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
        


# In[28]:


Person.get_age_group(43)


# #### Class Methods

# In[29]:


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
        
        


# In[30]:


Person.to_Birth_Year("Jesse","J",25)


# In[31]:


Person.from_Birth_Year("Jesse","J",2000)


# In[32]:


# Bound method  occurs when you omit the () the fxn call
# What does this tells us?: it appears that we are accessing it like an attributes
# every method can be made to behave like an attribute via properties
p.create_email


# ### OOP Principles
# + Encapsulation
# + Inheritance
# + Polymorphism
# + Abstraction
# + Aggregation
# + Composition
# + Association

# ### Inheritance
# + It allows a class to inherit or acquire all the features(methods,attributes) of its parents class
# * Inheritance models what is called an is a relationship
# 
# 
# 
# #### Goals
# + Code reuse
# + Code readability
# + DRY

# In[33]:


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
        


# In[34]:


# Check Full Inheritance
pu = Pupil("Peter","Pan",12)
print(pu)


# #### Narrative
# + Notice the repr produce the same form as the base class
# + How do we fix that

# In[38]:


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
        


# In[39]:


# Check Full Inheritance
pu = Pupil("Peter","Pan",12)
print(pu)


# In[40]:


# Check Overiding
s = Student("Peter")


# In[41]:


print(s)


# #### Narrtive
# + Why the AttributeError?
# Because it is inheriting from the Parent class that has the last name hence we have to overide those methods too

# In[42]:


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


# In[44]:


# Check Overiding of all
s = Student("Peter")
print(s)


# #### How do we get all the parents attributes as well as the child attributes according?
# + use of super()
# + Using super() allows it to inherit all the attributes of the parent class Person and initialize them too 
# + Without assigning it below it will use the attributes from the Parent class assigned above

# In[45]:


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


# In[47]:


# Check Overiding of all
s = Student("Peter",1)
print(s)
print(s.create_email())


# In[48]:


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


# In[49]:


# Check Overiding of al
s = Student("Peter",1)
print(s)


# In[50]:


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


# In[51]:


# Check Inheritance
s = Student("Peter",1)
print(s)


# In[52]:


print(s.last_name)


# In[53]:


# Inherit all the methods too
s.create_email()


# ##### How to check if a class is subclass of another?
# Python provides a function issubclass() that directly tells us if a class is subclass of another class.

# In[54]:


issubclass(Student,Person)


# In[ ]:


### Multiple Inheritance


# In[115]:


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


# In[116]:


ta = TeachingAssistant("John","Maths",12)


# In[117]:


TeachingAssistant.__mro__


# In[118]:


### Let reverse it maybe it will fix the TypeError which occurs because it does-nt know which to use first
class TeachingAssistant(Teacher,Student):
    pass
ta = TeachingAssistant("John","Maths",12)


# In[114]:


TeachingAssistant.__mro__


# In[137]:


# Solution is to specify one first and overide it and assign them
class TeachingAssistant(Teacher,Student):
    def __init__(self,first_name,subject,department):
        Student.__init__(self,first_name,student_id=None) # make id as none
        self.subject = subject
        self.department = department
        


# In[138]:


ta = TeachingAssistant("John","Maths",12)


# In[139]:


ta


# In[140]:


ta.subject


# In[141]:


ta.department


# In[143]:


ta.student_id = 34


# In[145]:


ta.student_id


# In[ ]:


TeachingAssistant


# ### Method Resolution Order
# + MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy 
# + It is useful in Python because Python supports multiple inheritance.
# The MRO satisfies 3 properties:
# 
# + Children of a class come before their parents
# + Left parents come before right parents
# + A class only appears once in the MRO
# 

# In[55]:


### MR0
s.__class__.__mro__


# the Liskov substitution principle. 
# The principle states that “in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties of the program”.

# ### Encapsulation
# + En + capsule
# + It describes the idea of wrapping data and the methods that work on data within one unit. 
# + This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 
# + To prevent accidental change, an object’s variable can only be changed by an object’s method
# Encapsulation helps with data security, allowing you to protect the data stored in a class from system-wide access. 
# As the name suggests, it safeguards the internal contents of a class like a capsule.
# 
# ##### Summary
# + capsule
# + data security and restriction
#     - private: __
#     - protected:_
#     - public:
#     - @property
# + use getters and setters to access data
# + getter methods return the field or attribute
# + getter methods let us change the value of the field
# 
# #### Goals
# + Data security/protection
# + Code readability
# 

# In[72]:


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


# In[79]:


h = Human("Markus","markus@gmail.com",23)
print(h)


# In[76]:


#### Can we access the attribute?
h.name


# In[80]:


#### Can we access and modify the attribute?
print(h)
h.name = "Mathew"
print(h)


# #### Narrative
# + If the attribute is public we can access it(getter) and modify it(setter).
# + By default every attribute that is public has these features

# In[90]:


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
        




# In[91]:


#### Can we  access and modify the attribute that is now a property but it is unprotected
h = Human("Markus","markus@gmail.com",23)


# In[85]:


h = Human("Markus","markus@gmail.com",23)
print(h)
print(h.email)


# #### Narrative
# * Why the RecursionError?
# + Because when you tend to change a property that is public, it will continue to call it self
# till the recursion limit is up and it will result in this error
# + Hence the need to make the attribute protected or private when you want to use the property decorator

# In[92]:


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
        


    


# In[94]:


#### Can we access and modify the attribute that is now a property but it is protected
h = HumanSecure("Markus","markus@gmail.com",23)
print(h)


# In[96]:


#### Can we access and modify the attribute that is now a property but it is protected
print(h.email)
h.email = "mathew@gmail.com"
print(h.email)


# #### Narrative
# + One of the usefulness of encapsulation is data protection 
# + This prevent recursion error

# ### Creating Properties From Attributes in Class
# + An attribute can be converted into a property by two methods
#   - @property
#   - property(fget,fset,fdel,doc)
# 

# In[104]:


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


# In[98]:


h2 = Human2("Matt","matthew@gmail.com",12)
print(h2)


# In[100]:


# Access and modifying the email
print(h2.email)
print(h2)
h2.email = "example@gmail.com"
print(h2)


# In[107]:


h2 = Human2("Matt","matthew@gmail.com",12)
print(h2)
# Access and modifying the email
print(h2.get_email())


# In[108]:


h2.get_email


# In[109]:


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
        


    


# In[110]:


h3 = Human3("Matt","matthew@gmail.com",12)
print(h3)
# Access and modifying the email
print(h3.email)
print(h3)
h3.email = "example@gmail.com"
print(h3)


# In[ ]:





# In[ ]:


### Association
Association means the act of establishing a relationship between two unrelated classes. 


# ### Composition
# It defines a strong type of relationship. It can be defined as when a class can reference one or more objects of another class inside its instance variable.
# Composition is a concept that models a `has a` relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component.
# 
# In composition, objects can not exist independently.
# Composition is a stricter form of aggregation. It occurs when the two classes you associate are mutually dependent and can’t exist without each other.
# + For example, take a Car and an Engine class. A Car cannot run without an Engine, while an Engine also can’t function without being built into a Car. This kind of relationship between objects is also called a PART-OF relationship.
# + Composite
# + Component
# 
# 
# Composition allows you to express that relationship by saying a Horse has a Tail.
# Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes.
# This provides better adaptability to change and allows applications to introduce new requirements without affecting existing code.

# In[162]:


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
        
                     


# In[163]:


s1 = Student("Peter",234)
print(s1)


# In[164]:


# Plugin the Address
addr1= Address("Wall Street","Manhattan")
print(addr1)


# In[166]:


print(s1.address)


# In[167]:


s1.address = addr1


# In[168]:


print(s1)


# In[ ]:


#### Using Composition Instead of Inheritance
+ Implement a Stack: FILO


# In[169]:


class Stack(list):
    def push(self,item):
        self.append(item)


# In[171]:


s = Stack()
s.push(4)
s.push(1)
print(s)


# In[172]:


# Get the last out using pop (supposed to be  4)
s.pop()
print(s)


# In[176]:


# Check out the side effect of inheritance
len(dir(s))


# In[175]:


# Same as that of a list
len(dir(list))


# In[177]:


s[0]


# #### Narrative
# + A stack doesnt allow insertion and slicing

# #### Fixing Using Composition : a stack has a list instead of a stack is a type of list

# In[186]:


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


# In[187]:


s = Stack()
s.push(4)
s.push(1)
print(s)


# In[188]:


# Now you cannot slice or index
s[0]


# In[189]:


s.pop()
print(s)


# In[ ]:


### Abstraction



#### Goal of Abstraction
+ Code reusability
+ Flexibility of implementation
+ Multiple Inheritance


# In[192]:


# get the actual data of an attribute  of a class
getattr(p,'first_name')


# In[ ]:




