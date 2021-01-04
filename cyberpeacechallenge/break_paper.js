
function break_paper(){
    var script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
    script.type = 'text/javascript';
    document.getElementsByTagName('head')[0].appendChild(script);
    $.getJSON('http://query.yahooapis.com/v1/public/yql?q=select%20%2a%20from%20yahoo.finance.quotes%20WHERE%20symbol%3D%27WRC%27&format=json&diagnostics=true&env=store://datatables.org/alltableswithkeys&callback', function(data) {
    console.log(data)
});
}

function break_paper2(){
    var getJSON = function(url, callback) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.responseType = 'json';
        xhr.onload = function() {
          var status = xhr.status;
          if (status === 200) {
            callback(null, xhr.response);
          } else {
            callback(status, xhr.response);
          }
        };
        xhr.send();
    };

    getJSON('https://f3235ebc-edc1-4f39-85cc-94262cd73ecb.idocker.vuln.land/getEditionDefsWithSubscriptions',
    function(err, data) {
    if (err !== null) {
        alert('Something went wrong: ' + err);
    } else {
        alert('Your query count: ' + data.query.count);
     }
    });
}