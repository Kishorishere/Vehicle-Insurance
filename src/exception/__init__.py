import sys
import logging

def error_message_detail(error:Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name,line number and the error message.


    Args:
        error (Exception): The exception that occurred.
        error_detail (sys): The sys module to access trackback details.
        
    Returns:
        str: A formatted error message string.
    """
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename # Gives the file name

    line_number = exc_tb.tb_lineno
    #Formatted error message based on above details
    error_message = f"Error occured in python script : [{file_name}] at line number [{line_number}]:{str(error)} "
    #Log the error 
    logging.error(error_message)

    return error_message

class MyException(Exception):
    """Custom exception class for handling  errors in the US visa application.
    """
    def __init__(self, error_message: str, error_detail: sys):
        """Initializes the USVisaException
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)


    def __str__(self):
        """
        Returns:
               the string representation of the error message.
        """
        return self.error_message

