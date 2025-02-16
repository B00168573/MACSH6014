var zlib = require('zlib');

var compressedStr1 = "eJzzyc9Lyc8DAAgpAms=";
var compressedStr2 = "eJxzSi3KycwDAAfXAl0=";
var compressedStr3 = "eJzzSy1XiMwvygYADKUC8A==";

function decompress(err, buf) {
    if (buf == undefined)
        console.log("The value to decompress is in incorrect format for processing Base64!");
    else
        console.log("Decompressed string is: " + buf.toString("utf8"));
}

zlib.inflate(new Buffer.from(compressedStr1, 'base64'), decompress);
zlib.inflate(new Buffer.from(compressedStr2, 'base64'), decompress);
zlib.inflate(new Buffer.from(compressedStr3, 'base64'), decompress);
