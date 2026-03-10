class StringSolution2:
    def reverseMessage(self, message: str) -> str:
        strs = message.split()
        strs.reverse()
        return ' '.join(strs)
        """
        words = []
        tmp = []
        for item in message:
            if item!=' ':
                tmp.append(item)
            else:
                if tmp:
                    words.append(''.join(tmp))
                    tmp=[]
        if tmp:
            words.append(''.join(tmp))
        words.reverse()
        return ' '.join(words)
        """