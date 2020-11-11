
def removeParenthesis(s):
	# Python3 program to simplify algebraic sing 

# Function to simplify the sing 
	Len = len(s) 

	# resultant sing of max Length 
	# equal to Length of input sing 
	res = [None] * Len
	index = 0
	i = 0

	# create empty stack 
	stack = [] 
	stack.append(0) 

	while (i < Len): 
		print('s', s)
		if (s[i] == '+'): 
			# If top is 1, flip the operator 
			res[index] = '-' if stack[-1] == 1 else '+'
			index += 1
		elif (s[i] == '-'): 
			print('stack len, i' , len(stack), index)
			res[index] = '+' if len(stack) != 0 and stack[-1] == 1 else '-'
			index += 1
		elif (s[i] == '(' and i > 0): 
			if (s[i - 1] == '-'): 

				# x is opposite to the top of stack 
				x = 0 if (len(stack) != 0 and stack[-1] == 1) else 1
				stack.append(x) 

			# append value equal to top of the stack 
			elif (s[i - 1] == '+'): 
				stack.append(s[-1]) 
		elif(s[i] == '(' and i==0):
			i+=1
			# index+=1
			continue
		# If closing parentheses pop 
		# the stack once 
		elif (s[i] == ')'): 
			stack.pop() 

		# copy the character to the result 
		else: 
			res[index] = s[i] 
			index += 1
		i += 1
	s = ''
	for r in res:
		s+= r if r is not None else ''
	return s



def simplifyExpression(s):
	
	
def simplify(s):
	print(removeParenthesis(s))

simplify('(b+c)-(c-a)')