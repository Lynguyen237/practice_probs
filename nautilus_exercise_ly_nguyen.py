# Improve the following code for:
# ● Style
# ● Simplicity
# ● Maintainability

# ==== Refactored code ===

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
