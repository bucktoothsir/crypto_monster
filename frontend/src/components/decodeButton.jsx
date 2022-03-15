import React from "react";
import Button from "./button";
import { PlainTextContext} from "./contexts/plainTextContext";
import { CipherTextContext} from "./contexts/cipherTextContext";

const DecodeButton = (props) => {
    const cipherKeyValue = props.cipherKeyValue;
    const decodeAPI = props.decodeAPI;
    const plainTextContext = React.useContext(PlainTextContext);
    const cipherTextContext = React.useContext(CipherTextContext);
    let bodyData = cipherKeyValue;
    bodyData["ciphertext"] = cipherTextContext.cipherText;

    const onClick = () => {
        // Simple POST request with a JSON body using fetcht
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(bodyData)
        };
        fetch(decodeAPI, requestOptions)
        .then(response => response.json())
        .then(res => {
            if (res.status === "ok"){
                plainTextContext.setPlainText(res["plaintext"])
            }
            }
        );
    }

    const text = 'Decode';
    return (
        <Button text={text}
        onClick={onClick}
        className="place-content-center items-center inline-flex  mt-4 font-bold antialiased font-mono bg-green-500 w-1/2 text-white hover:bg-green-800 focus:ring-4 focus:ring-green-800 font-medium rounded-full text-lg px-5 py-2.5 mr-2 mb-2 dark:bg-cyan-600 dark:hover:bg-cyan-700 dark:focus:ring-cyan-800"/>
    )
}
export default DecodeButton;