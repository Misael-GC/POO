<?php
require_once('car.php');
class UberBlack extends Car {
    public $typeCarAccepted;
    public $seatMaterial;

    public function __construct($license, $driver, $typeCarAccepted, $seatsMaterial){
        parent::__construct($license, $driver);
        $this->typeCarAcceoted = $typeCarAccepted;
        $this->seatsMaterial = $seatsMaterial;
    }
}
?>