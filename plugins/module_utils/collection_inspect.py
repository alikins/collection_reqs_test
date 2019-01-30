
def get_dunders(_globals, force_serializable=False):
    '''Pass in a the dict returned from globals() from caller

    ie, call like:

        dunders = get_dunders(globals())
    '''
    dunder_candidates = ('__cached__', '__file__', '__loader__',
                         '__name__', '__package__', '__spec__')
    # _globals = globals()

    not_defined_blurb = '_IS_NOT_DEFINED'

    data = {}
    for candidate in dunder_candidates:
        value = _globals.get(candidate,
                             "%s%s" % (candidate.upper(), not_defined_blurb))
        if force_serializable:
            data[candidate] = "%r" % value
        else:
            data[candidate] = value

    return data
