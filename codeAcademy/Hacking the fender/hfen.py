# Open "new_passwords.csv" in write mode
with open('new_passwords.csv', 'w') as new_passwords_obj:
    # Slash Null's signature
    slash_null_sig = """
     _  _     ___   __  ____             
    / )( \   / __) /  \(_  _)            
    ) \/ (  ( (_ \(  O ) )(              
    \____/   \___/ \__/ (__)             
     _  _   __    ___  __ _  ____  ____  
    / )( \ / _\  / __)(  / )(  __)(    \ 
    ) __ (/    \( (__  )  (  ) _)  ) D ( 
    \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
            ____  __     __   ____  _  _ 
     ___   / ___)(  )   / _\ / ___)/ )( \
    (___)  \___ \/ (_/\/    \\___ \) __ (
           (____/\____/\_/\_/(____/\_)(_/
     __ _  _  _  __    __                
    (  ( \/ )( \(  )  (  )               
    /    /) \/ (/ (_/\/ (_/\             
    \_)__)\____/\____/\____/
    """
    # Write the signature to the file
    new_passwords_obj.write(slash_null_sig)
