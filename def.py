class CreateMember():
	def __init__(self,name="",surname="",age="",id="",company=""):
		self.name = name
		self.surname = surname
		self.age = age
		self.id = id
		self.company = company
	def members(self):

		print("""
::::::::::::::::::::::::
	Name .: %s
	Surname .: %s
	Age .: %s 
	Id .: %s
	Company .: %s
::::::::::::::::::::::::
			"""%(self.name,self.surname,self.age,self.id,self.company))

	def pay(self):
		membersz = ["CANON","ASUS","MSI","ALIENWARE"]
		company = self.company
		for i in membersz:
			if(i == self.company):
				print("Pay.: 30.200 $")
			elif(i == self.company):
				print("Pay.: 2.300 $")
			elif(i == self.company):
				print("Pay.: 200.340 $")
			elif(i == self.company):
				print("Pay.: 19.033 $")
def createid(createid):
	return "0Pure"+createid 


name = input("Enter the name of member.: ")
surname = input("Enter the surname of member.: ")
age = input("Enter the age of member.: ")
id = input("Enter the id of member.: ")
company = input("Enter the name of company .: ")
id = createid(id)

CreateMember(name,surname,age,id,company).members()
CreateMember(name,surname,age,id,company).pay()