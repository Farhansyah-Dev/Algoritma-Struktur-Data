<?php

$number = readline ('Masukan Bilangan dong: ');

if ($number > 0 ) {
    echo "Bilangan $number : Positif".PHP_EOL;
}
else if ($number < 0 ) {
    echo "Bilangan $number :Negatif".PHP_EOL;
}
else {
    echo "Bilangan $number : Nol".PHP_EOL;
}