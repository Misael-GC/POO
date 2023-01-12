package Java;

class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo");
        UberX uberX = new UberX("AMD123", new Account("Don Gato", "ROSS123"), "Chevrolet", "Sonic");
        uberX.passegenger = 4;
        uberX.printDataCar();

        // Car car2 = new Car("ROSS789", new Account("Rosario Hernandez", "RHC731"));
        // car2.passegenger = 3;
        // car2.printDataCar();
    }
}
