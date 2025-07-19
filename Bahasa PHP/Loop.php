<?php

function BelajarLooping (int $numberLoop) {
    for ( $i = 1; $i <= $numberLoop; $i++ ) {
        echo "Looping PHP.", $i.PHP_EOL;
    }
    if ($numberLoop %2 == 0) {
        echo "$numberLoop Genap".PHP_EOL;
    }
    else {
        echo "Ganjil".PHP_EOL;
    }
}
$user = readline("Masukan angka Loop: ");
BelajarLooping($user);

function PerulanganWhile (int $number) {
    $start = 1;
    while ($start <= $number) {
        echo "This is While Loop...".PHP_EOL;
        $start++;
    }
}
PerulanganWhile(4);




