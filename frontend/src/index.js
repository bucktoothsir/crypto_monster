var API = "https://5tg3bs55i7.execute-api.us-west-2.amazonaws.com/dev"
function select_cipher(ele) {
  let svg = '<svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>'
  const ciphers = ["caesar", "linear", "vigenere"]
  for (let i = 0; i < ciphers.length; i++) {
    if (ciphers[i] == ele.id){
      document.getElementById(ciphers[i]+'_info').style.display = "block"
      var new_value = ciphers[i]
    }
    else{
      document.getElementById(ciphers[i]+'_info').style.display = "none" 
    }
  }
  document.getElementById("cipher_type_text").innerHTML = ele.innerHTML
  document.getElementById("cipher_type").value = new_value
  if (new_value == 'caesar'){
    document.getElementById("caesar_shift").value = null
  }
  else if(new_value == 'linear'){
    document.getElementById("linear_slope").value = null
    document.getElementById("linear_intercept").value = null
  }
  else if(new_value == 'vigenere'){
    document.getElementById("vigenere_key").value = null
    document.getElementById("vigenere_key_len").value = null
  }
}

async function encode() {
  let plaintext = document.getElementById("plaintext_textarea").value
  let cipher_type = document.getElementById("cipher_type").value
  if (cipher_type == "caesar"){
    let key = document.getElementById("caesar_shift").value
    data = {
      "plaintext": plaintext,
      "key": Number(key)
    }
    let path = "/cipher/caesar/encode"
    fetch(API+path, {
      "method": "post",
      "body": JSON.stringify(data)})
    .then((response) => response.json())
    .then((encode_res) => {
      update_ciphertext(encode_res)
    })
    .catch((error) => {
      console.error('Error:', error);
    })
  }
  else if (cipher_type == 'linear'){
    let key_slope = document.getElementById("linear_slope").value
    let key_intercept = document.getElementById("linear_intercept").value
    data = {
      "plaintext": plaintext,
      "a": Number(key_slope),
      "b": Number(key_intercept)
    }
    let path = "/cipher/linear/encode"
    fetch(API+path, {
      "method": "post",
      "body": JSON.stringify(data)})
    .then((response) => response.json())
    .then((encode_res) => {
      update_ciphertext(encode_res)
    })
    .catch((error) => {
      console.error('Error:', error);
    })
  }
  else if (cipher_type == "vigenere"){
    let key = document.getElementById("vigenere_key").value
    data = {
      "plaintext": plaintext,
      "key": key
    }
    console.log(key)
    let path = "/cipher/vigenere/encode"
    fetch(API+path, {
      "method": "post",
      "body": JSON.stringify(data)})
    .then((response) => response.json())
    .then((encode_res) => {
      update_ciphertext(encode_res)
    })
    .catch((error) => {
      console.error('Error:', error);
    })
  }
}

async function decode() {
  let ciphertext = document.getElementById("ciphertext_textarea").value
  let cipher_type = document.getElementById("cipher_type").value
  data = {
    "ciphertext": ciphertext,
  }
  if (cipher_type == "caesar"){
    let key = document.getElementById("caesar_shift").value
    if (isNumeric(key)){
      data["key"] = Number(key)
    }
    let path = "/cipher/caesar/decode"
    fetch(API+path, {
      "method": "post",
      "body": JSON.stringify(data)})
    .then((response) => response.json())
    .then((decode_res) => {
      update_plaintext(decode_res)
    })
    .catch((error) => {
      console.error('Error:', error);
    })
  }
  else if (cipher_type == 'linear'){
    let key_slope = document.getElementById("linear_slope").value
    let key_intercept = document.getElementById("linear_intercept").value
    if (isNumeric(key_slope) && isNumeric(key_intercept)){
      data["a"] = Number(key_slope)
      data["b"] = Number(key_intercept)
    }
    let path = "/cipher/linear/decode"
    fetch(API+path, {
      "method": "post",
      "body": JSON.stringify(data)})
    .then((response) => response.json())
    .then((decode_res) => {
      update_plaintext(decode_res)
    })
    .catch((error) => {
      console.error('Error:', error);
    })
  }
  else if (cipher_type == "vigenere"){
    let key = document.getElementById("vigenere_key").value
    let keylen = document.getElementById("vigenere_key_len").value
    if (!(key === "")){
      data['key'] = key
    }
    if (isNumeric(keylen)){
      data['keylen'] = Number(keylen)
    }
    console.log(data)
    let path = "/cipher/vigenere/decode"
    fetch(API+path, {
      "method": "post",
      "body": JSON.stringify(data)})
    .then((response) => response.json())
    .then((decode_res) => {
      update_plaintext(decode_res)
    })
    .catch((error) => {
      console.error('Error:', error);
    })
  }
}

function update_ciphertext(encode_res) {
  if (encode_res.status == 'ok'){
    document.getElementById("ciphertext_textarea").style.height = document.getElementById("plaintext_textarea").style.height 
    document.getElementById("ciphertext_textarea").value = encode_res.ciphertext
  }
}

function update_plaintext(decode_res) {
  if (decode_res.status == 'ok'){
    document.getElementById("plaintext_textarea").style.height = document.getElementById("ciphertext_textarea").style.height 
    document.getElementById("plaintext_textarea").value = decode_res.plaintext
  }
}

function isNumeric(value) {
  return /^-?\d+$/.test(value)
}