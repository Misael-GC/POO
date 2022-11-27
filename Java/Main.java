package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        Car car = new Car("AMD123", new Account("Rousse Ross", "ROSS123"));
        car.passegenger = 4;
        car.printDataCar();

        Car car2 = new Car("ROSS789", new Account("Rosario Hernandez", "RHC731"));
        car2.passegenger = 3;
        car2.printDataCar();
    }
}
