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