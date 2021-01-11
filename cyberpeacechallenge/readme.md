# Global CyberPeace CTF

##  Client side is the best side 

In this challenge, we looked at the source code and found that the flag was encrypted by a javascript algorithm, given below

```javascript
$(document).ready(function() {
    $("#check").click(function() {
        var dict = new Array();
        var dict = new Array();
        dict[0] = {"1":"4","4":"87","9":"c","t":"0f","z":"1","E":"5b","z":"03","M":"eb","Z":"3"};
        dict[1] = {"3":"45","5":"37","6":"a","c":"a9","h":"1","s":"00","E":"b","K":"c1","L":"3"};
        dict[2] = {"1":"1","3":"f8","c":"3","f":"6","B":"e0","I":"cc","S":"20","T":"94"};
        var pass = $('#password').val();
        var password = "";
        for (var i = 0; i < pass.length; i++) {
            password += dict[i%3][pass.charAt(i)];
        }
        $("#ok").show();
        if ("3a33364bf88700e00fa994eb45205b37" == password){ 
         //Z6cZLf1E34sBtcTM3SE5
           $("#ok").text("Very niice! This is your flag: HL{"+pass+"}");
        }else{
           $("#ok").text("Nope :(");
        }
        return false;
    });
});

var dict = new Array();
var dict = new Array();
dict[0] = {"1":"4","4":"87","9":"c","t":"0f","z":"1","E":"5b","z":"03","M":"eb","Z":"3"};
dict[1] = {"3":"45","5":"37","6":"a","c":"a9","h":"1","s":"00","E":"b","K":"c1","L":"3"};
dict[2] = {"1":"1","3":"f8","c":"3","f":"6","B":"e0","I":"cc","S":"20","T":"94"};

var keyCollection = []

for(var j =0; j <=3; ++j){
    for( var i of dict[j].keys()){
        keyCollection.push(dict[j])
    }    
}

console.log(keyCollection)

var pass1 = "3a33364bf88700e00fa994eb45205b37"

for (var i = 0; i < pass1.length; i++) {
    password += dict[i%3][pass1[]];
}
```

The objective was to reverse this algorithm such that we get the dict value back. 

##  Twizzle

A twitter handle had shared a series of photos, the aim of which was to download the pictures, resulting in a qr code then scanning the qr code to reach a site. The pictures were extracted through twint and then the picture were collaged using motnage in kali.

##  San Pedro newspapaer

`Historians found out that the very old issue of the "San Perdo Newspaper" contains a legendary crossword. The whole issue from 20th of April 1942 is protected by a paywall. Can you crack the paywall and solve the crossword`

In this challenge we were given a website hosting a newspaper with a crossword puzzle in one of the pages, however only the 1st page of the newpaper was visible to the user. The initial challenge was getting to the crossword page. In order to get to crossword page we studied how the url was being made and then we found that an extra parameter h was added to the url which took the has of the premade url using the function `createHash()`, In the `/getNewspaperDescription` we found that the id of pages. So using this information we found that the page number 9 contained the crossword puzzle.

On the crossword page the crossword was needed to be solved using regex union between the rows and columns. After much trial and error, the result that was found needed to be added to `/content?=` to get the flag finally.

##  Client side is the best side 2

In this challenge a webpage was provided with following code :

``` javascript
$(document).ready(function() {
        $("#check").click(function() {
            var pass = $('#password').val();
            console.log(SHA420(pass));
			$("#ok").show();
            if (pass.length==30 && "b0218147908009cec91e52147db8334162e332e060ba25f6db450a177d8c4c078e9e46a6ecd54f0c62ff9e19b6856a1821e2ff6712442b55a2a29697675697a2" == SHA420(pass)){
			   $("#ok").text("Very niice! This is your flag: "+pass);
            }else{
			   $("#ok").text("Nope :(");
			}
            return false;
        });
});

```

in order to reverse engineer this code a function `sha420()` was given to us. The aim being to reerse the hash and get the plaintext back. We were in luck because unlike other hashing function this was just and encryption therefore it was reversible. 

Baaki jose sir batayenge. I don't want to steal his thunder.

##  TLS Dance

The hint in this was to dance to the tune of CHACHACHA 

We were given an ip to connect to, connecting to it through telnet we found it was an https site so we used openssl instead. And because of the hint the cipher was chacha cipher.
so we connected using `openssl s_client -connect 152.96.7.8:443 -cipher ECDHE-RSA-CHACHA20-POLY1305` and got the flag

##  Lucky Luke 

In this challenge we were provided a minidump file. Our aim was to string together four different character  enigmatically from 'highest to lowest, whatever that might mean' When parsed through mimikatz we found that the minidump contained ntlkm hashes and username. After extracting the ntlm hashes they were cracked through john the ripper tool. The flag order was decided based on a cartoon `Lucky Luke` in which the character hieght decided the position of the flag.

##  Volatility Analysis vol 1

A memory dump was provided for anlysis , with aim of finding the encryption string of malware. The dump provided was anlaysed using volatility to find the id of the malicious process, which was identified as a command prompt was spawning an svchost processs. When the process history was logged through console command the encryption id of malicious process was found.

##  pcap analysis 1

The aim of this challenge was to find out a series of pssword from a pcap file. The password and username was given in pcap file itself. Only requirement was to follow the correct TCP stream.

##  clowns cipher

In this the N, E , q values were given and aim was to crack the RSA1 cipher. This was done using a tool called RSACTF tool, and the falg was pretty striaghtforward.

