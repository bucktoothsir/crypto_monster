import React from 'react'

export const PlainTextContext = React.createContext("")

export const PlainTextProvider = (props) => {
    const [plainText, setPlainText] = React.useState("");
    return (
        <PlainTextContext.Provider value={{plainText, setPlainText}}>
            {props.children}
        </PlainTextContext.Provider>
    );
}