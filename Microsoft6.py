class Solution(object):
    def getHint(self, secret, guess):
        x = len(secret)
        BullCount = 0 #counter for Bulls
        CowCount = 0 #counter for Cows

        #convert both strings to arrays for mutability
        SecretArray = list(secret) 
        GuessArray = list(guess)
        
        for i in range(x):
            if SecretArray[i] == GuessArray[i]:
                BullCount +=1
                #mark that element as counted
                SecretArray[i] ='X'
                GuessArray[i] ='X'

        
        for i in range(x):
            if GuessArray[i] != 'X' and GuessArray[i] in SecretArray:
                CowCount +=1
                thatIndex = SecretArray.index(GuessArray[i])
                SecretArray[thatIndex] = 'X'
                GuessArray[i] = 'X'
        return str(BullCount)+"A"+str(CowCount)+"B"