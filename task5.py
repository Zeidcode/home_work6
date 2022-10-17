    # Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв"".
text = '''Some абв text абв text абв text some words'''
text_list = text.split()
to_delete = "абв"  
result = [i for i in text_list if  not virus in i ]
print(result)