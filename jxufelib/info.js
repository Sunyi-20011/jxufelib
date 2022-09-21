const rsa = require("./security.js");
let modulus = "00ae1d6d965af848bc5814af9073dce0b03ee18f5f2448f922549826c7ae54601ea7c09ef026c8997343833160298849a9b73483f324100b7095b4bd10afabed447ea1b0871ca613aeb391f1e7361f3ae0a147d1431ddd1c1c080ba46a51d70dc93508a9fc4dcc683ed64d429e026d1335ab01020cfee00e788d78dced6fe5199b";
let exponent = "010001";
let rsaArea = rsa.getKeyPair(exponent, "", modulus);
function encry_info(info){
    //"9019,119,1,2022-09-19,12:00"
    let result = rsa.encryptedString(rsaArea, info);
    console.log(result);
    return result;
}