import React from "react";
import {BiChevronDown, BiLock, BiLockOpen} from "react-icons/bi";

const Button = (prop) => {
    const text = prop.text;
    const onClick = prop.onClick;
    const className = prop.className;

    const getIcon = (text) => {
        if (text == "Encode"){
            return <p> <BiLock /> </p>;
        } else if (text == "Decode"){
            return <p> <BiLockOpen /> </p>;
        } else {
            return <p> <BiChevronDown /> </p>;
        }
    }

    return (
        <button className={className} type="button" onClick={onClick}>
            <p className="font-bold antialiased font-mono"> 
                {text}
            </p>
            {
                getIcon(text)
            }
        </button>
    )
}

export default Button;
