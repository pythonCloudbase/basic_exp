First challenge 
HL{Z6cZLf1E34sBtcTM3SE5}

Twizzle - 

350, 337, 335, 330, 329, 324, 320, 319, 318, 317, 316, 314,313, 
interesting things - twizzle means circular does it mean a number series
is this guy following ssomenone a cyclist which is again circular
https://edublognss.wordpress.com/2013/04/16/famous-mathematical-sequences-and-series/
why 359 tweets if the numer is 361

No flag in tweets

Steghide- 
1) ./configure 
2) make
3) make check
4) make install (as root)

libmhash is missing

San Pedro Newspaper
Historians found out that the very old issue of the "San Perdo Newspaper" contains a legendary crossword. The whole issue from 20th of April 1942 is protected by a paywall. Can you crack the paywall and solve the crossword?

client side is the best side 2
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

Substitution cipher

TLS dance
	152.96.7.8
    	tcp
        	7ad1fc0b-f28f-4fa4-af60-5c85c4c5c910.rdocker.vuln.land
            	443


Hint TLS dance : Cha cha cha

ChaCha stream cipher
https://tools.ietf.org/id/draft-mavrogiannopoulos-chacha-tls-01.html
https://superuser.com/questions/924261/manipulation-of-https-method-in-telnet

using Openssl for https website
https://www.bearfruit.org/thoughts/telnet-for-testing-ssl-https-websites/

https://docs.pingidentity.com/bundle/solution-guides/page/iqs1569423823079.html

openssl s_client -connect 152.96.7.8:443 -cipher ChaCha20-Poly1305

TLS_CHACHA20_POLY1305_SHA256:

ECDHE-ECDSA-CHACHA20-POLY1305:
ECDHE-RSA-CHACHA20-POLY1305:
DHE-RSA-CHACHA20-POLY1305:

RSA-PSK-CHACHA20-POLY1305:
DHE-PSK-CHACHA20-POLY1305:
ECDHE-PSK-CHACHA20-POLY1305:
PSK-CHACHA20-POLY1305:

TLS_CHACHA20_POLY1305_SHA256 - TLS_CHACHA20_POLY1305_SHA256 TLSv1.3 Kx=any      Au=any  Enc=CHACHA20/POLY1305(256) Mac=AEAD

S_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 - ECDHE-ECDSA-CHACHA20-POLY1305 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=CHACHA20/POLY1305(256) Mac=AEAD
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 - ECDHE-RSA-CHACHA20-POLY1305 TLSv1.2 Kx=ECDH     Au=RSA  Enc=CHACHA20/POLY1305(256) Mac=AEAD
TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256 - DHE-RSA-CHACHA20-POLY1305 TLSv1.2 Kx=DH       Au=RSA  Enc=CHACHA20/POLY1305(256) Mac=AEAD

TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256 - RSA-PSK-CHACHA20-POLY1305 TLSv1.2 Kx=RSAPSK   Au=RSA  Enc=CHACHA20/POLY1305(256) Mac=AEAD
TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256 - DHE-PSK-CHACHA20-POLY1305 TLSv1.2 Kx=DHEPSK   Au=PSK  Enc=CHACHA20/POLY1305(256) Mac=AEAD
TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256 - ECDHE-PSK-CHACHA20-POLY1305 TLSv1.2 Kx=ECDHEPSK Au=PSK  Enc=CHACHA20/POLY1305(256) Mac=AEAD

TLS_PSK_WITH_CHACHA20_POLY1305_SHA256 - PSK-CHACHA20-POLY1305   TLSv1.2 Kx=PSK      Au=PSK  Enc=CHACHA20/POLY1305(256) Mac=AEAD


TLS_AES_256_GCM_SHA384  TLSv1.3 Kx=any      Au=any  Enc=AESGCM(256) Mac=AEAD
TLS_CHACHA20_POLY1305_SHA256 TLSv1.3 Kx=any      Au=any  Enc=CHACHA20/POLY1305(256) Mac=AEAD
TLS_AES_128_GCM_SHA256  TLSv1.3 Kx=any      Au=any  Enc=AESGCM(128) Mac=AEAD
ECDHE-ECDSA-AES256-GCM-SHA384 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=AESGCM(256) Mac=AEAD
ECDHE-RSA-AES256-GCM-SHA384 TLSv1.2 Kx=ECDH     Au=RSA  Enc=AESGCM(256) Mac=AEAD
DHE-RSA-AES256-GCM-SHA384 TLSv1.2 Kx=DH       Au=RSA  Enc=AESGCM(256) Mac=AEAD
ECDHE-ECDSA-CHACHA20-POLY1305 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=CHACHA20/POLY1305(256) Mac=AEAD
ECDHE-RSA-CHACHA20-POLY1305 TLSv1.2 Kx=ECDH     Au=RSA  Enc=CHACHA20/POLY1305(256) Mac=AEAD
DHE-RSA-CHACHA20-POLY1305 TLSv1.2 Kx=DH       Au=RSA  Enc=CHACHA20/POLY1305(256) Mac=AEAD
ECDHE-ECDSA-AES128-GCM-SHA256 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=AESGCM(128) Mac=AEAD
ECDHE-RSA-AES128-GCM-SHA256 TLSv1.2 Kx=ECDH     Au=RSA  Enc=AESGCM(128) Mac=AEAD
DHE-RSA-AES128-GCM-SHA256 TLSv1.2 Kx=DH       Au=RSA  Enc=AESGCM(128) Mac=AEAD
ECDHE-ECDSA-AES256-SHA384 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=AES(256)  Mac=SHA384
ECDHE-RSA-AES256-SHA384 TLSv1.2 Kx=ECDH     Au=RSA  Enc=AES(256)  Mac=SHA384
DHE-RSA-AES256-SHA256   TLSv1.2 Kx=DH       Au=RSA  Enc=AES(256)  Mac=SHA256
ECDHE-ECDSA-AES128-SHA256 TLSv1.2 Kx=ECDH     Au=ECDSA Enc=AES(128)  Mac=SHA256
ECDHE-RSA-AES128-SHA256 TLSv1.2 Kx=ECDH     Au=RSA  Enc=AES(128)  Mac=SHA256
DHE-RSA-AES128-SHA256   TLSv1.2 Kx=DH       Au=RSA  Enc=AES(128)  Mac=SHA256
ECDHE-ECDSA-AES256-SHA  TLSv1 Kx=ECDH     Au=ECDSA Enc=AES(256)  Mac=SHA1
ECDHE-RSA-AES256-SHA    TLSv1 Kx=ECDH     Au=RSA  Enc=AES(256)  Mac=SHA1
DHE-RSA-AES256-SHA      SSLv3 Kx=DH       Au=RSA  Enc=AES(256)  Mac=SHA1
ECDHE-ECDSA-AES128-SHA  TLSv1 Kx=ECDH     Au=ECDSA Enc=AES(128)  Mac=SHA1
ECDHE-RSA-AES128-SHA    TLSv1 Kx=ECDH     Au=RSA  Enc=AES(128)  Mac=SHA1
DHE-RSA-AES128-SHA      SSLv3 Kx=DH       Au=RSA  Enc=AES(128)  Mac=SHA1
AES256-GCM-SHA384       TLSv1.2 Kx=RSA      Au=RSA  Enc=AESGCM(256) Mac=AEAD
AES128-GCM-SHA256       TLSv1.2 Kx=RSA      Au=RSA  Enc=AESGCM(128) Mac=AEAD
AES256-SHA256           TLSv1.2 Kx=RSA      Au=RSA  Enc=AES(256)  Mac=SHA256
AES128-SHA256           TLSv1.2 Kx=RSA      Au=RSA  Enc=AES(128)  Mac=SHA256
AES256-SHA              SSLv3 Kx=RSA      Au=RSA  Enc=AES(256)  Mac=SHA1
AES128-SHA              SSLv3 Kx=RSA      Au=RSA  Enc=AES(128)  Mac=SHA1

 openssl s_client -connect 152.96.7.8:443 -cipher ECDHE-RSA-CHACHA20-POLY1305
CONNECTED(00000006)
Can't use SSL_get_servername
depth=0 C = UK, ST = England, L = London, O = localhost, OU = localhost, CN = localhost, emailAddress = admin@localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 C = UK, ST = England, L = London, O = localhost, OU = localhost, CN = localhost, emailAddress = admin@localhost
verify error:num=10:certificate has expired
notAfter=Feb 15 08:04:30 2017 GMT
verify return:1
depth=0 C = UK, ST = England, L = London, O = localhost, OU = localhost, CN = localhost, emailAddress = admin@localhost
notAfter=Feb 15 08:04:30 2017 GMT
verify return:1
---
Certificate chain
 0 s:C = UK, ST = England, L = London, O = localhost, OU = localhost, CN = localhost, emailAddress = admin@localhost
   i:C = UK, ST = England, L = London, O = localhost, OU = localhost, CN = localhost, emailAddress = admin@localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDljCCAn4CCQDiGU3GuzXKCDANBgkqhkiG9w0BAQUFADCBjDELMAkGA1UEBhMC
VUsxEDAOBgNVBAgMB0VuZ2xhbmQxDzANBgNVBAcMBkxvbmRvbjESMBAGA1UECgwJ
bG9jYWxob3N0MRIwEAYDVQQLDAlsb2NhbGhvc3QxEjAQBgNVBAMMCWxvY2FsaG9z
dDEeMBwGCSqGSIb3DQEJARYPYWRtaW5AbG9jYWxob3N0MB4XDTE2MDIxNjA4MDQz
MFoXDTE3MDIxNTA4MDQzMFowgYwxCzAJBgNVBAYTAlVLMRAwDgYDVQQIDAdFbmds
YW5kMQ8wDQYDVQQHDAZMb25kb24xEjAQBgNVBAoMCWxvY2FsaG9zdDESMBAGA1UE
CwwJbG9jYWxob3N0MRIwEAYDVQQDDAlsb2NhbGhvc3QxHjAcBgkqhkiG9w0BCQEW
D2FkbWluQGxvY2FsaG9zdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
ALtT2NQIXvVC7DD05AGkgaCF/dViK4AtgbC5j02ayjcAOzfBP12tkjD4MnHqL/Kz
NGCGQHNuTGFGWkO5lrMldOLR9CXtVfqwiPU/llRIRjASWzTEkmPD9zTPropwsav2
wejRXm7p01NW2l6tfeCsvXuRUMsDL52TZAG3jlZQ4gae44MYg1nWtEC11iCjKSD1
B7goswSetNHSzu9t8B49NIycF2AzYSEZoe184XMaD6w/JoE8jAEmkXU6UblmcGwY
55fzwKyCp5q93tVWWLtRM5N8xnypW/8WutR8vQVsZGV0rHr92aApVIHZIQLhRL9F
9N7clYeRszjIDObws5Lz8VkCAwEAATANBgkqhkiG9w0BAQUFAAOCAQEAf1Mk3VXU
O2nsOl3Cxr1RY8dFzqJRWaKhT+6C+maWmI599D8yWMzU4ozjbfdTTrXxkjgdf82c
PthBRjtbj2a0yLP6XPAkLPo6Z+biV/S/hCf9HUMs4AiPAXMwmjFipwqT/fCIChYe
TF7ZC/QSfukjKQ6iLHVsJHDQS2DsP0A0q+cKlxxnQqLzvOEKidu2TTZnFUD5Z32Y
gAaXN/ae5t0xd+yqJLVoKp0azWsOsGpyyQCJQH/2/p60WAwyaSxoOT8XyDY50sfu
R3il5I4WDPw/3dniWovoVmhyjyjVV750/6fgEyHu98LhAq3e4qM6YH6EIyRuN56V
ZrsF0yyago6Dkg==
-----END CERTIFICATE-----
subject=C = UK, ST = England, L = London, O = localhost, OU = localhost, CN = localhost, emailAddress = admin@localhost

issuer=C = UK, ST = England, L = London, O = localhost, OU = localhost, CN = localhost, emailAddress = admin@localhost

---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1555 bytes and written 316 bytes
Verification error: certificate has expired
---
New, TLSv1.2, Cipher is ECDHE-RSA-CHACHA20-POLY1305
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-CHACHA20-POLY1305
    Session-ID: B770728BBE72A9AE042E696695CBCA66DB474B310670BFA214DA11ACB87F121F
    Session-ID-ctx: 
    Master-Key: AA387DC1E233B4941B03F2826EB6CD9DA17C0E9025524C4B79CDD203CE636D0B574CB88599A0FEB59A0A33D25FED733F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - a8 51 53 a6 fb 04 3c 7b-fb 67 69 4f 43 93 c9 b1   .QS...<{.giOC...
    0010 - 67 de 7a d4 47 f0 5e bc-00 8c 21 c4 0d 80 50 3d   g.z.G.^...!...P=
    0020 - 99 4c 51 34 ea 41 53 0b-d9 04 70 8b 21 12 2c 1c   .LQ4.AS...p.!.,.
    0030 - 8c 82 b6 da 40 c4 ba e5-3e 5e e0 ee b7 6d 00 05   ....@...>^...m..
    0040 - a4 30 b1 f8 dd 5d 73 05-20 9e 7a bf 76 84 cd e4   .0...]s. .z.v...
    0050 - ce aa df b0 f8 02 ba 89-30 15 40 d1 c4 54 41 59   ........0.@..TAY
    0060 - e4 ab 36 1e 5b db b1 74-d7 b2 8d 07 2e 40 41 f2   ..6.[..t.....@A.
    0070 - f0 03 f6 71 10 d6 ef 41-e1 54 67 ed 75 5d b0 d1   ...q...A.Tg.u]..
    0080 - ab 21 b5 0e 19 f9 22 36-07 35 87 15 34 b6 89 8c   .!...."6.5..4...
    0090 - a1 89 69 d0 8b 81 13 04-d5 a5 1d 66 90 e7 a4 98   ..i........f....
    00a0 - c3 d2 a3 5c 3a 18 04 86-49 43 b5 b6 83 ec 01 96   ...\:...IC......

    Start Time: 1609915483
    Timeout   : 7200 (sec)
    Verify return code: 10 (certificate has expired)
    Extended master secret: yes
---
GET /
Let's do the ChaCha dance! Here is your flag: 49f36fae-90f3-483e-80e9-8cbe95e63ecaclosed

Using volatility

https://resources.infosecinstitute.com/topic/memory-forensics-and-analysis-using-volatility/

Blue rays

~/codeplay/basic_exp$ telnet 152.96.7.12 4242
Trying 152.96.7.12...
Connected to 152.96.7.12.
Escape character is '^]'.
Welcome to the Hacking-Lab BluRay Database!
1) Add BluRay
2) Remove BluRay
3) Edit BluRay
4) Print BluRay
5) Exit



