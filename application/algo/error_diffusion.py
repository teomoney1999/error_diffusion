
class ErrorDiffusion: 
    def __init__(self, mtx, f, height, width): 
        self.mtx = mtx
        self.f = f
        self.height = height
        self.width = width
    
    def normalize(self, value): 
        # Control the value on [0:255]
        if value > 255: 
            value = 255
        elif value < 0: 
            value = 0     
        return value
    
    def __err(self, err, divident, divisor): 
        # if divisor == 0: return None
        return err * (divident / divisor)

    def one_way(self): 
        mtx = self.mtx
        for i in range(self.height): 
            for j in range(self.width): 
                current = mtx[i][j]
                new_value = 0

                if current < self.f: 
                    new_value = 0
                elif current > self.f: 
                    new_value = 255
                
                mtx[i][j] = new_value
                
                if j == self.width - 1:
                    break

                error = current - new_value

                new_number = mtx[i][j+1] + error
                new_number = self.normalize(new_number)

                mtx[i][j+1] = new_number
        return mtx
    
    def floyd_steinberg_way(self): 
        mtx = self.mtx

        for i in range(self.height): 
            for j in range(self.width): 
                current = mtx[i][j]
                new_value = 0
                
                if current < self.f: 
                    new_value = 0
                elif current > self.f: 
                    new_value = 255
                
                mtx[i][j] = new_value

                error = current - new_value

                if j < self.width - 1:
                    # new_number = mtx[i][j+1] + ( error * (7/16) )
                    new_number = mtx[i][j+1] + self.__err(error, 7, 16)
                    new_number = self.normalize(new_number)
                    # print("new_number", new_number)
                    mtx[i][j+1] = new_number
                
                if i < self.height - 1: 
                    new_number = mtx[i+1][j] + ( error * (5/16) )
                    # new_number = mtx[i][j+1] + self.__err(error, 5, 16)
                    new_number = self.normalize(new_number)
                    mtx[i+1][j] = new_number

                if (j > 0) and (i < self.height - 1):
                    new_number = mtx[i+1][j-1] + ( error * (3/16) )
                    # new_number = mtx[i][j+1] + self.__err(error, 3, 16)
                    new_number = self.normalize(new_number)
                    mtx[i+1][j-1] = new_number

                if (i < self.height - 1) and (j < self.width - 1): 
                    new_number = mtx[i+1][j+1] + ( error * (1/16) )
                    # new_number = mtx[i][j+1] + self.__err(error, 1, 16)
                    new_number = self.normalize(new_number)
                    mtx[i+1][j+1] = new_number
        return mtx

    
    def from_bell_lab_way(self): 
        mtx = self.mtx
        for i in range(self.height): 
            for j in range(self.width): 
                current = mtx[i][j]
                new_value = 0

                if current < self.f: 
                    new_value = 0
                elif current > self.f: 
                    new_value = 255
                
                mtx[i][j] = new_value

                error = current - new_value  
                
                if j < self.width - 1:
                    new_number = mtx[i][j+1] + ( error * (7/48) )
                    new_number = self.normalize(new_number)
                    mtx[i][j+1] = new_number

                if j < self.width - 2:
                    new_number = mtx[i][j+2] + ( error * (5/48) )
                    new_number = self.normalize(new_number)
                    mtx[i][j+2] = new_number

                if (j > 1) and (i < self.height - 1):
                    new_number = mtx[i+1][j-2] + ( error * (3/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+1][j-2] = new_number

                if (j > 0) and (i < self.height - 1):
                    new_number = mtx[i+1][j-1] + ( error * (5/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+1][j-1] = new_number

                if i < self.height - 1: 
                    new_number = mtx[i+1][j] + ( error * (7/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+1][j] = new_number

                if (j < self.width - 1) and (i < self.height - 1):
                    new_number = mtx[i+1][j+1] + ( error * (5/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+1][j+1] = new_number   

                if (j < self.width - 2) and (i < self.height - 1):
                    new_number = mtx[i+1][j+2] + ( error * (3/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+1][j+2] = new_number

                if (j > 1) and (i < self.height - 2):
                    new_number = mtx[i+2][j-2] + ( error * (1/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+2][j-2] = new_number

                if (j > 0) and (i < self.height - 2):
                    new_number = mtx[i+2][j-1] + ( error * (3/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+2][j-1] = new_number

                if i < self.height - 2:
                    new_number = mtx[i+2][j] + ( error * (5/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+2][j] = new_number

                if (j < self.width - 1) and (i < self.height - 2):
                    new_number = mtx[i+2][j+1] + ( error * (3/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+2][j+1] = new_number

                if (j < self.width - 2) and (i < self.height - 2):
                    new_number = mtx[i+2][j+2] + ( error * (1/48) )
                    new_number = self.normalize(new_number)
                    mtx[i+2][j+2] = new_number
        return mtx
