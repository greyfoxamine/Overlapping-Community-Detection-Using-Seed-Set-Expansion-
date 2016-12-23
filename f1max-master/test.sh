s1="$(./f1max $1 $2)"
s2="$(./f1max $2 $1)"
s3=$(bc <<<"scale=6; ($s1+$s2)/2") 
s4=$(bc <<<"scale=6; 2*$s1*$s2/($s1+$s2)") 
echo $s1, $s2, $s3, $s4
