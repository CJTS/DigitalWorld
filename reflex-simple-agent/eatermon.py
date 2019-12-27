from random import randrange

class Eatermon:
    x = 0
    y = 0
    def walkup(this):
        this.y -= 1
    def walkdown(this):
        this.y += 1
    def walkleft(this):
        this.x -= 1
    def walkright(this):
        this.x += 1
    def eat(this, grid):
        grid[this.x][this.y] = 0
    def see(this, square):
        return square == 1
    def live(this, grid):
        if(this.see(grid[this.x][this.y])):
            this.eat(grid)
            return False
        else:
            action = randrange(4)
            if(action == 0 and this.y > 0):
                this.walkup()
            elif(action == 1 and this.y < 9):
                this.walkdown()
            elif(action == 2 and this.x > 0):
                this.walkleft()
            elif(action == 3 and this.x < 9):
                this.walkright()

            return True