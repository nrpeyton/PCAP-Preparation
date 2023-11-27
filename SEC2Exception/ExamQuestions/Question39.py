'''
What is the output of the following snippet?


try:
    print('start ', end='')
    raise ValueError
except IOError:
    print('io error ', end='')
except:
    print('general error ', end='')
    raise RuntimeError
except Exception:
    print('exception ', end='')
finally:
    print('end')
'''

# Answer: 