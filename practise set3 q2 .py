# Q2 --- Write a python program to fill in a letter template given below with name and date.
# letter = '''
        #Dear < |Name| >,
        #You are selected!
        # <|Date|>
        # '''

# Ans ---
# signing in
letter = '''
        Dear < |Name| >,
        You are selected!
         <|Date|>
         '''
replaced_string = letter.replace("Name","Pritish").replace("Date","5 JUNE 2004")
print(replaced_string)
# signing off 
