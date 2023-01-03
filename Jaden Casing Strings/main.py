def to_jaden_case(string):
    '''
    Function to return string
    in the style Jaden Smith
    would write it in.
    
    Return: 
        Modified string.
    
    Params:
        string - Any string user passes in.
    '''
    
    split_string = string.split()
    if len(split_string) == 0:
        return string

    def first_upper(s):
        '''
        Helper function to capitalize
        first letter and uncapitalize
        other letters for string s.
        
        Return:
            Modified string s.
        
        Params:
            s - Input string.
        '''
        ret = ""
        if len(s) > 0:
            ret += s[0].upper()
            ret += s[1:].lower()
        
        return ret
        
    sol = ""      
    for word in split_string[:-1]:
        sol += first_upper(word) + ' '
    sol += first_upper(split_string[-1])
    
    return sol
