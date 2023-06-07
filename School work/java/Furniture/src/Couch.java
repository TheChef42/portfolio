public class Couch extends Furniture{
    private String type;
    private String material;


    public Couch(double height, double width, String material) {
        this.type = "couch";
        this.material = material;
        setHeight(height);
        setWidth(width);
    }
    @Override
    public String getType() {
        return type;
    }

    public String getMaterial() {
        return material;
    }
    public void setMaterial(String material) {
        this.material = material;
    }
}
