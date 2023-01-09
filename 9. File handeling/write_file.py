'''
writing into file
================
write(): This function is used to write data into file.

syntax:

    file_pointer.write(data)



      data.txt                         write_file.py                   IDLE Shell
  ----------------                --------------------              --------------
                      write()                             input()   Enter Mobile No:
                   <-------------   mn=input()         <-----------

'''
fp=open("data.txt","w")
#d="This is  first line in the file"
#fp.write(d)
mn=input("enter mobile number:")
fp.write(mn)
fp.close()

'''
If a file is open in write mode and it has previous data,
then new data get overwritten on the previous data.


OTP generated
1)Send to user mobile number
2)store in database or file in web application.

when user enter OTP

For verification
OTP entered by User is matched with the OTP stored in File.
If above condition is true then user mobile is verified.
'''
