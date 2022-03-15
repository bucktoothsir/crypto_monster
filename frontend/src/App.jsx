import React, { useEffect } from 'react';
import './index.css';
import CipherPanel from './components/cipherPanel';
import EncodeTextArea from './components/encodeTextArea';
import DecodeTextArea from './components/decodeTextArea';
import { PlainTextProvider} from "./components/contexts/plainTextContext";
import { CipherTextProvider } from './components/contexts/cipherTextContext';
import configData from './config'


const App = () => {
    useEffect(() => {
        document.body.className = "bg-emerald-200/50"
        document.title = configData.TITLE
    }
    )
    console.log(configData)
    return ( 
        <div className="application">
        <div className="flex flex-row mt-36 h-96 w-full place-content-center">
            <PlainTextProvider>
            <CipherTextProvider>
                <EncodeTextArea title={configData.ENCODE_AREA_TITLE}/>
                <CipherPanel cipherOptions={configData.CIPHER_OPTIONS}
                defaultCipher={configData.DEFAULT_CIPHER}
                cipherKey={configData.CIPHER_KEY}
                encodeAPIs={configData.ENCODE_APIS}
                decodeAPIs={configData.DECODE_APIS}
                />
                <DecodeTextArea title={configData.DECODE_AREA_TITLE}/>
            </CipherTextProvider>
            </PlainTextProvider>
        </div>
        </div>
        )
};

export default App;



