import sys
import Pretreatment
import Translation


file_name = str(sys.argv[-1])

file = open(file_name,encoding = 'utf-8')
file_text = file.read()

List_Code = Pretreatment.Decomposition_Code(file_text)

Text = Translation.Translation_Code(List_Code)
print(Text)

    

    


