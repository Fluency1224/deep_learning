#/usr/bin/env python
#coding:utf-8
import numpy as np
import theano.tensor as T
import theano

state = theano.shared(np.array(0,dtype=np.float64), 'state')
inc = T.scalar('inc', dtype=state.dtype)
accumulator = theano.function([inc], state,updates=[(state,state+inc)])

#to get variable
print(state.get_value())
accumulator(1)
print(state.get_value())
accumulator(10)
print(state.get_value())
#to set variable
state.set_value(10)
print(state.get_value())

#temporarily replace shared variable with another value
tmp_func = state*2 + inc
a = T.scalar(dtype=state.dtype)
skip_shared = theano.function([inc,a],tmp_func,givens=[(state,a)])
print(skip_shared(2,3))
print(state.get_value())