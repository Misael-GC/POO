<?php

require_once('Car.php');
require_once('Account.php');

$car = new Car("ART456", new Account("Andres Herrera", "AMC980"));
$car->printDataCar();