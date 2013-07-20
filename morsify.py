#!/usr/bin/env python

import sys

#
# Contains basic functionality for converting basic text into morse
# code
#

# Ensure compatible keyboard input from both versions of Python
if sys.version_info.major < 3: input = raw_input

DOT = '.' # Default dot
DASH = '_' # Default underscore
LETTER = ' ' # Default 1 space
WORD = '   ' # Default 3 spaces
CHARSET = {
	'a': DOT + DASH,
	'b': DASH + DOT + DOT + DOT,
	'c': DASH + DOT + DASH + DOT,
	'd': DASH + DOT + DOT,
	'e': DOT,
	'f': DOT + DOT + DASH + DOT,
	'g': DASH + DASH + DOT,
	'h': DOT + DOT + DOT + DOT,
	'i': DOT + DOT,
	'j': DOT + DASH + DASH + DASH,
	'k': DASH + DOT + DASH,
	'l': DOT + DASH + DOT + DOT,
	'm': DASH + DASH,
	'n': DASH + DOT,
	'o': DASH + DASH + DASH,
	'p': DOT + DASH + DASH + DOT,
	'q': DASH + DASH + DOT + DASH,
	'r': DOT + DASH + DOT,
	's': DOT + DOT + DOT,
	't': DASH,
	'u': DOT + DOT + DASH,
	'v': DOT + DOT + DOT + DASH,
	'w': DOT + DASH + DASH,
	'x': DASH + DOT + DOT + DASH,
	'y': DASH + DOT + DASH + DASH,
	'z': DASH + DASH + DOT + DOT
}

def morsify(text):
	'''
	Convert a piece of text and return its morse code equivalent
	
	Any unrecognised characters are stripped
	'''
	code = ''

	for c in text.lower():
		if c == '\n':
			code += c
		elif c == ' ':
			code += WORD
		else:
			try:
				code += CHARSET.get(c) + LETTER
			except KeyError:
				pass

	return code

def test_morsify():
	'''Test that the morsify function is working as intended'''
	print('test_morsify():')
	print('hello world = %s' % morsify('hello world'))
	print('sos = %s' % morsify('sos'))

if __name__ == '__main__':
	test_morsify()
