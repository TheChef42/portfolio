public class Main {
    public static void main(String[] args) {
        // Instantiate the Couch class
        Couch couch = new Couch(0.5, 3, "leather");

        // Check the type of this furniture
        System.out.println("This is a: " + couch.getType());

        // Check the attribute values
        System.out.println("Height: " + couch.getHeight());
        System.out.println("Width: " + couch.getWidth());
        System.out.println("Material: " + couch.getMaterial());

        // Adjust the height
        couch.setHeight(0.6);
        System.out.println("New height: " + couch.getHeight());
    }
}
