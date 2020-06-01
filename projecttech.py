import re
import copy
import json

def scrapping_data():
        file1=open("file1.txt","r")
        file2=open("file2.txt","r")
        content_file1=file1.read()
        content_file2=file2.read()

        pattern_file1=re.compile(r'\d\d[0\W]')
        pattern_file2=re.compile(r'[0-9]+ |\d\d\d[0-9]?')
        pattern_machine=re.compile(r'[0-9a-zA-Z]+e')
        data_units=pattern_file1.findall(content_file1)
        data_cost=pattern_file2.findall(content_file2)
        machine_names=pattern_machine.findall(content_file1)
        data_units=list(map(int,data_units))
        data_cost=list(map(int,data_cost))
        return data_units,data_cost,machine_names


def main_operation(main_1,main_2,main_units,main_hour):
        
        main_2=[num*main_hour for num in main_2]
        machine_count=[]
        cost_count=[]
        digit=6
        for value in range(len(main_2)):
            duplicate=main_units
            digit-=1
            process=[]
            for value1 in range(len(main_1)-1,-1,-1):
                temp1=1
                temp2=0
                while True:
                    temp=main_1[value1]*temp1
                    if temp>duplicate or main_1[value1]==1:
                        break
                    temp2=temp
                    temp1+=1
                process.append(temp2)
                duplicate=duplicate-temp2
            process.reverse()
            temp_list=[]
            for value2 in range(len(process)-1,-1,-1):
                divide_value=process[value2]//main_1[value2]
                temp_list.append(divide_value)
            temp_list.reverse()
            result=0
            for value3 in range(len(temp_list)):
                result=result+(main_2[value3]*temp_list[value3])
            main_1.pop(digit)
            machine_count.append(temp_list)
            cost_count.append(result)
        return cost_count,machine_count
        


number_input=[]
final_result=[]
print("Enter the input: ")
user_input=input()
splitted_input=user_input.split(" ")
for value in splitted_input:
    if value.isdigit():
        number_input.append(value)
units,hour=map(int,number_input)
data_units,data_cost,type_machines=scrapping_data()
for value in range(3):
    data_unit=copy.copy(data_units)
    if value==1:
        data_unit[value]=1
    elif value==2:
        data_unit[value]=1
        data_unit[value+3]=1
    cost_list=[]
    for value_1 in range(6):
       cost_list.append(data_cost[value])
       value+=3
    total_cost,total_machine=main_operation(data_unit,cost_list,units,hour)
    cost=min(total_cost)
    machine=total_machine[total_cost.index(cost)]
    cost=str(cost)
    final_result.append(cost)
    machine=list(map(str,machine))
    final_result.append(machine)
string_list=[]
index=-1
while(index<=3):
    index+=2
    temporary=[]
    for i in range(len(final_result[index])-1,-1,-1):
        if final_result[index][i]!='0':
            tuple_string='('+type_machines[i]+','+final_result[index][i]+')'
            tuple_string=tuple_string.replace("'","")
            temporary.append(tuple_string)
    string_list.append(temporary)

output={
"Output":[
{
     "region":"New York",
     "total_cost":"$"+final_result[0],
     "machines":
         string_list[0]

     },
     {
     "region":"India",
     "total_cost":"$"+final_result[2],
     "machines":
         string_list[1]
      
     },
     {
     "region":"China",
     "total_cost":"$"+final_result[4],
     "machines":
         string_list[2]
      
     },
    ]
   }

json_result=json.dumps(output,indent=1)
print(json_result)



    



