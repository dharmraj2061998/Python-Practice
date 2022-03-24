# package is container for multiple modules means files. which we can reuse.
# In file system the package is like directory of folder.
# package is the directory in which we include related modules.

# import ecommerce.shipping

# ecommerce.shipping.cal_shipping()

# we can use the above way but its still somwhere not preferable.so we
# have to use second way thats by use of from keyword.

# from ecommerce.shipping import cal_shipping

# cal_shipping()

# for one function we can use above syntax but if functions are more than one
# then we can use it by importing with use of ","

from ecommerce.shipping import cal_shipping,cal_tax

cal_tax()
cal_shipping()
cal_tax()
cal_shipping()