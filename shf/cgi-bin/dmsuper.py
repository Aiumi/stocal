import abc

class DMSuper:
    
    def __init__(self):
        
        self.totals = [0, 0]
        self.companyMap = dict()
    
    @abc.abstractmethod
    def getWeight(self) -> int:
        
        pass
    
    @abc.abstractmethod
    def read(self):
        
        pass
    
    def getAccumulators(self) -> []:
        
        return self.totals
    
    @abc.abstractmethod    
    def getName(clss, param:str) -> str:
        
        pass
        
    
    
