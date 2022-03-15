import React from "react";

const CipherKeyInput = (props) => {
    const value = props.value
    const onInput = props.onInput
    const keyName = props.keyName;
    return (
        <div className="border-2 rounded-lg h-24 shadow-lg shadow-green-800 border-green-600 bg-white">
            <div className="relative z-0 mt-8 mb-4 w-4/5 ml-4 group">
                <input 
                    className="ml-2 text-center font-bold antialiased font-mono block py-2.5 px-0 w-full text-lg text-green-600 bg-transparent border-0 border-b-2 border-green-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-green-600 peer"
                    placeholder=" "
                    required 
                    onInput={onInput} 
                    value={value}
                />
                <label className="absolute text-base text-green-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-green-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
                <p className="text-green-700 font-bold antialiased font-mono">
                    {keyName}
                </p>
                </label>
            </div>
        </div>
    )
}

export default CipherKeyInput;