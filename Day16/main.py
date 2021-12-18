hex_to_bin = {
'0':'0000',
'1':'0001',
'2':'0010',
'3':'0011',
'4':'0100',
'5':'0101',
'6':'0110',
'7':'0111',
'8':'1000',
'9':'1001',
'A':'1010',
'B':'1011',
'C':'1100',
'D':'1101',
'E':'1110',
'F':'1111'
}

class Packet():
    def __init__(self, binary):
                
        self.lenght = 6
        self.version = self.to_decimal(binary[0:3])
        self.type_id = self.to_decimal(binary[3:6])

        self.sub_packects = []
        
        if self.type_id == 4:
            self.payload = self.get_literal(binary[6:])
        else:
            self.payload = self.get_operator(binary[6:])
            
    def get_literal(self,binary):
        number = ''
        i = 0
        while(True):
            self.lenght += 5
            number = number + binary[i+1:i+5]
            if binary[i] == '0':
                break
            i += 5
        return self.to_decimal(number)
    
    def get_operator(self,binary):
        
        self.length_type_id = binary[0]
        self.lenght += 1
        
        if self.length_type_id == '0':
            i = 16
            L = self.to_decimal(binary[1:i])
            self.lenght += 15
            read = 0
            while read < L:
                P = Packet(binary[i:]) 
                read += P.lenght
                i += P.lenght
                self.lenght += P.lenght
                self.sub_packects.append(P)
                
        elif self.length_type_id == '1':
            i = 12
            I = self.to_decimal(binary[1:i])
            self.lenght += 11
            for sub in range(I):
                P = Packet(binary[i:]) 
                i += P.lenght
                self.lenght += P.lenght
                self.sub_packects.append(P)
        
        return self.compute_result()
        
     
    def compute_result(self):
        
        if self.type_id == 0:
            result = 0
            for sub_packet in self.sub_packects: result += sub_packet.payload
        
        elif self.type_id == 1:
            result = 1
            for sub_packet in self.sub_packects: result *= sub_packet.payload
        
        elif self.type_id == 2:
            result = float('inf')
            for sub_packet in self.sub_packects: 
                if sub_packet.payload < result: 
                    result = sub_packet.payload
        
        elif self.type_id == 3:
            result = -float('inf')
            for sub_packet in self.sub_packects: 
                if sub_packet.payload > result: 
                    result = sub_packet.payload
        
        elif self.type_id == 5:
            if self.sub_packects[0].payload > self.sub_packects[1].payload:
                result =  1
            else:
                result = 0
            
        elif self.type_id == 6:
            if self.sub_packects[0].payload < self.sub_packects[1].payload:
                result =  1
            else:
                result =  0
            
        elif self.type_id == 7:
            if self.sub_packects[0].payload == self.sub_packects[1].payload:
                result =  1
            else:
                result =  0
            
        return result
    
    def to_decimal(self,b):
        return int(format(int(b, 2), "d"))
    
    def get_sum_versions(self,count):
        count += self.version
        for sub_packet in self.sub_packects:
            count += sub_packet.get_sum_versions(0)
        return count
    
    def get_payload(self):
        return self.payload
    
        
input = '00537390040124EB240B3EDD36B68014D4C9ECCCE7BDA54E62522A300525813003560004223BC3F834200CC108710E98031C94C8B4BFFF42398309DDD30EEE00BCE63F03499D665AE57B698F9802F800824DB0CE1CC23100323610069D8010ECD4A5CE5B326098419C319AA2FCC44C0004B79DADB1EB48CE5EB7B2F4A42D9DF0AA74E66468C0139341F005A7BBEA5CA65F3976200D4BC01091A7E155991A7E155B9B4830056C01593829CC1FCD16C5C2011A340129496A7EFB3CA4B53F7D92675A947AB8A016CD631BE15CD5A17CB3CEF236DBAC93C4F4A735385E401804AA86802D291ED19A523DA310006832F07C97F57BC4C9BBD0764EE88800A54D5FB3E60267B8ED1C26AB4AAC0009D8400854138450C4C018855056109803D11E224112004DE4DB616C493005E461BBDC8A80350000432204248EA200F4148FD06C804EE1006618419896200FC1884F0A00010A8B315A129009256009CFE61DBE48A7F30EDF24F31FCE677A9FB018F6005E500163E600508012404A72801A4040688010A00418012002D51009FAA0051801CC01959801AC00F520027A20074EC1CE6400802A9A004A67C3E5EA0D3D5FAD3801118E75C0C00A97663004F0017B9BD8CCA4E2A7030C0179C6799555005E5CEA55BC8025F8352A4B2EC92ADF244128C44014649F52BC01793499EA4CBD402697BEBD18D713D35C9344E92CB67D7DFF05A60086001610E21A4DD67EED60A8402415802400087C108DB068001088670CA0DCC2E10056B282D6009CFC719DB0CD3980026F3EEF07A29900957801AB8803310A0943200042E3646789F37E33700BE7C527EECD13266505C95A50F0C017B004272DCE573FBB9CE5B9CAE7F77097EC830401382B105C0189C1D92E9CCE7F758B91802560084D06CC7DD679BC8048AF00400010884F18209080310FE0D47C94AA00'
binary = ''.join([hex_to_bin[h] for h in input])
p = Packet(binary)
print('Result Part A:', p.get_sum_versions(0))
print('Result Part B:', p.get_payload())