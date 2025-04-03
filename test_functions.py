import random
import unittest
from io import StringIO
from test_base import captured_io
import mastermind

class MyTestCase(unittest.TestCase):
 
    def test_create_code(self):
        '''This function is testing the function create_code() from mastermind.py, it 
           checks it a 100 times

            local variable:
            --------------
            
            - test_code : Type --> list (expected to be a list) : definition --> It's value its
            what is returned by the create_code function from mastermind

            - message_range : Type --> str : definition --> error message for when the digits
            in the code are out of range of 1-8

            - message_duplicates : Type --> str : definition --> error message for when the
            code contains duplicates 

            Testing:
            =======

            - Test if the length of the code is a 4 : If length == 4 -> Test Pass
            
            - Test if the date type returned by the code is a list or not : 
              If code type === list --> Test Pass 
            
            - Test if each digit in the code is within range 1 to 8 : If all characters in the
              code range between 1 to 8 --> Test Pass 
            
            
            '''
        message_range = "Some digit(s) in create code are out range of 1-8"
        message_duplicates = "The created code has duplicates"       
        for i in range(0,100):
            test_code = mastermind.create_code()
            self.assertEqual(len(test_code), 4)
            self.assertEqual(type(test_code),list)
            self.assertEqual(len(set(test_code)), 4,message_duplicates)
            self.assertTrue(0 not in test_code,message_range)
            self.assertTrue(9 not in test_code,message_range)
    
    
    def test_get_answer(self):

        '''This function is testing output from the function get_answer_input() when the 
           input is incorrect from mastermind.py

            local variables
            --------------

            - output : Type --> string : definition --> Gets the terminal outputs returned by
            the function get_answer_input()
            - return_output : Type --> string (expected to be a string when returned by the 
            function) : definition --> The object returned by get_answer_input from mastermind

            Testing
            ======

            Test Case 1
            -----------
            - With an input of 12 followed by 1234
            - Test if the user inputs a string containing digits only and has less than 4 
              characters

            - The user must be prompted to input again after seeing the message saying Please 
              enter exactly 4 digits

            - Then asked for the input another input, the user inputs a string containing only
              4 digits and characters --> Test Pass

            
            Test Case 2
            -----------
            - With an input of 1234567 followed by 1234
            - Test if the user inputs a string containing digits only and has more than 4
              characters

            - The user must be prompted to input again after seeing the message saying Please
              enter exactly 4 digits

            - Then asked for the input another input, the user inputs a string containing only
              4 digits and characters --> Test Pass 

            
            Test Case 3
            -----------
            - With an input of abcd followed by 1234
            - Test if the user inputs a string containing digits only and has less than 4
              characters
            - The user must be prompted to input again after seeing the message saying Please
              enter exactly 4 digits
            - Then asked for the input another input, the user inputs a string containing only
              4 digits and characters --> Test Pass
             
            Test Case 4
            -----------
            - With input of a2b7 followed by 1234
            - Test if the user inputs a string mixed with digits and other
              characters
            - The user must be prompted to input again after seeing the message saying Please
              enter exactly 4 digits
            - Then asked for the input another input, the user inputs a string containing only
              4 digits and characters --> Test Pass

            Test Case 5
            -----------
            - With input of 1234
            - Checks if the function get_answer_input returns a str containing digits only and
              its length is 4
        
        '''
        #Test Case 1
        with captured_io(StringIO('12\n1234')) as (out, err):
            mastermind.get_answer_input()
            output = out.getvalue().strip()
        self.assertEqual(output, 'Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code:')

        #Test Case 2
        with captured_io(StringIO('1234567\n1234')) as (out, err):
            mastermind.get_answer_input()
            output = out.getvalue().strip()
        self.assertEqual(output, 'Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code:')
        
        #Test Case 3
        with captured_io(StringIO('abcd\n1234')) as (out, err):
            mastermind.get_answer_input()
            output = out.getvalue().strip()
        self.assertEqual(output, 'Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code:')
    
        #Test Case 4
        with captured_io(StringIO('a2b7\n1234')) as (out, err):
            mastermind.get_answer_input()
            output = out.getvalue().strip()
        self.assertEqual(output, 'Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code:')
        
        #Test Case 5
        with captured_io(StringIO('1234\n')) as (out, err):
            return_input = mastermind.get_answer_input()
        self.assertEqual(type(return_input),str)
        self.assertTrue(return_input.isdigit())
        self.assertEqual(len(return_input),4)


       
    def test_check_correctness(self):
        '''This function is testing the function 
        check_correctness(turns,correct_digits_and_position) from mastermind.py

        local variables
        --------------

        - ret_bool : Type --> bool : definition --> Is the bool value returned by 
        check_correctness
        - message : Type --> str : definition --> Is the message printed out when the test
        is not passing
        
        Testing
        =======
        NOTE: For each Test case a random number of turns(range from 0-11) is
        passed as a pareameter because it is independent of what is being
        tested, we only need correct_digits_and_position
        
        Test Case 1:
        -----------

        - Test if True is returned when the code is guessed correctly : 
        If correct_digits_and_position == 4
         --> check_correctness(randomint,4) == True --> Test Pass

        Test Case 2:
        ------------

        - Test if False is returned when the code is not guessed correctly :
          If correct_digits_and_position != 4
           --> check_correctness(randomint,num) == False --> Test Pass
        - num is an integer ranging from 0 to 3
        - It has a message when the case fails that it prints out
        '''

        #Test Case 1
        with captured_io(StringIO()) as (out, err):
           ret_bool = mastermind.check_correctness(random.randint(0,11),4)
        message = f'''Your code returned False when it was supposed to return\
 True for correct digits number of digits == 4'''
        self.assertTrue(ret_bool,message)
        
        #Test Case 2
        for num in range(4):
            with captured_io(StringIO()) as (out, err):
                ret_bool = mastermind.check_correctness(random.randint(0,11),num,)
            message = f'''Your code returned True when it was supposed to return\
 False for correct digits number of digits == {num}'''
            
            self.assertFalse(ret_bool,message)
    

    

    def test_take_turn(self):

        '''This function tests the function take_turn(code) from mastermind.py\
            
            local variable
            --------------

            - code : Type --> list : defaultvalue --> [1,2,3,4] : definition --> We passed it
            on take turn as the generated code on each test case
            - message : Type --> str : definition --> Is the message printed out when the test
            is not passing

            TESTING
            =======
            
            Test Case 1
            -----------
            - With input of 1234
            - Checks if take turn returns a tuple containing: If return_variable type is
              tuple --> Test Pass
            
            Test Case 2
            -----------

            - With input of 1234
            - Checks if take turn return a data type of length 2: if length of return_variable
              is 2 --> Test Pass 
            
            Test Case 3
            -----------
            
            - With input of 1234
            - if the input is the same as code does it return a tuple of (4,0)
            - If take_turn(code) with input 1234 --> return (4,0) --> Test Pass

            Test Case 4
            -----------
            - With input of 1245
            - If the input has 2 correct digits that are in the right place and 1 correct
              digit in a wrong place
            - If the functions returns a tuple of (2,1) --> Test Pass

            Test Case 5
            -----------
            - With input of 5678
            - If the input has 0 correct digits that are in the right place and 0 correct
              digit in a wrong place
            - If the functions returns a tuple of (0,0) --> Test Pass


        '''
        code = [1,2,3,4]
    
        with captured_io(StringIO('1234\n')) as (out, err):
            
            return_variable = mastermind.take_turn(code)
        
        #Test Case 1
        self.assertEqual(type(return_variable), tuple)
        
        #Test Case 2
        message = "Your take turn function is not returning 2 variables"
        self.assertEqual(len(return_variable),2,message)
        
        #Test Case 3
        message = "Your function is not returning the valid number of correct digits in correct\
place and/or number correct digits but in a wrong place "
        self.assertEqual((4,0),return_variable, message)

        #Test Case 4
        with captured_io(StringIO('1245\n')) as (out, err):
            return_variable = mastermind.take_turn(code)
        self.assertEqual((2,1),return_variable,message)

        #Test Case 5
        with captured_io(StringIO('5678\n')) as (out, err):
            return_variable = mastermind.take_turn(code)
        self.assertEqual((0,0),return_variable,message)


if __name__ == "__main__":
    unittest.main()
        
