

Code_Base = [] #初始化基本库
Code_Core = [] #初始化核心库
Code_Method = [] #初始化方法库

Library_Version = "G2209081840.0 PEL"

def Join_Code(Code,Replace_Code,Library):
    
    if Library == "Base":
        Code_Base.append([Code,Replace_Code])

    if Library == "Core":
        Code_Core.append([Code,Replace_Code])

    if Library == "Method":
        Code_Method.append([Code,Replace_Code])
#创建基本库

Join_Code("print",["输出","打印"],"Base")
Join_Code("input","输入","Base")
Join_Code("import","导入","Base")

Join_Code("elif","否则如果","Base")
Join_Code("if","如果","Base")
Join_Code("else","否则","Base")

Join_Code("def",["创建函数","声明函数","声明方法","创建方法","创建子程序","函数","子程序"],"Base")
Join_Code("class","创建类","Base")

Join_Code("for","遍历循环","Base")
Join_Code("while","判断循环","Base")
Join_Code("break","退出循环","Base")
Join_Code("continue","跳过本轮循环","Base")
Join_Code("return","返回","Base")

Join_Code("int",["整数","到整数","整型","到整型"],"Base")
Join_Code("str",["字符串","到字符串"],"Base")
Join_Code("float",["浮点","到浮点"],"Base")
Join_Code("bool","布尔","Base")

Join_Code("pass","无操作","Base")
Join_Code("False","假","Base")
Join_Code("None","无","Base")
Join_Code("True","真","Base")
Join_Code("and","与","Base")
Join_Code("del","删除","Base")
Join_Code("global","全局变量","Base")
Join_Code("in","在","Base")
Join_Code("is","是","Base")
Join_Code("lambda","创建匿名函数","Base")
Join_Code("not","非","Base")
Join_Code("or","或","Base")
Join_Code("raise","触发异常","Base")
Join_Code("assert","断言","Base")
Join_Code("die","打印错误信息","Base")
Join_Code("abs","取绝对值","Base")
Join_Code("long",["长整数","到长整数"],"Base")
Join_Code("pow","取幂","Base")
Join_Code("range","创建序列","Base")
Join_Code("round","四舍五入","Base")
Join_Code("sum","集合求和","Base")
Join_Code("oct",["八进制","到八进制"],"Base")
Join_Code("hex",["十六进制","到十六进制"],"Base")
Join_Code("chr","取ASCII","Base")
Join_Code("bin",["二进制","到二进制"],"Base")

Join_Code("random","随机数模块","Base")
Join_Code("randint","取随机数","Base")

Join_Code("tkinter.messagebox.showinfo","信息框","Base")

#创建方法库

Join_Code("replace","替换","Base")
Join_Code("split","分割","Base")

Join_Code("Max","最大","Base")
Join_Code("Min","最小","Base")
Join_Code("Append","添加","Base")

Join_Code("get",["取内容","取数据","读取","获取"],"Base")

#导入外部库
#ReadTranslationLibrary()