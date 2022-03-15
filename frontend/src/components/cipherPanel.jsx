import React from "react";
import 'flowbite';
import Button from "./button";

import DropdownCard from "./dropdownCard";
import EncodeButton from "./encodeButton"
import DecodeButton from "./decodeButton"
import Tooltip from "./tooltip";
import CipherKeyInput from "./cipherKeyInput";


function isNumeric(value) {
    return /^-?\d+$/.test(value)
}

const CipherPanel = (props) => {
    const cipherOptions = props.cipherOptions;
    const defaultCipher = props.defaultCipher
    const encodeAPIs = props.encodeAPIs
    const decodeAPIs = props.decodeAPIs
    const [cipherOption, setCipherOption] = React.useState(defaultCipher);
    const [menuOpen, setOpen] = React.useState(false);

    const buttonOnClick = () => {
        setOpen(menuOpen => !menuOpen)
    }

    const MenuClick = React.useCallback(
        (event) => {
            buttonOnClick();
            setCipherOption(event.target.innerHTML);
            setCaesarShiftValue("");
            setLinearAValue("");
            setLinearBValue("");
            setVigenereKeyValue("");
            setVigenereKeylenValue("")
        },
        [],
    );

    // caesar key
    const caesarKey = props.cipherKey.CAESAR_KEY;
    const [caesarShiftValue, setCaesarShiftValue] = React.useState("");
    const caesarShiftOnInput = (e) => { setCaesarShiftValue(e.target.value)
    }

    // linear key
    const linearKey = props.cipherKey.LINEAR_KEY;
    const [linearAValue, setLinearAValue] = React.useState("");
    const linearAOnInput = (e) => {
        setLinearAValue(e.target.value)
    }
    const [linearBValue, setLinearBValue] = React.useState("");
    const linearBOnInput = (e) => {
        setLinearBValue(e.target.value)
    }

    // vigenere Key
    const vigenereKey = props.cipherKey.VIGENERE_KEY 
    const [vigenereKeyValue, setVigenereKeyValue] = React.useState("");
    const vigenereKeyInput = (e) => {
        setVigenereKeyValue(e.target.value)
    }
    const [vigenereKeylenValue, setVigenereKeylenValue] = React.useState("");
    const vigenereKeylenInput = (e) => {
        setVigenereKeylenValue(e.target.value)
    }

    let cipherKeyValue = {}
    if (cipherOption === "Caesar Cipher"){
        if (isNumeric(caesarShiftValue)){
            cipherKeyValue["key"] = Number(caesarShiftValue)
            }
    } else if(cipherOption === "Linear Cipher"){
        if (isNumeric(linearAValue) && isNumeric(linearBValue)){
            cipherKeyValue["a"] = Number(linearAValue)
            cipherKeyValue["b"] = Number(linearBValue)
        }
    } else if (cipherOption === "Vigenère Cipher"){
        if (!(vigenereKeyValue === "")){
            cipherKeyValue["key"] = vigenereKeyValue
        }
        if (isNumeric(vigenereKeylenValue)){
            cipherKeyValue["keylen"] = Number(vigenereKeylenValue)
        }
    }
    const encodeAPI = encodeAPIs[cipherOption]
    const decodeAPI = decodeAPIs[cipherOption]

    return ( 
        <div className="mx-8 h-full w-1/5">
            <header>
                <Button
                    text={cipherOption}
                    className="place-content-center h-14 bg-green-500  w-full text-white focus:ring-4 focus:ring-green-800 rounded-lg text-lg px-4 py-2.5 inline-flex items-center"
                    onClick={buttonOnClick}/>
                {menuOpen && <DropdownCard options={cipherOptions} onClick={MenuClick}/>}
            </header>
            <div className="mt-8">
                {cipherOption === "Caesar Cipher" &&
                        <CipherKeyInput
                            onInput={caesarShiftOnInput}
                            keyName={caesarKey}
                            value={caesarShiftValue}
                        />
                }

                {cipherOption === "Linear Cipher" &&
                        <CipherKeyInput
                            onInput={linearAOnInput}
                            keyName={linearKey[0]}
                            value={linearAValue}
                        />
                }
                {cipherOption === "Linear Cipher" &&
                        <CipherKeyInput
                            onInput={linearBOnInput}
                            keyName={linearKey[1]}
                            value={linearBValue}
                        />
                }

                {cipherOption === "Vigenère Cipher" &&
                        <CipherKeyInput
                            onInput={vigenereKeyInput}
                            keyName={vigenereKey[0]}
                            value={vigenereKeyValue}
                        />
                }
                {cipherOption === "Vigenère Cipher" &&
                        <CipherKeyInput
                            onInput={vigenereKeylenInput}
                            keyName={vigenereKey[1]}
                            value={vigenereKeylenValue}
                        />
                }
            </div>

            <div className='mt-5'>
                <Tooltip />
                    <div className="flex flex-row ml-2">
                        <EncodeButton cipherKeyValue={cipherKeyValue} encodeAPI={encodeAPI}/>
                        <DecodeButton cipherKeyValue={cipherKeyValue} decodeAPI={decodeAPI}/>
                    </div>
            </div>
        </div>
    ) 
}

export default CipherPanel;