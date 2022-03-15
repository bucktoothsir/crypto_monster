import React from "react";
import TextArea from "./textArea";
import { CipherTextContext} from './contexts/cipherTextContext';

const DecodeTextArea = (prop) => {
    const title = prop.title;
    const cipherTextContext = React.useContext(CipherTextContext)
    //const [value, setValue] = React.useState(cipherTextContext.cipherText)
    const onInput = React.useCallback(
        (e) => {
            e.target.style.height = "";
            e.target.style.height = e.currentTarget.scrollHeight + "px"
            //setValue(e.currentTarget.value)
            cipherTextContext.setCipherText(e.currentTarget.value)
        }
    )
    return (
        <TextArea title={title} value={cipherTextContext.cipherText} onInput={onInput}/>
    )
}

export default DecodeTextArea;