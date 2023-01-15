package Java;

class Car {
    Integer id;
    String license;
    Account driver;
    private Integer passegenger;

    public Car (String lincense, Account driver) {
        this.license = license;
        this.driver = driver;
        passegenger = 4; 
        System.out.print("passenger: " + passegenger);
    }

    void printDataCar() {
        System.out.println("Lincense: " + license + "Driver: " + driver.name + " Passengers: " +  passegenger);
    }
}
