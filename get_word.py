with open("html_text.txt", 'r') as file:
    text = file.read()

beginning = 0
text.find('成都天气预报12月', beginning) != -1;


word_start_point = text.find('成都天气预报12月', beginning)
word_end_point = text.find('星期', word_start_point + 7)

word = text[word_start_point: word_end_point]

beginning2 =0



text.find('小于', beginning2) != -1;

start_definition = text.find('成都天气预报12月', beginning2)+11 

end_definition = text.find('小于3级')

word_definition = text[start_definition + 1 : end_definition]

word_dict= "Today is" +  word  + "."  + "And todays weather is"  +  word_definition  + "."


print(word_dict)
