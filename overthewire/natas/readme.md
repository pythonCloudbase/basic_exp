# Natas
### Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at http://natasX.natas.labs.overthewire.org, where X is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. natas0 for level 0) and its password.

# Natas 0
password natas0

# Natas 1
password <!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->

The password was in the source code

# Natas 2

password <!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->

In source code without right click

# Natas 3

password 
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14

we saw a file names `files/pixel.png` indicating that the pixel.png is in a folder `files`. After enumerating  `files` it was found that `users.txt` existed. Inside which we found the password.

# Natas 4

natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

in robots.txt
User-agent: *
Disallow: /s3cr3t/

# Natas 5

Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

adding the referer through burpsuite as http://natas5.natas.labs.overthewire.org

# Natas 6

Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1

changing the cookie value to loggedin through burpsuite as 1

# Natas 7

Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9

when looking at source file we found that javascript included one secretes.inc file, which when accessed through browser told us the values of $secret. 

# Natas 8

<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

Changed the url to http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/

DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe

# Natas 9

encodedSecret = "3d3d516343746d4d6d6c315669563362"

function decodeSecret(encodedSecret) {

    var hex = encodedSecret
    var bytes = []
    var str
    
    for (var i=0; i< hex.length-1; i+=2){
        bytes.push(parseInt(hex.substr(i,2),16))
    }

    str = String.fromCharCode.apply(String, bytes)

    str = str.split("").reverse().join("");
    console.log("after reversing")

    return atob(str)    
}

//return bin2hex(strrev(base64_encode($secret)));

"oubWYf2kBq"

Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl

we did it after reverse engineering the number.

# Natas 10 

it was a code execution vulnerability
we input 	
`;cat /etc/natas_webpass/natas10`

nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

# Natas 11

.htaccess:AuthType Basic
.htaccess: AuthName "Authentication required"
.htaccess: AuthUserFile /var/www/natas/natas10//.htpasswd
.htaccess: require valid-user
.htpasswd:natas10:$1$XOXwo/z0$K/6kBzbw4cQ5exEWpW5OV0
.htpasswd:natas10:$1$mRklUuvs$D4FovAtQ6y2mb5vXLAy.P/
.htpasswd:natas10:$1$SpbdWYWN$qM554rKY7WrlXF5P6ErYN/
/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

This time certain characters were filtered so we used
*/ cat /etc/pass/natas to get tall the values for command injection

# Natas 12

Given code :

'''javascript

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
        $mydata['showpassword'] = $tempdata['showpassword'];
        $mydata['bgcolor'] = $tempdata['bgcolor'];
        }
    }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}

$data = loadData($defaultdata);

if(array_key_exists("bgcolor",$_REQUEST)) {
    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
        $data['bgcolor'] = $_REQUEST['bgcolor'];
    }
}

saveData($data);
'''











