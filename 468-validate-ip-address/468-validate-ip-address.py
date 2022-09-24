class Solution:
    
    def validateIPv4(self, IP):
        nums =  IP.split('.')
        for x in nums:
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
            
        return "IPv4"
    
    
    def validateIPv6(self, IP):
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            if len(x) == 0 or len(x) > 4:
                return "Neither"        
    
            for i in x:
                if i not in hexdigits:
                    return "Neither"
                
        return "IPv6"
    
    
    
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            return self.validateIPv4(queryIP)
        elif queryIP.count(':') == 7:
            return self.validateIPv6(queryIP)
        else:
            return "Neither"
        