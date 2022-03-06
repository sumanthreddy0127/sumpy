# sorted
# b=[4,9,1,6]
# b.sort()
# print(b)
# print(sorted([34,78,120,7]))
# print(sorted([12,4,1,45]))py #[1, 4, 6, 9][7, 34, 78, 120][1, 4, 12, 45]

# all()
# print(all([True,3,8]))
# print(all([True,'',9,7]))
# print(all([True,' ',2,7]))
# print(all([True,False,2,7]))
# print(all([True,False,3,8,0]))
# print(all([False,False,3,8,None]))

#any()

# print(any([True,False,23])) #true
# print(any([False,False,3])) #true
# print(any([False,True,None,0])) #true

#bool()

# print(bool(False))
# print(bool(1))
# print(bool(0))
# print(bool(None))
# print(bool('bool'))
# print(bool(''))
# print(bool('  '))

#eval

# print('eval=',eval('7+8.4-5'))
# a=eval('7+9-2')
# b=eval('8+3.9-2')
# print(a,type(a))
# print(b,type(b))

#sum()

# print('sum=',sum([3,6,7,8,9]))
# print('sum=',sum([3.7,9,6,7,8,9]))

#reversed list

# for i in reversed([3,7,9,5]): # 5973
#     print(i)

#reversed tuple
# for i in reversed((45,89,23,67)):
#     print(i)

#enumerate

d=['sumanth','good','boy']
b=enumerate(d)
print(type(b))
print(dict(b))
print(list(b))
print(tuple(b))
a=enumerate(b,3)
print(list(a))

