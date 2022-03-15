import React from "react";
import TextArea from "./textArea";
import { PlainTextContext} from "./contexts/plainTextContext";

const EncodeTextArea = (prop) => {
    const title = prop.title;
    const plainTextContext = React.useContext(PlainTextContext)
    const onInput = React.useCallback(
        (e) => {
            e.target.style.height = "";
            e.target.style.height = e.currentTarget.scrollHeight + "px"
            plainTextContext.setPlainText(e.currentTarget.value)
        }
    )

    return (
        <TextArea title={title} value={plainTextContext.plainText} onInput={onInput}/>
    )
}

export default EncodeTextArea;