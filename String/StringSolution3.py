class StringSolution3:
    def dynamicPassword(self, password: str, target: int) -> str:
        #return password[target:] + password[:target]
        res = []
        for j in range(target,len(password),1):
            res.append(password[j]) 
        for i in range(target):
            res.append(password[i])
        return ''.join(res)