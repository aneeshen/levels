import datetime as dt

def get_exp_l_c_s_value(b,t,msbs,ref_lcs):#*2
    at_time=dt.time(hour=13,minute=0)
    if t>=at_time:
        if b<=msbs:
            lcs=ref_lcs+5
        else:
            lcs=ref_lcs+((b-msbs)*1)
    else:
        if b<=msbs:
            lcs=ref_lcs
        else:
            lcs=ref_lcs+(b-msbs)*3
    return lcs

def get_normal_lcs_value(b,ref_lcs):
    if b<=msbs:
        lcs=ref_lcs
    else:
        lcs=ref_lcs+(b-msbs)*3
    return lcs