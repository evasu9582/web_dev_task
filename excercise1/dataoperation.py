class datagenerator:
    sapid=None
    Hostname=None
    Macaddress=None
    loopbackipv4=None

    def __init__(self,sapid,Hostname,Macaddress,loopbackipv4):
        self.sapid=sapid
        self.Hostname=Hostname
        self.Macaddress=Macaddress
        self.loopbackipv4=loopbackipv4
        self.lst=[]
    
    def create(self,format,n):
        if format=='XML':
            router=[f"""
            <router>
            <sapid> {self.sapid} </sapid>
            <Hostname> {self.Hostname} </Hostname>
            <Macaddress> {self.Macaddress} </Macaddress>
            <loopbackipv4> {self.loopbackipv4} </loopbackipv4>
            </router>"""]

            self.lst.append(router)

        elif format=='JSON':
            routers={}
            routers['sapid']=self.sapid
            routers['Hosatname']=self.Hostname
            routers['Macaddress']=self.Macaddress
            routers['Loopbackipv4']=self.loopbackipv4

            self.lst.append(routers)
        
        
        return self.lst*n

        


s=datagenerator('12345','www.google.com','12e3-123e-45re-56t4','1.2.3.5')
print(s.create('JSON',3))
# print(s.create('XML',3))

# print(s.update('XML',1))

print(s.delete1('JSON',0))
