#Assignment of variable and creating a list
# In eu-west-2 they want to provision this ami  - ami- 0d729d2846a86a9e7, 
# in eu-west-1 this ami-  ami-0c1bc246476a5572b
# In, us-east-1 this ami ami-0022f774911c1d690



ami_list = ["ami- 0d729d2846a86a9e7","ami- 0c1bc246476a5572b","ami- 0022f774911c1d690"] 
print(ami_list)



# # #for loop
ami_list = ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"] 
for ami in ami_list:
       print("ami list")
       print(ami)
    
     

# # # Assigning a variable and creating a Tuple
regions_tuple = ["ami- 0d729d2846a86a9e7","ami-0c1bc246476a5572b","ami-0022f774911c1d690"]
for ami in regions_tuple:
       print(ami)
if ami == "ami- 0d729d2846a86a9e7":
        print ("The region is equal to us-east-1")



# # Assigning a variable and creating dictionary    
regions_ami_dict = {"eu-west-2" :"ami- 0d729d2846a86a9e7","eu-west-1" :"ami-0c1bc246476a5572b","us-east-1" : "ami-0022f774911c1d690"}   

for key,Value in regions_ami_dict.items():
      print(f"key is: (key) and value: (value)")
