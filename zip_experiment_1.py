list1=['wjufn','jfiw','eifwhuwffehhha']
list2=[9,0,3]
paired= zip(list1, list2)
paired_new= sorted(paired, key= lambda pair: len(pair[0]), reverse=True)        #REVERSEEEE 
list1_new, list2_new= list(zip(* paired_new))
print(list1_new, list2_new, sep='\n')
