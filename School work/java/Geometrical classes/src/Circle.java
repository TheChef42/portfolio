public class Circle extends Shape {
    private double radius;


    public Circle(double radius) {
        this.radius = radius;
    }
    public Circle(double radius, int x, int y) {
        this.radius = radius;
        this.setX(x);
        this.setY(y);
    }

    @Override
    public double getArea() {
        return 3.14*radius*radius;
    }

    @Override
    public double getPerimeter() {
        return 2*3.14*radius;
    }
    @Override
    public void print() {
        System.out.println("This is a circle with centre at (" + getX() + "," + getY() + ") and radius of " + radius);
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }
}
