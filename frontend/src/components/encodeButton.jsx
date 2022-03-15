import React from "react";
import Button from "./button";
import { PlainTextContext} from "./contexts/plainTextContext";
import { CipherTextContext} from "./contexts/cipherTextContext";

const EncodeButton = (props) => {
    const cipherKeyValue = props.cipherKeyValue;
    const encodeAPI = props.encodeAPI;
    const plainTextContext = React.useContext(PlainTextContext);
    const cipherTextContext = React.useContext(CipherTextContext);
    let bodyData = cipherKeyValue;
    bodyData["plaintext"] = plainTextContext.plainText;
    const onClick = () => {
        // Simple POST request with a JSON body using fetcht
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(bodyData)
        };
        fetch(encodeAPI, requestOptions)
        .then(response => response.json())
        .then(res => {
            if (res.status === "ok"){
                cipherTextContext.setCipherText(res["ciphertext"])
            }
            }
        );
    }

    const text = 'Encode';
    return (
        <Button
            className="place-content-center text-center inline-flex items-center mt-4 font-bold antialiased font-mono bg-green-500 w-1/2 text-white hover:bg-green-800 focus:ring-4 focus:ring-green-800 font-medium rounded-full text-lg px-5 py-2.5 mr-2 mb-2"
            text={text}
            onClick={onClick}
            />
    )

}

export default EncodeButton;