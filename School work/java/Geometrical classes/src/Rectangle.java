public class Rectangle extends Shape{
    private double a;
    private double b;

    public Rectangle(double a, double b) {
        this.a = a;
        this.b = b;
    }
    public Rectangle(double a, double b, int x, int y) {
        this.a = a;
        this.b = b;
        this.setX(x);
        this.setY(y);
    }

    @Override
    public double getArea() {
        return a*b;
    }

    @Override
    public double getPerimeter() {
        return 2*a+2*b;
    }

    @Override
    public void print() {
        System.out.println("This is a rectangle with the coordinates x:" + getX() + " y:" + getY());
    }

    public double getA() {
        return a;
    }

    public void setA(double a) {
        this.a = a;
    }

    public double getB() {
        return b;
    }

    public void setB(double b) {
        this.b = b;
    }
}
