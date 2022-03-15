import React from 'react'

export const CipherTextContext = React.createContext("")

export const CipherTextProvider = (props) => {
    const [cipherText, setCipherText] = React.useState("");
    return (
        <CipherTextContext.Provider value={{cipherText, setCipherText}}>
            {props.children}
        </CipherTextContext.Provider>
    );
}