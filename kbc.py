print("          wellcome to the con banega karore pati        ")
print()
question_list = [
    "How many continents are there?",          
    "What is the capital of India?",           
    "NG mei kaun se course padhaya jaata hai?"  
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
	print(i+1,"question")
	print("*",question_list[i])
	j=0
	while j<len(options_list[i]):
			print(j+1,options_list[i][j])
			j+=1
	ans=int(input("choose the correct options: "))
	if ans==solution_list[i]:
		print("*******your answer is corect*******")
	else :
		print("*****your answer is wrong*****")
		break
	print()
	i+=1