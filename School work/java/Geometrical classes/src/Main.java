public class Main {
    public static void main(String[] args) {
        // Instance some concrete classes (subclasses of Shape)
        /* We can actually create an array of type the superclass,
         * because all of it subclasses are inherently of type Shape as well */
        Shape[] shapes = {new Circle(1.0), new Square(2.0), new Rectangle(1.0, 2.0),
                new Circle(1, 2, 3), new Square(3, -1, 5), new Rectangle(0, 7, 2, 4)};

        // Check all shapes
        for(Shape shape : shapes) {
            shape.print();
            System.out.println("- Area: " + shape.getArea());
            System.out.println("- Perimeter: " + shape.getPerimeter());
        }
    }
}