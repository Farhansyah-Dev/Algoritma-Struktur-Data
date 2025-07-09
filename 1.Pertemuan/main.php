<?php

echo "Masukan Bilangan :".PHP_EOL;
$number = trim(fgets(STDIN));

if ($number > 0 ) {
    echo "Bilangan $number : Positif".PHP_EOL;
}
else if ($number < 0 ) {
    echo "Bilangan $number :Negatif".PHP_EOL;
}
else {
    echo "Bilangan $number : Nol".PHP_EOL;
}