package Java;

class Car {
    Integer id;
    String license;
    Account driver;
    Integer passegenger;

    public Car (String lincense, Account driver) {
        this.license = license;
        this.driver = driver;
    }

    void printDataCar() {
        System.out.println("Lincense: " + license + "Driver: " + driver.name + " Passengers: " +  passegenger);
    }
}
