# Improve the following code for:
# ● Style
# ● Simplicity
# ● Maintainability

# ==== Refactored code ===

def f():
    """ Main function """
    if not A:
        s()
        return False
    
    z()
    b_helper()


def d_helper():
    """ Helper function if condition D is met """
    if not D:
        v()
        return False
    
    w()
    return True


def c_helper():
    """ Helper function if condition C is met """
    if not C:
        u()
        return False
    
    x()
    d_helper()


def b_helper():
    """ Helper function if condition B is met """
    if not B:
        t()
        return False
    
    y()
    c_helper()


# ===== Original ====
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
