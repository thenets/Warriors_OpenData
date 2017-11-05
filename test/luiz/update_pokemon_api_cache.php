<?php

for ($i=1; $i<803; $i++) {
    $url = 'https://apps.thenets.org/api/pokemon/v2/pokemon/'.$i;
    echo $url."\n";
    file_get_contents($url);
}