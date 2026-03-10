class StringSolution1:
    def pathEncryption(self, path: str) -> str:
        #return path.replace('.', ' ')
        res = []
        for item in path:
            if item == '.':
                res.append(' ')
            else :
                res.append(item)
        return ''.join(res)