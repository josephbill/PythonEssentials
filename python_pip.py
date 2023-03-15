# PIP  : package manager for python packages /  modules
# Python Packages /Modules  : ready code / code library /
# benefits : file containg a set of functions you might want to use in your application.
# if the modules are not built in like pip. We simply download the package
# pip install packagename
# pip install camelcase
# to use a package , simply call it using the import keyword
import camelcase

c = camelcase.CamelCase()
text = "joseph mbugua"
print(c.hump(text))