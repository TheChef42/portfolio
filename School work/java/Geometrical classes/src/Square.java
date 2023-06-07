public class Square extends Shape{
    private double side;

    public Square (double side){
        this.side = side;
    }
    public Square (double side, int x, int y){
        this.side = side;
        this.setX(x);
        this.setY(y);
    }
    @Override
    public double getArea() {
        return side*side;
    }

    @Override
    public double getPerimeter() {
        return side*4;
    }

    @Override
    public void print() {
        System.out.println("This is a square with the coordinates x:" + getX() + " y:" + getY());
    }

    public double getSide() {
        return side;
    }

    public void setSide(double side) {
        this.side = side;
    }
}

