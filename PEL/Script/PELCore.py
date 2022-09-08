import json,socketserver,os,time,threading

buildScriptBase = ""

# 若超过7s没有收到Link心跳包说明已经和IDE断开连接，则结束Core
lastCheck = time.time()
def CheckLink():
    global lastCheck
    while True:
        time.sleep(1)
        if time.time() - lastCheck >= 7:
            os._exit(0)

# SocketServer监听PyELang IDE的请求
class Server(socketserver.BaseRequestHandler):
    
    def handle(self):
        global lastCheck
        global buildScriptBase

        conn = self.request
        
        threading.Thread(target=CheckLink).start()

        while True:
            data = conn.recv(1024).decode()

            if data == "__Exit":
                os._exit(0)

            if "__RunProgram" in data: # 收到测试指令，开始分析代码

                mainWindowJsonPath = data.split("__")[0] # 获取窗口构建Json文件路径
                mainWindowTriggerScriptPath = data.split("__")[1]
                buildScriptPath = data.split("__")[2] # 获取生成代码目录的路径

                triggerScript = "" # 触发代码
                windowScript = "" # 生成窗口的代码
                unitScript = "" # 生成其他组件的代码

                buildScript = buildScriptBase # 生成窗口的基本代码
                windowName = "" # 生成的Window Object

                with open(mainWindowJsonPath,"r",encoding="utf-8") as f: # 读取json文件
                    buildJson = json.load(f) # 解析json文件

                    for i in buildJson: # 解析Json获取各组件信息，i在循环中为各组件信息的Key
                        creatScript = "\n".join(buildJson[i]["CreatScript"]) # 解析组件的生成代码

                        for j in buildJson[i]["ShowAttributeList"]: # 对组件的生成代码需要插入属性值的地方进行替换，j在循环中为各属性值的Key
                            creatScript = creatScript.replace(f"{{{{{j}}}}}", buildJson[i][j])
                        
                        # 根据Unit Type储存到各临时变量中
                        if buildJson[i]["Type"] == "Window":
                            windowScript = creatScript
                            buildScript = buildScript.replace("{{Window}}", buildJson[i]["名称"])
                            windowName = buildJson[i]["名称"]
                        else:
                            unitScript += (f"\n{creatScript}").replace('{{DoubleClick}}', buildJson[i]['DoubleClick'])
                    
                    unitScript = unitScript.replace("{{Window}}", windowName)

                    # 将生成的创建代码替换到buildScript中
                    buildScript = buildScript.replace("{{WindowScriptPos}}", windowScript)
                    buildScript = buildScript.replace("{{UnitScriptPos}}", unitScript)


                    # 读取事件响应代码并替换
                    with open(mainWindowTriggerScriptPath,"r",encoding="utf-8") as sf:
                        eventScript = sf.read()

                    buildScript = buildScript.replace("{{TriggerScriptPos}}", eventScript)

                    # 生成最终代码文件
                    with open(f'{buildScriptPath}build.py',"w",encoding="utf-8") as bs:
                        bs.write(buildScript)

                    conn.sendall(f'{buildScriptPath}build.py__building'.encode())
                    
            
            if "__LinkCheck" in data:
                lastCheck = time.time()
                conn.sendall("__Linking".encode())
                
                


if __name__ == "__main__":
    
    # 读取构建程序的基本代码
    with open(os.path.dirname(__file__) + "/Base.py","r") as f:
        buildScriptBase = f.read()

    # 启动Socket服务器
    server = socketserver.ThreadingTCPServer(("127.0.0.1",28888),Server)
    server.serve_forever()