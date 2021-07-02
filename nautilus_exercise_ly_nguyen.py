# Improve the following code for:
# ● Style
# ● Simplicity
# ● Maintainability

# ==== Refactored codes - Option 1
''' 
Cerate smaller helper functions and eliminate unnecessary return False statements 
This is the closet to the original code with clear if/else statements for each condition A, B, C, D
'''

def f():
    """ Main function """
    if A:
        z()
        b_helper()
    else:
        s()

    return False


def d_helper():
    """ Helper function if condition D is met """
    if D:
        w()
        return True
    else:
        v()


def c_helper():
    """ Helper function if condition C is met """
    if C:
        x()
        d_helper()
    else:
        u()


def b_helper():
    """ Helper function if condition B is met """
    if B:
        y()
        c_helper()
    else:
        t()


# ==== Refactored codes - Option 2
''' 
Create smaller helper functions and eliminate else statements. 
In each function, we quickly return False if a given condition is not met.
'''

def f():
    """ Main function """
    if not A:
        s()
        return False
    
    z()
    b_helper()


def d_helper():
    """ Helper function for condition D """
    if not D:
        v()
        return False
    
    w()
    return True


def c_helper():
    """ Helper function for condition C """
    if not C:
        u()
        return False
    
    x()
    d_helper()


def b_helper():
    """ Helper function for condition B """
    if not B:
        t()
        return False
    
    y()
    c_helper()


# ===== Original codes 
def f():
    if A:
        z()
        if B:
            y()
            if C:
                x()
                if D:
                    w()
                    return True
                else:
                    v()
                    return False
            else:
                u()
                return False
        else:
            t()
            return False
    else:
        s()
        return False
