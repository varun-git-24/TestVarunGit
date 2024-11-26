my_string = """    My Name is Varun 
so i am Varun 
so i am called as varun
so i am knows as varun """

import re
# test1 = '1HI 1997 VA90RUN 98 , my email id varunrotti11@gmail.com and second one is hi@gmail.uk.com'
# text = "Please contact us at9support@example.com or0sales@example.co.uk for further information. You can also reach out to admin@my-domain.org."
# test2 = 'nOsha VarunD'
# temp = "''3.335''"
#
# p = r'[A-Z]'
# x = re.search(p,test2)
# print(x.group())

# pattern = r'Split+'
# string = 'Split this string by spaces.'
#
# result = re.split(pattern, string)
# print("Split result:", result)

pattern_to_get_digits = r'\d+' # ---['1997', '90', '98', '11']
pattern_to_get_digits1 = r'\d*'  # ----- ['', '', '', '1997', '', '', '', '90', '', '', '', '', '98', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '11', '', '', '', '', '', '', '', '', '', '', '']
pattern_to_get_digits2 = r'\d?'    # ----   ['', '', '', '1', '9', '9', '7', '', '', '', '9', '0', '', '', '', '', '9', '8', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', '1', '', '', '', '', '', '', '', '', '', '', '']
pattern_to_get_digits3 = r'\d$' #--- ['0']
pattern_to_get_digits4 = r'^\d' #--- ['1']
#pattern_to_get_emails = r'[a-zA-Z0-9._%]*@[a-zA-Z0-9.-]*\.[a-zA-z]{2,1}'
#pattern_to_get_emails = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
pattern_to_get_non_digits = r'\D*'
#result = re.findall(pattern_to_get_emails, test1)
#print(result)


x = 'hello i am varun , am am am'
p = r'he'
x = re.match(p,x)
print(x.group())


#print(temp.strip("'"))
# print(test2[::])
# print(test2[3::])
# print(test2[1:6])
# print(test2[:6])
# print(test2[2:])
# print(test2[3:1:])
# print(test2[3:8:2]) #saV
test2 = 'nOsha VarunD'
print(test2[8:3:-1]) #a h
# print(test2[::-2]) #nrVasn

#x = 'a'
#print(my_string.count(x))
#print(my_string.count('x'))
#print("This is formated string --> {} ---- of my_string".format(my_string))
#print(my_string.lower())
#print(my_string.upper())
# print(my_string.strip())
# print(my_string.split())'
# print(my_string.splitlines())
# print(test1.isupper())
# print(my_string.islower())
# print(test1.isalnum())
# print(test1.startswith('V'))
# print(test1.find('98',8))
# print(test1.count('9',10))
# print('x'.join(test2))
#print(test2.capitalize())
#print(test1.replace(test1, test2.capitalize()))
#print(test2.rfind('g'))
#print(test2.find('g'))



# x  = ['Hi', 'hello', 'hey']
# print(''.join(x))
#
#
# y = 'Hello , how are you'
# print('x'.join(y))








import re
# sfp = """.{"hostname": "rs10002100a-fv224300035", "metric_name": "sfp", "interface": "p3cpk", "link_detected": true, "module_type": "SFF_8472", "transeiver_type": "10G Ethernet: 10GBASE-SR", "digital_diagnostic_monitoring_supported": true, "temperature_high_alarm_threshold_c": 75.0, "temperature_low_alarm_threshold_c": -5.0, "temperature_high_warning_threshold_c": 70.0, "temperature_low_warning_threshold_c": 0.0, "voltage_high_alarm_threshold_v": 3.5, "voltage_low_alarm_threshold_v": 3.08, "voltage_high_warning_threshold_v": 3.48, "voltage_low_warning_threshold_v": 3.1, "bias_current_high_alarm_threshold_ma": 18.0, "bias_current_low_alarm_threshold_ma": 1.0, "bias_current_high_warning_threshold_ma": 15.0, "bias_current_low_warning_threshold_ma": 2.0, "output_power_high_alarm_threshold_mw": 1.2589, "output_power_low_alarm_threshold_mw": 0.1585, "output_power_high_warning_threshold_mw": 1.0, "output_power_low_warning_threshold_mw": 0.2512, "receiver_signal_power_high_alarm_threshold_mw": 1.0, "receiver_signal_power_low_alarm_threshold_mw": 0.0631, "receiver_signal_power_high_warning_threshold_mw": 0.7943, "receiver_signal_power_low_warning_threshold_mw": 0.0794, "temperature_c": 50.5391, "voltage_v": 3.3418, "bias_current_ma": 5.366, "output_power_mw": 0.5552, "receiver_signal_power_mw": 0.5846, "enhanced_options_supported": true, "RX_LOS": false, "TX_FAULT": false, "sfp_detected": true, "error": ""}
# Received signal 2
# Stopping application
# [root@rs10002100a-fv224300035 sfp]#
# """
#
# lines = sfp.split('\n')
# for line in lines:
#     if not line.startswith('Received signal 2') and not line.startswith('Stopping application') and not line.startswith('[root@'):
#         print(line)



# Sample string
# text1 = "Hello, World!"
#
# # Convert string to ASCII values using list comprehension
# ascii_values = [ord(char) for char in text1]
# ascii_char = [ele+2 for ele in ascii_values]
# final = [chr(item) for item in ascii_char]
# print(final)
#
# final1 = ''.join(final)
# #final = final.replace('"' , " ")
#
#
# print(final1)


# status = False
# i = 3
# while status:
#     print(status , 'is the status')
#     print('HI')
#     i = i - 1
#     if i == 1:
#         break



# a = 10
# b = 11
# print(id(a))
# print(id(b))

print(3/7)
print(7//3)






