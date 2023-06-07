public abstract class Shape implements Printable{
    private int x = 0;
    private int y = 0;
    public abstract double getArea();
    public abstract double getPerimeter();

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}
