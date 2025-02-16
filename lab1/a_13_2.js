var zlib = require('zlib');

var str1 = "abc";
var str2 = "SomeRandommStr123";
var loopTime = 10;

function compress(err, buf) {
    var res = buf.toString('base64');
    console.log("After Compression: " + res)
}

function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}
async function buildUpString(currentStr, repeatStr, loopTime) {
    for (let step = 0;step < loopTime;step++) {
        var input = new Buffer.from(currentStr);
        console.log("Current loop number: " + step)
        console.log("Before compression: " + currentStr)
        zlib.deflate(input, compress)
        currentStr += repeatStr
        await delay(1000);
    }
}

var currentStr = str1
buildUpString(currentStr, str1, loopTime);

//console.log("=========================================");
var currentStr2 = str2
//buildUpString(currentStr2, str2, loopTime);